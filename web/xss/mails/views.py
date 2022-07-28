from django.shortcuts import render, redirect
from django.http import HttpResponse

from mails.models import Message, MessageReceived, AdminMessage, AdminMessageReceived
from mails.forms import MessageForm

import time
import hashlib

ADMIN_COOKIE = "T3LeC0oK_5uP3R_Co0K1e!!!"
ADMIN_MAIL = "telecook@telecom-paris.fr"

def check_session(request, response):
    if not(request.COOKIES.get('SESSION_ID')):
        token = hashlib.sha256(("3562e59d259ef9a3977ec913311f5b2f" + str(time.time())).encode()).hexdigest()
        response.set_cookie(key='SESSION_ID', value=token)
        return response
    else:
        return response


def accueil(request, mode):
    is_admin = False

    if request.COOKIES.get('ADMIN_TOKEN') == ADMIN_COOKIE:
        is_admin = True
        if mode == 1:
            MESSAGE = AdminMessageReceived
        elif mode == 2:
            MESSAGE = AdminMessage
    else:
        if mode == 1:
            MESSAGE = MessageReceived
        elif mode == 2:
            MESSAGE = Message


    if mode == 2 and not(is_admin):
        messages = MESSAGE.objects.filter(session=request.COOKIES.get('SESSION_ID'))[::-1]
    else:
        messages = MESSAGE.objects.all()[::-1]

    if is_admin and request.GET.get('delete') == 'YesIAmTheBotYouCanDeleteLastMessage!!:)':
        messages[0].delete()
        messages.pop(0)

    message_id = request.GET.get('id')
    try:
        if not(is_admin) and mode==2:
            current = MESSAGE.objects.get(id=message_id,session=request.COOKIES.get('SESSION_ID'))
        else:
            current = MESSAGE.objects.get(id=message_id)
        current.content = current.content.replace('\n', '<br/>')
    except:
        current = None
    response = render(request, 'mails/accueil.html', {'messages': messages, 'current': current, 'mode': mode, 'is_admin': is_admin})
    return check_session(request, response)

def new_mail(request):

    if request.COOKIES.get('ADMIN_TOKEN') == ADMIN_COOKIE:
        return redirect('read-mails', mode=1)

    if request.method == 'POST':
        form = MessageForm(request.POST)

        admin_message = AdminMessageReceived()
        message = Message()

        if form.is_valid():
            message.to = request.POST.get('to')
            message.obj = request.POST.get('obj')
            message.content = request.POST.get('content')
            message.session = request.COOKIES.get('SESSION_ID')
            message.save()

            if request.POST.get('to') == ADMIN_MAIL:
                admin_message.sender = request.POST.get('to')
                admin_message.obj = request.POST.get('obj')
                admin_message.content = request.POST.get('content')
                admin_message.session = request.COOKIES.get('SESSION_ID')
                admin_message.save()
            return redirect('read-mails', mode=1)
    else:
        form = MessageForm()

    response = render(request, 'mails/write.html')
    return check_session(request, response)

def home(request):
    return redirect('read-mails', mode=1)