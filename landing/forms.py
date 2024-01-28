from django_recaptcha.fields import ReCaptchaField
from django import forms


class CaptchaForm(forms.Form):
    captcha = ReCaptchaField()
