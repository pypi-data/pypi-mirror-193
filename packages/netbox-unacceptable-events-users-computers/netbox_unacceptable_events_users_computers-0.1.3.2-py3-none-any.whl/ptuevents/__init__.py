from extras.plugins import PluginConfig


class NetBoxPTUEventsConfig(PluginConfig):
    name = 'ptueventsuserscomputers'
    verbose_name = 'Unacceptable events and users and computers'
    description = 'Add events related fields to devices and virtual machines, adds application systems'
    version = '0.1.3.0002'
    base_url = 'ptueventsuserscomputers'
    author = 'Artur Shamsiev'
    author_email = 'me@z-lab.me'


config = NetBoxPTUEventsConfig
