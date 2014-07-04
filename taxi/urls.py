#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from taxi.views import PlanningView
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
    # Examples:
   url(r'^planning/$', PlanningView.as_view(), name='planning'), 
    
) 

