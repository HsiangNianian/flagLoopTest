import OlivOS
import flagLoopTest

class Event(object):
    def init(plugin_event, Proc):
        pass

    def private_message(plugin_event, Proc):
        pass

    def group_message(plugin_event, Proc):
        pass

    def poke(plugin_event, Proc):
        pass

    def save(plugin_event, Proc):
        pass

    def menu(plugin_event, Proc):
        if plugin_event.data.namespace == 'OlivOSPluginTemplate':
            if plugin_event.data.event == 'OlivOSPluginTemplate_Menu_001':
                pass
            elif plugin_event.data.event == 'OlivOSPluginTemplate_Menu_002':
                pass
            