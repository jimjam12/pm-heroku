from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class ContactForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(
      attrs={
          "class": "form-control",
          "placeholder": "Fullname"
      }
    ))

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            "class": "form-control",
            "placeholder": "Email"
        }
    ))

    content = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Message"
        }
    ))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail.com")
        return email

class RequestForm(forms.Form):
    emp_email = forms.EmailField()
    emp_name = forms.CharField(max_length=100)
    emp_leaveDateStart = forms.DateField()
    emp_leaveDateEnd = forms.DateField()
    typeOf_leave = forms.Select()
    reasonFor_leave = forms.CharField(max_length=100)
