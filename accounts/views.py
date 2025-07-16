from django.shortcuts import render,redirect,get_object_or_404
from .models import User
from .forms import Signupform,LoginForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core.utils import assign_permission
from accounts.emails import send_activation_email
from django.http import HttpResponse

# Create your views here.
def Signup(request):
    if request.method=='POST':
        form=Signupform(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            raw_pass=form.cleaned_data.get('password')
            user.set_password(raw_pass)
            role = form.cleaned_data.get('role')
            user.save()
            assign_permission(user,role)
            send_activation_email(user)
            messages.success(request,'Successfully registered..')
            return render(request,'accounts/activation_pending.html')
    else:
        form=Signupform()
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

def activate_account(request,user_id):
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