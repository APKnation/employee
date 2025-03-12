from django import forms
from .models import Employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"
        widgets={
            'fullname':forms.TextInput(attrs={'class':'form-control'}),
            'mobile':forms.TextInput(attrs={'class':'form-control'}),
            'emp_code':forms.TextInput(attrs={'class':'form-control'}),
            'position':forms.Select(attrs={'class':'form-control'}),
        }
        def __init__(self,*args,**kwargs):
            super(EmployeeForm,self).__init__(*args,**kwargs)
            self.fields['position'].empty_label="Select"
            self.fields['emp_code'].required=False