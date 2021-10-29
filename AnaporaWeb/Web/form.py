from django import forms
from Web.models import Input

class fileform(forms.Form):
    Upload_file = forms.FileField(widget=forms.FileInput(attrs={"class": "form-control"}))
    class Meta:
        model=Input
        field =('file')
