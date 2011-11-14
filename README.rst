#################
CMS Plugin Disqus
#################

`django CMS`_ plugin for `Disqus`_.


************
Installation
************

This plugin requires `django CMS` 2.2 or higher to be properly installed and
configured. It also requires you to have a `Disqus`_ account.

* In your projects `virtualenv`_, run ``pip install cmsplugin-disqus``.
* Add ``'cmsplugin_disqus'`` to your ``INSTALLED_APPS`` setting.
* Set the ``DISQUS_SHORTNAME`` setting to your sites shortname. See the Disqus
  documentation for more details.
* Run ``manage.py migrate cmsplugin_disqus``.


*********
Templates
*********

CMS Plugin Disqus has a single template, located at
``cmsplugin_disqus/disqus_plugin.html``. The template is rendered with the 
following context variables:

* ``DISQUS_SHORTNAME``: The value of the ``DISQUS_SHORTNAME`` setting, used by
  `Disqus`_ to identify your site.
* ``instance``: The plugin instance used to render the template.
* ``developermode``: The value of the ``DEBUG`` setting, can be used to turn on
  the `Disqus`_ developer mode for testing.

The context is inherited from the main context used to render the page,
therefore you also get all context variables from your template context
processors. Most importantly you get the ``request`` object, which you can use
to load the `Disqus`_ embed javascript code over HTTPS if necessary.


************
Translations
************

You can help translate this plugin at 
https://www.transifex.net/projects/p/cmsplugin-disqus/.

.. _django CMS: https://www.django-cms.org
.. _Disqus: http://disqus.com
.. _virtualenv: http://www.virtualenv.org 
