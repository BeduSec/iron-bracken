import yaml

_config_cache = {}

def load_config(path):
    with open(path, 'r') as f:
        config = yaml.safe_load(f)
    _config_cache.update(config)
    return config

def get_setting(key, default=None):
    return _config_cache.get(key, default)