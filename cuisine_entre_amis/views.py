from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView

from django.core.urlresolvers import reverse_lazy

from .models import Contact, Post
from .forms import ContactForm


class ContactView(FormView):

  model = Contact
  template_name = 'cuisine_entre_amis/contact.html'
  form_class = ContactForm
  success_url = reverse_lazy('/')

  def form_valid(self, form):
    if form.should_save:
      form.save()

    return super(ContactView, self).form_valid(form)


class PostView(ListView):

  model = Post
  template_name = 'cuisine_entre_amis/post.html'


class PostDetailsView(DetailView):

    model = Post
    template_name = 'cuisine_entre_amis/post_details.html'
