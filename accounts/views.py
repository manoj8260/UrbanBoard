from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from .models import User
from .forms import SignupForm,LoginForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core.utils import assign_permission
# for forget password
from django.contrib.auth.forms import PasswordResetForm,SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.utils.html import strip_tags
from accounts.emails import send_activation_email

def password_reset_request(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            try:
                user = User.objects.get(email=email)
                uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
                token = default_token_generator.make_token(user)
                current_site = get_current_site(request)
                context = {
                    "email": user.email,
                    "domain": current_site.domain,
                    "site_name": "UrbanBoard",
                    "uid": uidb64,
                    "user": user,
                    "token": token,
                    "protocol": "https" if request.is_secure() else "http",
                }
                html_message = render_to_string("email/password_reset_email.html", context)
                plain_message = strip_tags(html_message)
                subject = "🔐 Reset Your Password"
                from_email = settings.DEFAULT_FROM_EMAIL
                to_email = [user.email]
                email = EmailMultiAlternatives(
                    subject=subject,
                    body=plain_message,
                    from_email=from_email,
                    to=to_email                     
                )
                email.attach_alternative(html_message, 'text/html')
                email.send()
            except User.DoesNotExist:
                pass  # Don’t reveal whether email exists

            messages.success(request, "If an account exists with the email you entered, you'll receive password reset instructions shortly.")         
            return redirect('password_reset_done')
        
        # Handles invalid form (e.g., empty email, bad format)
        return render(request, "email/password_reset.html", {"form": form})

    else:          
        form = PasswordResetForm()
        return render(request, "email/password_reset.html", {"form": form})


def password_reset_confirm(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (User.DoesNotExist, TypeError, ValueError, OverflowError):
        user = None
    if user and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                return redirect('password_reset_complete')
        else:
            form = SetPasswordForm(user)
        return render(request, 'email/password_reset_confirm.html', {'form': form})
    
    # Invalid or expired link
    return render(request, 'email/password_reset_invalid.html')
    
def password_reset_done(request):
    return render(request, "email/password_reset_done.html")


def password_reset_complete(request):
    return render(request, "email/password_reset_complete.html")


# Create your views here.
def Signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            raw_pass=form.cleaned_data.get('password')
            username = form.cleaned_data.get('email').split('@')[0]
            user.set_password(raw_pass)
            role = form.cleaned_data.get('role')
            user.username = username
            user.role=role
            user.save()
            assign_permission(user,role)
            send_activation_email(user)
            messages.success(request,'Successfully registered..')
            return render(request,'accounts/activation_pending.html')
    else:
        form=SignupForm()
    return render(request,'accounts/signup.html',{'form':form})

def Signin(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            identifier=form.cleaned_data.get('username') # either phone oe email
            password=form.cleaned_data.get('password')
            user=authenticate(request,username=identifier,password=password)
            if user is not None:
                login(request,user)
                request.session['identifier'] = identifier
                messages.success(request,'user logined...')
                if user.role=='landlord':
                    return redirect('landlord_dashboard')
                elif user.role=='boarder':
                    return redirect('boarder_dashboard')
                else:
                    return redirect('home')
            else:
                form.add_error(None,'wrong email or password')
    else:
        form=LoginForm()
    return render(request,'accounts/signin.html',{'form':form})

@login_required
def Logout(request):
    logout(request)
    return redirect('signup')

@login_required
def home(request):   
    return render(request,'accounts/home.html')

def activate_account(request,uidb64):
    user_id = urlsafe_base64_decode(uidb64).decode()
    user=get_object_or_404(User,id=user_id)
    try:
        if not user.is_active:
            user.is_active=True
            user.save()
            return render(request,'accounts/account_activate.html',{'role':user.role})
        else:
            return HttpResponse('Your Account is Activated')
    except User.DoesNotExist:
        return HttpResponse('Activation failed...invalid user , try again.')



@login_required
def google_role_redirect(request):
    user = request.user
    if not user.role:
        return redirect('select_role')
    
    # Redirect based on role
    if user.role == 'landlord':
        return redirect('landlord_dashboard')
    elif user.role == 'boarder':
        return redirect('boarder_dashboard')
    else:
        return redirect('select_role')

@login_required
def select_role(request):
    user = request.user
    if request.method == 'POST':
        role = request.POST.get('role')
        if role in ['landlord', 'boarder']:
            user.role = role
            user.save()
            return redirect('landlord_dashboard' if role == 'landlord' else 'boarder_dashboard')
        else:
            messages.error(request, "Please select a valid role.")
    return render(request, 'accounts/select_role.html')    

def clear_sesion(request):
    request.session.flush()
    return HttpResponse('done')