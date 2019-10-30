from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages


def UserSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if User.objects.filter(username=username).exists():
            messages.warning(request,'Username Taken!')
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.warning(request, 'Email already exist!')
            return redirect('signup')
        elif password1 != password2:
            messages.warning(request, 'Password must match!')
            return redirect('signup')
        user = User.objects.create_user(username = username,
                                        email=email,
                                        password=password1)
        user.save()
        return redirect('login')
    return render(request, 'registration/signup.html')
