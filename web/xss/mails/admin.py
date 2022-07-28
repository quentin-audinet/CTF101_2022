from django.contrib import admin

from mails.models import Message, MessageReceived, AdminMessage, AdminMessageReceived

admin.site.register(Message)
admin.site.register(MessageReceived)
admin.site.register(AdminMessage)
admin.site.register(AdminMessageReceived)

