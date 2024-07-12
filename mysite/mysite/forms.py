# myapp/forms.py

from django import forms
from .models import Person, House

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email', 'number', 'woonplaats', 'age', 'school', 'school_year', 'house']

class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['address', 'city', 'postal_code']
