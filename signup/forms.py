from django import forms

class RegisterForm(form.Form):
    first_name = form.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = form.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = form.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = form.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password_repeat = form.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
