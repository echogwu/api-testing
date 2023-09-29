import pytest
import os
import yaml

CONFIG_DIR = "./env/"

# load the constants defined in ./env/*.yml and find the value for url.base 
@pytest.fixture(scope="session", autouse=True)
def base_url(pytestconfig):
    env = pytestconfig.getoption("env")
    # config_files = [file.split(".")[0] for file in os.listdir(CONFIG_DIR)]
    if env not in ["local", "staging"]:
        raise Exception(
            f"the env config file is not in {CONFIG_DIR}, please specify a string from this list: {config_files}"
        )
    with open(CONFIG_DIR + f"{env}.yml", "r") as ymlfile:
        env_cfg = yaml.full_load(ymlfile)
        base_url = env_cfg["url"]["base"]
    return base_url


# load all the constants defined in ./env/other.yml and set them as environment variables 
@pytest.fixture(scope="session", autouse=True)
def read_env():
    with open(CONFIG_DIR + "other.yml", "r") as ymlfile:
        env_cfg = yaml.full_load(ymlfile)
        for k, v in env_cfg.items():
            os.environ[k] = v