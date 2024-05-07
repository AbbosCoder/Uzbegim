from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Row, Column
from .models import Region  # Assuming this is your Region model

class ZiyoratgohSearchForm(forms.Form):
    title = forms.CharField(required=False,label='Ziyoratgoh nomini yozing', max_length=100)
    viloyat = forms.ModelChoiceField(queryset=Region.objects.all(), required=False, label='Viloyatlar', empty_label='Viloyatni tanlang')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'GET'  # Ensure the form uses GET method
        #self.helper.form_class = ''  # This can ensure horizontal layout
        self.helper.layout = Layout(
            Row(
                Column('viloyat', css_class='form-group col-md-6'),  # Half the row
                Column('title', css_class='form-group col-md-4'),  # Slightly smaller than half
                Column(Submit('submit', 'Search', css_class='btn btn-primary'), css_class='form-group col-md-2'),  # Smaller column for the submit button
                css_class='g-3'  # Optional: Adds spacing between columns
            )
        )
