from django import forms
from .models import PostAJob

class JobPostForm(forms.ModelForm):

    class Meta:
        model = PostAJob
        fields = ('title', 'description')