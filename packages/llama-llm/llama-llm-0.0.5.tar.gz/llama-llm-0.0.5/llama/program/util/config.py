import config
import os


def get_config():
    global_config = setup_config()
    return global_config


def setup_config():
    config_set = config.ConfigurationSet(
        config.config_from_env(
            prefix="POWERML", separator="__", lowercase_keys=True),
        home_yaml_config(),
    )
    return config_set


def home_yaml_config():
    home = os.path.expanduser("~")
    home_config_path = os.path.join(home, ".powerml/configure_llama.yaml")
    if os.path.exists(home_config_path):
        yaml_config = config.config_from_yaml(
            home_config_path, read_from_file=True)
    else:
        yaml_config = config.config_from_dict({})
    return yaml_config
