from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile



class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your username', 'class': 'w-full py-4 px-6 rounded-xl'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Your email address', 'class': 'w-full py-4 px-6 rounded-xl'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Your password', 'class': 'w-full py-4 px-6 rounded-xl'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Repeat password', 'class': 'w-full py-4 px-6 rounded-xl'}))



class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your username', 'class': 'w-full py-4 px-6 rounded-xl'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Your password', 'class': 'w-full py-4 px-6 rounded-xl'}))
    
    
    
class ProfileForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your name', 'class': 'w-full py-4 px-6 rounded-xl'}))
    profile_img = forms.ImageField(label="Profile Picture")
    profile_bio = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Bio', 'class': 'w-full py-4 px-6 rounded-xl'}))
    facebook_link = forms.URLField(widget=forms.TextInput(attrs={'placeholder': 'facebook', 'class': 'w-full py-4 px-6 rounded-xl'}))
    instagram_link = forms.URLField(widget=forms.TextInput(attrs={'placeholder': 'instagram', 'class': 'w-full py-4 px-6 rounded-xl'}))
    twitter_link = forms.URLField(widget=forms.TextInput(attrs={'placeholder': 'twitter', 'class': 'w-full py-4 px-6 rounded-xl'}))

	
    class Meta:
        model = Profile
        fields = ('profile_img', 'name',  'profile_bio', 'facebook_link', 'instagram_link', 'twitter_link',)