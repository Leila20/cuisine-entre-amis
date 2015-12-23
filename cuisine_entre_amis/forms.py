from django import forms

from .models import Contact

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class ContactForm(forms.ModelForm):
  lastname = forms.CharField(max_length=100, required=False)

  def clean_lastname(self):
    lastname = self.cleaned_data['lastname']
    if lastname != "":
      self.should_save = False
    else:
      self.should_save = True

    return lastname

  class Meta:
    model = Contact
    fields = ['lastname', 'name', 'mail', 'phone', 'message']

  def __init__(self, *args, **kwargs):
    super(ContactForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper(self)
    self.helper.form_action = 'contact'
    self.helper.form_class = 'form-horizontal'
    self.helper.label_class = 'col-sm-3'
    self.helper.field_class = 'col-sm-9'
    self.helper.html5_required = True
    self.helper.layout = Layout(
      'lastname',
      'name',
      'mail',
      'phone',
      'message',
      Submit('submit', 'Envoyer', css_class='pull-right')
    )
