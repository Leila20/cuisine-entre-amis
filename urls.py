from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


from cuisine_entre_amis.views import ContactView, PostView, PostDetailsView, PostTaggedView

# from cuisine_entre_amis.views import HomeView


urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact/$', ContactView.as_view(template_name='cuisine_entre_amis/contact.html'), name='contact'),
    url(r'^tagged/(?P<slug>[\w-]+)\.html$', PostTaggedView.as_view(), name='tagged_entries'),
    url(r'^$', PostView.as_view(template_name='cuisine_entre_amis/post.html'), name='post'),
    url(r'^Detail/(?P<pk>[0-9]+)/$', PostDetailsView.as_view(template_name='cuisine_entre_amis/post_details.html'), name='post_details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
