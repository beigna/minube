from django.db import models
from django.utils.translation import ugettext as _

from uuidfield import UUIDField


# Create your models here.


class Group(models.Model):
    id = UUIDField(auto=True, primary_key=True)

    name = models.CharField(verbose_name=_('Name'), max_length=64)

    def __unicode__(self):
        return self.name


class Contact(models.Model):
    id = UUIDField(auto=True, primary_key=True)
    group = models.ManyToManyField('contacts.Group', blank=True)

    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name


class ContactData(models.Model):
    CATEGORY_CHOICES = (
        ('email', _('Email')),
        ('phone', _('Phone')),
        ('address', _('Address')),
    )
    LABEL_CHOICES = (
        ('home', _('Home')),
        ('work', _('Work')),
        ('mobile', _('Mobile')),
    )

    id = UUIDField(auto=True, primary_key=True)
    contact = models.ForeignKey('contacts.Contact')

    category = models.CharField(max_length='16', choices=CATEGORY_CHOICES)
    label = models.CharField(max_length='16', choices=LABEL_CHOICES)
    value = models.TextField()

    def __unicode__(self):
        return u'%s %s: %s' % (self.get_category_display(),
                               self.get_label_display(),
                               self.value)
