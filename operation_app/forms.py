# your_app/forms.py
from django import forms
from .models import Profile,Complaint

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','mobile','email','password','profile_type_id','designation_id','created_at','updated_at']

        # Add or remove fields based on your model's structure
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
#comment out later if not needed 
        
class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['profile_id', 'subject', 'current_handler', 'created_at', 'updated_at', 'priority_id']

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = '__all__'