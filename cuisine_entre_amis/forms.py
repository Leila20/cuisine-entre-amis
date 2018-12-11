from django import forms

from .models import Contact

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class ContactForm(forms.ModelForm):

  class Meta:
    model = Contact
    fields = ['name', 'mail', 'phone', 'message']

  def __init__(self, *args, **kwargs):
    super(ContactForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper(self)
    self.helper.form_action = 'contact'
    self.helper.form_class = 'form-horizontal'
    self.helper.label_class = 'col-sm-3'
    self.helper.field_class = 'col-sm-9'
    self.helper.html5_required = True
    self.helper.layout = Layout(
      'name',
      'mail',
      'message',
      Submit('submit', 'Envoyer', css_class='pull-right')
    )
