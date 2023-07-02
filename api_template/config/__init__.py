from .dev_config import DevConfig
from .prod_config import ProdConfig
import dotenv
import os

env_config = {
    "dev": DevConfig,
    "prod": ProdConfig
}

def import_env_name():
    dotenv.load_dotenv(".env")
    return os.getenv("ENV")


env_name = import_env_name()
app_config = env_config.get(env_name)

if not app_config:
    raise ValueError(f"Invalid environment name: {env_name}")