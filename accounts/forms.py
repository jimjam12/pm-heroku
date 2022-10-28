from django import forms
from django.contrib.auth import get_user_model, authenticate

import calculation

User = get_user_model()

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "placeholder": "Email",
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Password"
    }))

    def clean(self):
        username = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        if not user or not user.is_active:
            raise forms.ValidationError("No entry")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        user = authenticate(username=username, password=password)

        return user


class RegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder": "Email"
    }))

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Password"
    }))

    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Confirm Password"
    }))

    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "First Name"
    }))

    middle_name = forms.CharField(label='Middle Name', widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Middle Name"
    }))

    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Last Name"
    }))

    gender = forms.CharField(label='Gender', widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Gender"
    }))

    nationality = forms.CharField(label='Nationality', widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Nationality"
    }))

    birth_date = forms.DateField(label='Date of Birth', widget=forms.DateInput(attrs={
        "class": "form-control",
        "placeholder": "YYYY-MM-DD"
    }))

    address = forms.CharField(label='Address', widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Address"
    }))

    pay_per_day1 = forms.DecimalField(label='Pay per Day', widget=forms.NumberInput(attrs={
        "class": "form-control",
        "placeholder": "Pay per Day"
    }))

    sick_leave = forms.IntegerField(label='Sick Leave', widget=forms.NumberInput(attrs={
        "class": "form-control",
        "placeholder": "No. of Sick Leave"
    }))

    vacation_leave = forms.IntegerField(label='Vacation Leave', widget=forms.NumberInput(attrs={
        "class": "form-control",
        "placeholder": "No. of Vacation Leave"
    }))

    tax_rate = forms.DecimalField(label='Tax Rate', widget=forms.NumberInput(attrs={
        "class": "form-control",
        "placeholder": "in decimal form"
    }))

    # tax_pay = forms.DecimalField(
    #     widget=calculation.FormulaInput(1 - tax_rate)
    # )

    # total_pay = forms.DecimalField(
    #     widget=calculation.FormulaInput('(payperday1 * total_attendance) - tax_pay')
    # )

    class Meta:
        model = User
        fields = ('email', 'first_name', 'middle_name', 'last_name', 'gender', 'nationality', 'birth_date', 'address', 'hr', 'admin', 'accounting', 'employee', 'pay_per_day1', 'sick_leave', 'vacation_leave', 'tax_rate')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password2 != password1:
            raise forms.ValidationError("Password does not match")
        return password2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()
        return user
