from django  import forms

from mails.models import Message, AdminMessageReceived

class MessageForm(forms.ModelForm):
    
    class Meta:
        model = Message
        fields = "__all__"