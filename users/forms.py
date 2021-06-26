from django import forms
from django.contrib.auth.password_validation import validate_password, password_validators_help_text_html
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.contrib.auth import get_user_model

AuthUser = get_user_model()


class RegisterForm(forms.ModelForm):
    class Meta:
        model = AuthUser
        fields = ['first_name', 'last_name', 'email']
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
        required=True,
        help_text=password_validators_help_text_html()
    )
    password_confirmation = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput,
        required=True
    )

    def clean_password(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        user = AuthUser(
            first_name=first_name,
            last_name=last_name,
            email=email,
        )

        validate_password(password, user)

        return password

    def clean_password_confirmation(self):
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')

        if password_confirmation != password:
            raise forms.ValidationError('Password confirmation mismatch.')

        return password_confirmation

    def save(self, commit=True):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        self.instance.username = email
        self.instance.set_password(password)  # set pass in AuthUser model

        return super().save(commit)  # commit method from parent class
