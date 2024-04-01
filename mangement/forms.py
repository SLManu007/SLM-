from django import forms
from students.models import studentmodels

class studentmodelsform(forms.ModelForm):
    class Meta:
        model=studentmodels
        fields = '__all__'