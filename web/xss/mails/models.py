from django.db import models

class MessageReceived(models.Model):
    sender   = models.fields.CharField(max_length=100)
    obj     = models.fields.CharField(max_length=255)
    content = models.fields.TextField()

class Message(models.Model):
    to      = models.fields.CharField(max_length=100)
    obj     = models.fields.CharField(max_length=255)
    content = models.fields.TextField()
    session = models.fields.CharField(max_length=64, null=True, blank=True)

class AdminMessageReceived(models.Model):
    sender   = models.fields.CharField(max_length=100)
    obj     = models.fields.CharField(max_length=255)
    content = models.fields.TextField()
    session = models.fields.CharField(max_length=64, null=True, blank=True)

class AdminMessage(models.Model):
    to      = models.fields.CharField(max_length=100)
    obj     = models.fields.CharField(max_length=255)
    content = models.fields.TextField()