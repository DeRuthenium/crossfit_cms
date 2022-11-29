from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from easy_thumbnails.files import get_thumbnailer

from plugins.model import NadpisSFonomPluginSetting


@plugin_pool.register_plugin
class NadpisSFonomPlugin(CMSPluginBase):

    render_template = "plugins/nadpis_s_fonom.html"
    module = '00. Оформление'
    name = 'Надпись с фоном'
    cache = False
    model = NadpisSFonomPluginSetting
    allow_children = True


    def render(self, context, instance, placeholder):
        options = {'size': (1000, instance.visota), 'crop': False}
        fon = get_thumbnailer(instance.fon).get_thumbnail(options).url
        context.update({'instance': instance, 'fon': fon})
        return context

@plugin_pool.register_plugin
class KartaPlugin(CMSPluginBase):

    render_template = "plugins/karta.html"
    module = '00. Оформление'
    name = 'Карта '
    cache = False
    # model = NadpisSFonomPluginSetting
    allow_children = False


    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

@plugin_pool.register_plugin
class Karta1Plugin(CMSPluginBase):

    render_template = "plugins/karta_arkfit_small.html"
    module = '00. Оформление'
    name = 'Карта аркфит маленькая '
    cache = False
    # model = NadpisSFonomPluginSetting
    allow_children = False

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

@plugin_pool.register_plugin
class Karta2Plugin(CMSPluginBase):

    render_template = "plugins/karta_boston_small.html"
    module = '00. Оформление'
    name = 'Карта бостон маленькая '
    cache = False
    # model = NadpisSFonomPluginSetting
    allow_children = False

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context


@plugin_pool.register_plugin
class PlaylistPlugin(CMSPluginBase):

    render_template = "plugins/playlist.html"
    module = '00. Оформление'
    name = 'Плейлист'
    cache = False
    # model = NadpisSFonomPluginSetting
    allow_children = False

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

@plugin_pool.register_plugin
class Playlist1Plugin(CMSPluginBase):

    render_template = "plugins/playlist1.html"
    module = '00. Оформление'
    name = 'Плейлист1'
    cache = False
    # model = NadpisSFonomPluginSetting
    allow_children = False

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

@plugin_pool.register_plugin
class Playlist2Plugin(CMSPluginBase):

    render_template = "plugins/playlist2.html"
    module = '00. Оформление'
    name = 'Плейлист2'
    cache = False
    # model = NadpisSFonomPluginSetting
    allow_children = False

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

@plugin_pool.register_plugin
class Playlist3Plugin(CMSPluginBase):

    render_template = "plugins/playlist3.html"
    module = '00. Оформление'
    name = 'Плейлист3'
    cache = False
    # model = NadpisSFonomPluginSetting
    allow_children = False

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context
