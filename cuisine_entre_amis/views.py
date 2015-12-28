
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateResponseMixin

from django.core.urlresolvers import reverse_lazy

from .forms import ContactForm


class AjaxResponseMixin(TemplateResponseMixin):

  html_template_name = None
  ajax_template_name = None


class AbstractContactView(object):

  def get_context_data(self, **kwargs):
    context = super(AbstractContactView, self).get_context_data(**kwargs)
    return context


class ContactView(AbstractContactView, FormView, AjaxResponseMixin):
  html_template_name = 'jean_yves/contact.html'
  ajax_template_name = "jean_yves/ajax-contact.html"
  form_class = ContactForm
  success_url = reverse_lazy('thanks')

  def form_valid(self, form):
    if form.should_save:
      form.save()

    return super(ContactView, self).form_valid(form)
