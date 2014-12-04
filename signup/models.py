from django.db import models
from django.utils.encoding import smart_unicode
# Tells django what data to store.
# Create your models here.

class SignUp(models.Model):
    first_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField(null=False, blank=False)
    timestamp = models.DateField(auto_now_add=True, auto_now=False)
    updated = models.DateField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.email)