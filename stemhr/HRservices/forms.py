from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Application, ContactMessage
from HRservices import models


# 🔥 Shared styling (clean reuse)
FORM_INPUT_CLASS = 'w-full mt-2 bg-black/30 text-white p-3 rounded-lg border border-white/10 focus:border-purple-500 focus:ring-1 focus:ring-purple-500 outline-none'


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.required = True
            field.widget.attrs.update({'class': FORM_INPUT_CLASS})


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({'class': FORM_INPUT_CLASS})


class ServiceForm(forms.ModelForm):
    class Meta:
        model = models.Service
        fields = '__all__'


# 🔥 THIS is what fixes login styling
class StyledLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({'class': FORM_INPUT_CLASS})