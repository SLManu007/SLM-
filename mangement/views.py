from django.shortcuts import render
from django.contrib import messages
from students.models import studentmodels
from .forms import studentmodelsform


def mhome(request):
    return render(request,'mangement/home.html')
#login views
def AdminLoginCheck(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        pswd = request.POST.get('pswd')
        print("User ID is = ", email)
        if email == 'cbitadmin@gmail.com' and pswd == 'admin@cbit':
            return render(request, 'mangement/home.html', {'email': email})

        else:
            messages.success(request, 'Please Check Your Login Details')
    return render(request, 'mangmentlogin.html', {})

def addstudent(request):
    if request.method == 'POST':
        form = studentmodelsform(request.POST, request.FILES)  # Include request.FILES here
        if form.is_valid():
            print('Data is Valid')
            form.save()
            messages.success(request, 'You have been successfully registered')
            form = studentmodelsform()
            return render(request, 'mangement/addstudent.html', {'form': form})
        else:
            messages.error(request, 'Form submission failed. Please check the fields.')
            print("Invalid form")
    else:
        form = studentmodelsform()
    return render(request, 'mangement/addstudent.html', {'form': form})


def ViewRegisteredStudents(request):
    students = studentmodels.objects.all()
    return render(request, 'mangement/ViewRegisteredStudents.html',{'students':students})