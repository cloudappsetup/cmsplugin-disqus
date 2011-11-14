# -*- coding: utf-8 -*-
from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.text import javascript_quote
from django.utils.translation import ugettext_lazy as _


class DisqusPlugin(CMSPlugin):
    title = models.CharField(verbose_name=_('Title'), max_length=50,
        default='', blank=True, help_text=_('Title for your comments, if empty, the page title will be used'))
    
    def __unicode__(self):
        if self.title:
            return self.title
        else:
            return 'Disqus Plugin %s' % self.pk
    
    def javascript_quoted_title(self):
        return mark_safe(u"'%s'" % javascript_quote(self.title))
