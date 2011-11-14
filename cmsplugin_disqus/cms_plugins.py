# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cmsplugin_disqus import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class DisqusPlugin(CMSPluginBase):
    render_template = 'cmsplugin_disqus/disqus_plugin.html'
    admin_preview = False
    name = _('Disqus Plugin')
    model = models.DisqusPlugin
    
    def render(self, context, instance, placeholder):
        context['DISQUS_SHORTNAME'] = settings.DISQUS_SHORTNAME
        context['instance'] = instance
        context['developer_mode'] = settings.DEBUG
        return context
plugin_pool.register_plugin(DisqusPlugin)
