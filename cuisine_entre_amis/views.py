from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView

from django.core.urlresolvers import reverse_lazy

from taggit.models import Tag

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


class PostTaggedView(PostView):

    def get_queryset(self):
        slug = self.kwargs.get('slug', '')
        queryset = super(PostTaggedView, self).get_queryset()
        return queryset.filter(tags__slug__iexact=slug)

    def get_contect_data(self, **kwargs):
        context = super(PostTaggedView, self).get_contect_data(**kwargs)
        slug = self.kwargs.get('slug', '')
        tag = Tag.object.filter(slug__iexact=slug)
        if len(tag):
            context['cur_tag']=tag[0]
        return context
