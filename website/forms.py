from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "input", 'placeholder': "First name"}),
        max_length=50
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "input", 'placeholder': "Last name"}),
        max_length=50
    )
    email_address = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': "input", 'placeholder': "Email address"}),
        max_length=150
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': "textarea"}),
        max_length=2000
    )


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user