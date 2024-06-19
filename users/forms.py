from django import forms
from .models import User



class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Username"}))
    password = forms.CharField(widget=forms.PasswordInput({"class": "form-control", "placeholder": "Password"}))


class RegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Name"}))
    phone_number = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Phone Number"}))
    first_name = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "First Name"}))
    last_name = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Last Name"}))

    password = forms.CharField(widget=forms.PasswordInput({"class": "form-control", "placeholder": "Password"}))
    confirm_password = forms.CharField(widget=forms.PasswordInput({"class": "form-control", "placeholder": "Confirm Password"}))

    class Meta:
        model = User
        fields = ('username', 'phone_number', 'first_name', 'last_name', 'password', 'confirm_password')

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return password
    
class ProfileForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Name"}))
    phone_number = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Phone Number"}))
    first_name = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "First Name"}))
    last_name = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Last Name"}))
    jobs = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Jobs"}))
    address = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "address"}))
    email = forms.CharField(widget=forms.EmailInput({"class": "form-control", "placeholder": "address"}))
    image = forms.ImageField(widget=forms.FileInput({"class": "form-control", "placeholder": "image"}))
    
    class Meta:
        model = User
        fields = ('username', 'phone_number','address', 'first_name', 'last_name','image','email','jobs')


class UsersEditForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Name"}))
    phone_number = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Phone Number"}))
    first_name = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "First Name"}))
    last_name = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Last Name"}))
    jobs = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Jobs"}))
    address = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "address"}))
    email = forms.CharField(widget=forms.EmailInput({"class": "form-control", "placeholder": "address"}))
    image = forms.ImageField(widget=forms.FileInput({"class": "form-control", "placeholder": "image"}))

    class Meta:
        model = User
        fields = ('username', 'phone_number','address', 'first_name', 'last_name','image','email','jobs', 'user_role')