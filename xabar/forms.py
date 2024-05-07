from django import forms
from .models import Xabar
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

class XabarForm(forms.ModelForm):
    class Meta:
        model = Xabar
        fields = ['name', 'email', 'phone_number', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('name', css_class='form-control'),
            Field('email', css_class='form-control'),
            Field('phone_number', css_class='form-control'),
            Field('message', css_class='form-control'),
        )
        
