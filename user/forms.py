from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import  UserCreationForm
from .models import Profile
from PIL import Image

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)   

    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2'] 


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)   

    class Meta:
        model = User
        fields = ['username', 'email'] 


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
    
    def save(self):
        super().save()
        
        img = Image.open(self.image.path)
        if img.height > 300 or img.width >300:
            output_size =(250,250)
            img.thumbnail(output_size)
            img.save(self.image.path)