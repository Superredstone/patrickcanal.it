from django import forms
from django.utils.translation import gettext as _


class TablerEmailInput(forms.EmailInput):
    def __init__(self, *args, **kwargs):
        attrs = kwargs.setdefault("attrs", {})
        attrs.update(
            {
                "class": "form-control",
                "placeholder": "example@mail.com",
                "autocomplete": "off",
                "minlength": "4",
            }
        )
        super().__init__(*args, **kwargs)


class TablerTextInput(forms.TextInput):
    def __init__(self, placeholder=None, *args, **kwargs):
        attrs = kwargs.setdefault("attrs", {})
        attrs.update(
            {
                "class": "form-control",
                "placeholder": placeholder,
                "autocomplete": "off",
                "minlength": "4",
            }
        )
        super().__init__(*args, **kwargs)


class TablerTextArea(forms.Textarea):
    def __init__(self, placeholder=None, *args, **kwargs):
        attrs = kwargs.setdefault("attrs", {})
        attrs.update(
            {
                "class": "form-control",
                "placeholder": placeholder,
                "autocomplete": "off",
                "minlength": "4",
            }
        )
        super().__init__(*args, **kwargs)


class ContactForm(forms.Form):
    email = forms.EmailField(max_length=50, min_length=4, widget=TablerEmailInput())
    subject = forms.CharField(
        max_length=200,
        min_length=4,
        widget=TablerTextInput(placeholder=_("Your message")),
    )
    message = forms.CharField(max_length=5000, min_length=10, widget=TablerTextArea())
