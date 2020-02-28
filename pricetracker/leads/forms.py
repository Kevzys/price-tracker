from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200)

class CreateNewItem(forms.Form):
    url = forms.CharField(max_length=100)
    name = forms.CharField(max_length=50)
    update = forms.CheckboxInput()