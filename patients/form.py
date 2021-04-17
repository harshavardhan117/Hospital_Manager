from django import forms 
from patients.models import TaskList
from django.core import validators

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = ['name','disease','firstappointment','phone_number']
        widgets = {
             'name':forms.TextInput(attrs={'class':'form-control'}),
             'disease':forms.TextInput(attrs={'class':'form-control'}),
              'firstappointment':forms.DateInput(attrs={'class':'form-control'}),
                
                'phone_number':forms.NumberInput(attrs={'class':'form-control'}),
                
  }