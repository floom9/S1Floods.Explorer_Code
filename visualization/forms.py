# forms.py
from django import forms

class DateSelectorForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))