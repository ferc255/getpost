# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class SiteRequest(models.Model):
    url = models.TextField()
    status = models.IntegerField()
    internal = models.TextField()
    external = models.TextField()
