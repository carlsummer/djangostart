import MySQLdb
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import UserMessage


# Create your views here.

def getform(request):
    message = None
    # all_messages = UserMessage.objects.all()
    all_messages = UserMessage.objects.filter(name='bobby', address='北京')

    if all_messages:
        message = all_messages[0]

    # for message in all_messages:
    #     print(message.name)
    #
    # if request.method == "POST":
    #     name = request.POST.get('name','')
    #     message = request.POST.get('message', '')
    #     address = request.POST.get('address', '')
    #     email = request.POST.get('email', '')
    #     user_message = UserMessage()
    #     user_message.name = name
    #     user_message.message = message
    #     user_message.address = address
    #     user_message.email = email
    #     #user_message.object_id = "helloword2"
    #     user_message.save()
    return render(request, 'message_form.html', {
        "my_message": message
    })


def index(request):
    return render(request, 'index.html', {'user': request.user})


@login_required
def protected(request):
    return render(request, 'protected.html', {'user': request.user})


def logout(request):
    auth.logout(request)
    return redirect("https://cas.shoudujiyin.com/cas/logout?service=http://127.0.0.1:8089/index/")
