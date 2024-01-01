from django import forms
from board.models import Notice, EmailSubscriber


class NoticeForm(forms.ModelForm):
    
    class Meta():
        model = Notice
        fields = ('title','content','category','image','file')
        
        
        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass','name':'samir'}),
            'text':forms.Textarea(attrs={'type':'hidden'})
        }
        
        
        
class EmailSubscriberForm(forms.ModelForm):
    class Meta:
        model = EmailSubscriber
        fields = ['email']