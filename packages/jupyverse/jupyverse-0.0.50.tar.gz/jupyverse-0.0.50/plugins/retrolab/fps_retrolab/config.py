from fps.config import PluginModel, get_config  # type: ignore
from fps.hooks import register_config  # type: ignore


class RetroLabConfig(PluginModel):
    pass


def get_rlab_config():
    return get_config(RetroLabConfig)


c = register_config(RetroLabConfig)
