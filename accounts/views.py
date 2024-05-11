from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from.forms import SignuoForm,UserActivateForm
from.models import Profile
from django.core.mail import send_mail

# Create your views here.

def signup(request):
    '''
    - create new user
    - send email : code
    - redirect : activate
    '''
    if request.user.is_uthenticated:
        return redirect('/')
    if request.method== 'POST':
        form=SignuoForm(request.POST)
        if form.is_valid():
            usename=form.cleaned_data['username']
            email=form.cleaned_data['email']
            user=form.save(commit=False)
            user.is_active=False
            
            form.save()  #trigger signal-->create profile:code
            profile=Profile.objects.get(user__username=username)
            #send email
            send_mail(
                " Activate Your Account",
                "Welcome {username}\n Use this code{profile.code} to activate your account",
                "pythondeveloper@gmail.com",
               [email],
               fail_silently=False,
            )
            return redirect(f'/account/{username}/activate')
        
    else:
        form=SignuoForm()
    return render(request,'accounts/signup.html',{'form':form})
       
    
'''
-create new user
-send email:code
-redirect:activate
'''

def user_activate(request,username):
    profile=Profile.objects.get(user__username=username)
    if request.method== 'POST':
        form=UserActivateForm(request.POST)
        if form.is_valid():
            code=form.cleaned_data['code']
            if code==profile.code:
                profile.code=''
                
                user=User.objects.get(username=username)
                user.is_active=True
                
                user.save()
                profile.save()
                
                return redirect('/account/login')
        
    else:
        form=UserActivateForm()
    return render(request,'accounts/activate.html',{'form':form})
       
    
'''
code--->activate
redirect : login
'''
