from django import forms

class DataForm(forms.Form):
    content = forms.CharField(label="Your data", max_length=255)
