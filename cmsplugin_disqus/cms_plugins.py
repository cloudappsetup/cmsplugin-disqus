# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class DisqusPlugin(CMSPluginBase):
    render_template = 'cmsplugin_disqus/disqus_plugin.html'
    admin_preview = False
    name = _('Disqus Plugin')
    
    def render(self, context, instance, placeholder):
        context['DISQUS_SHORTNAME'] = settings.DISQUS_SHORTNAME
        context['instance'] = instance
        return context
