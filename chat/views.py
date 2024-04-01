from django.shortcuts import render, redirect
from chat.forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout
from chat.models import Room

# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')  # Redirect to login after successful registration
#     else:
#         form = RegistrationForm()
#     return render(request, 'chat/registration.html', {'form': form})



# def login_view(request):
#     error_message = None
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('chatHome')  # Redirect to home page after successful login
#         else:
#             error_message = 'Username or password is incorrect.'
#     return render(request, 'chat/login.html', {'error_message': error_message})

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'chat/room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })


def chathome(request):
    if not request.user.is_authenticated:
        return redirect('chat-login')  # Redirect to login if user is not authenticated
    return render(request, 'chat/home.html')