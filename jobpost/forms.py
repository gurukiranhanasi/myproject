from django import forms
from jobpost.models import submit,addpost,comment,subscribe

class submitform(forms.ModelForm):
    class Meta:
        model=submit
        fields="__all__"
    
class addposts(forms.ModelForm):
    class Meta:
        model=addpost
        fields="__all__"

class commentform(forms.ModelForm):
    class Meta:
        model = comment
        fields= ['Content','Name','Email']

class sub(forms.ModelForm):
    class Meta:
        model=subscribe
        fields="__all__"