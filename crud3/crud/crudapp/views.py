from django.shortcuts import HttpResponse, redirect
from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
# from .forms import MobileLoginForm
# Create your views here.

# ADD and Show item
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg= User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration()
            messages.success(request,"Product Added Successfully !!!")
    else:
        fm = StudentRegistration()
    stud=User.objects.all()    
    return render(request,'enroll/Add.html',{'form':fm,'stu':stud})

#Update and Edit
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Updated Successfully !!!")
    else:
        pi=User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)    
    return render(request, 'enroll/updatestudent.html', {'form':fm})


# Delete Item

def delete_data(request, id):
    if request.method == 'POST':
        pi=User.objects.get(pk=id)   #pk=primary key
        pi.delete()
        messages.success(request, "Deleted Successfully !!!")
        return HttpResponseRedirect('/')
    
# Login
def mobile_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Add')
        else:
            message = 'Invalid username or password'
            return render(request, 'enroll/login.html', {'message': message})
    else:
        return render(request, 'enroll/login.html')