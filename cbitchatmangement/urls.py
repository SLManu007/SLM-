"""cbitchatmangement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views as mainview
from students import views as sviews
from mangement import views as mvi
from chat import views as chatviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mainview.home,name='home'),
    path('studenthome',sviews.studenthome, name='studenthome'),
    
    
    
    #managment app urls
    path('mhome',mvi.mhome,name='mhome'),
    path('AdminLoginCheck',mvi.AdminLoginCheck,name='AdminLoginCheck'),
    path('addstudent',mvi.addstudent,name='addstudent'),
    path('ViewStudents', mvi.ViewRegisteredStudents,name='ViewRegStudents'),

    #Student app urls
    path('student-login', sviews.StudentLogin, name='student_login'),


    #chat app urls
    path('chat-home/', chatviews.chathome, name='chatHome'),
    # path('chat-login/', chatviews.login_view, name='chat-login'),
    # path('chat-register/', chatviews.register, name='chat-register'),
    path('<str:room>/', chatviews.room, name='room'),
   
]
