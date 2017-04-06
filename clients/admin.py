# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Client

@admin.register(Client)
class AdminClient(admin.ModelAdmin):
	list_display = ('name', 'phone', 'email', 'adress')
	list_filter = ('name',)
