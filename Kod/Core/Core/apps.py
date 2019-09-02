import pkg_resources
from django.apps import AppConfig


class CoreConfig(AppConfig):

    name = 'Core'
    data_plugins = []
    visualization_plugins = []
    graph = None

    def ready(self):
        self.data_plugins = load_plugins("data_maker.load")
        self.visualization_plugins = load_plugins("data_visualization.load")


def load_plugins(identifier):
    plugins = []
    for ep in pkg_resources.iter_entry_points(group=identifier):
        p = ep.load()
        plugins.append(p())
    return plugins
