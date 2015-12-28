from django.db import models
from django.utils.translation import ugettext as _

from django.db.models.signals import post_save
from django.dispatch import receiver


class Contact(models.Model):
  name = models.CharField(_('Name'), max_length=100)
  mail = models.EmailField(_('E-mail'), max_length=100)
  phone = models.CharField(_('Phone'), max_length=100)
  message = models.TextField(_('Message'))
  created_at = models.DateTimeField(auto_now_add=True)

  @property
  def short(self):
    if len(self.message) > 30:
      return '{}...'.format(self.message[:27])
    return self.message


@receiver(post_save, sender=Contact)
def contact_send_mail(sender, instance, **kwargs):
  from .tasks import send_contact_mail
  send_contact_mail.delay(instance.pk)
