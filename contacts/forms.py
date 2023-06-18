from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelMultipleChoiceField, CheckboxSelectMultiple, BaseInlineFormSet

from .models import *


class AddContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["gender"].empty_label = "None"

    class Meta:
        model = Contact
        fields = ["first_name", "last_name", "birthdate", "gender", "address", "photo", ]
        labels = {
            'first_name': 'First name*',
            'last_name': 'Last name*',
            'gender': 'Gender*',
            }
        widgets = {
            "address": forms.Textarea(
                attrs={"cols": 30, "rows": 5},
            ),
            "birthdate": forms.DateInput(attrs={'placeholder': 'YYYY-mm-dd'})
        }

class AddPhoneForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["phone"].required = False
        self.fields["field_type"].required = False
        self.fields["field_type"].empty_label = "None"

    class Meta:
        model = PhoneNumber
        fields = ["phone", "field_type",]
        widgets = {"phone": forms.TextInput(attrs={'placeholder': 'only digits here'})
        }


class AddEmailForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].required = False
        self.fields["field_type"].required = False
        self.fields["field_type"].empty_label = "None"

    class Meta:
        model = Email
        fields = ["email", "field_type"]


class ContactImportForm(forms.Form):
        csv_file = forms.FileField(label='CSV file')

        class Meta:
            fields = ['csv_file',]


class EmailFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.forms:
            form.fields.pop('contact')


class PhoneFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.forms:
            form.fields.pop('contact')