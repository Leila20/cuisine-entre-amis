from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView


from cuisine_entre_amis.views import ContactView, PostView

# from cuisine_entre_amis.views import HomeView


urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', TemplateView.as_view(template_name='base.html'), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact/$', ContactView.as_view(template_name='cuisine_entre_amis/contact.html'), name='contact'),
    url(r'^post/$', PostView.as_view(template_name='cuisine_entre_amis/post.html'), name='post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
