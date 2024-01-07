from django import forms
from django.contrib.auth.hashers import make_password
from .models import CustomUser, Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'name',
            'surname',
            'avatar',
            'phone',
        )
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['surname'].required = False
        self.fields['phone'].required = False
        self.fields['avatar'].required = False

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if phone:
            if phone[:4] != '+380' and len(phone) != 13:
                self.add_error('phone', 'Enter correct phone')
                raise forms.ValidationError('Enter phone in format +380XXXXXXXXX')
        return phone

class UserForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)


    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'password2')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password != password2:
            self.add_error('password2', "Passwords do not match.")
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data


