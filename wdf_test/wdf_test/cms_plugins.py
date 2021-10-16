from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _

from .models import Person

@plugin_pool.register_plugin
class FoundersPlugin(CMSPluginBase):
    model = Person
    render_template = "founders.html"
    cache = False