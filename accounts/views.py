from django.shortcuts import render,redirect
from .models import User
from .forms import Signupform,LoginForm
from django.contrib.auth import login,logout,authenticate,get_user_model
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
            return redirect('signin')
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
    _User=get_user_model()
    try:
        user=_User.objects.get(id=user_id)
        if not user.is_active:
            user.is_active=True
            user.save()
            login(request,user)
            if user.role=='landlord':
                return redirect('landlord_dashboard')
            else:
                return redirect('boarder_dashboard')
        return HttpResponse('Your Account is Activated')
    except _User.DoesNotExist:
        return HttpResponse('Activation failed...invalid user , try again.')