from django import forms
from .models import PostAJob

class JobPostForm(forms.ModelForm):

    class Meta:
        model = PostAJob
        fields = ('title', 'description')

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)