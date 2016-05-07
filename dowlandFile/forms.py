from django import forms

class NameForm(forms.Form):
    your_file = forms.CharField(label="your_file",max_length=100)