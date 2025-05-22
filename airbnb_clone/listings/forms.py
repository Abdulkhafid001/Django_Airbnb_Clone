from django import forms
from .models import Property, PropertyImage
from django.forms import modelformset_factory


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'


class PropertyImageForm(forms.ModelForm):
    class Meta:
        model = PropertyImage
        fields = ['image']


PropertyImageFormSet = modelformset_factory(
    PropertyImage, form=PropertyImageForm, extra=4)
