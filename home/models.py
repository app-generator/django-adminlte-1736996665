# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Experience(models.Model):

    #__Experience_FIELDS__
    company = models.TextField(max_length=255, null=True, blank=True)
    role = models.TextField(max_length=255, null=True, blank=True)
    start_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    end_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    skillsets = models.TextField(max_length=255, null=True, blank=True)

    #__Experience_FIELDS__END

    class Meta:
        verbose_name        = _("Experience")
        verbose_name_plural = _("Experience")


class Lookups(models.Model):

    #__Lookups_FIELDS__
    technology_category = models.TextField(max_length=255, null=True, blank=True)
    skillsets = models.TextField(max_length=255, null=True, blank=True)
    vendors = models.TextField(max_length=255, null=True, blank=True)
    experience = models.TextField(max_length=255, null=True, blank=True)

    #__Lookups_FIELDS__END

    class Meta:
        verbose_name        = _("Lookups")
        verbose_name_plural = _("Lookups")


class Technology(models.Model):

    #__Technology_FIELDS__
    vendor = models.ForeignKey(LOOKUPS, on_delete=models.CASCADE)
    technology_category = models.ForeignKey(LOOKUPS, on_delete=models.CASCADE)
    name = models.TextField(max_length=255, null=True, blank=True)
    experience = models.TextField(max_length=255, null=True, blank=True)

    #__Technology_FIELDS__END

    class Meta:
        verbose_name        = _("Technology")
        verbose_name_plural = _("Technology")



#__MODELS__END
