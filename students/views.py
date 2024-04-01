from django.shortcuts import render
from django.contrib import messages
from .models import studentmodels
# Create your views here.


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import studentmodels

def StudentLogin(request):
    if request.method == 'POST':
        Hallticket = request.POST.get('Hallticket')
        pswd = request.POST.get('pswd')
        print("User ID is =", Hallticket)
        try:
            user = studentmodels.objects.get(Hallticket=Hallticket, password=pswd)
            return redirect('studenthome')

        except studentmodels.DoesNotExist:  
            messages.error(request, 'Please check your login details')
            return redirect('student_login')  
        
    return render(request, 'student/studentlogin.html', {})



def studenthome(request):
    students = studentmodels.objects.all()

    return render(request,'chat/index.html',{'students':students})

