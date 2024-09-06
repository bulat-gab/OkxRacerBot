from .logger import logger
from . import launcher
from .proxy_utils_v1 import create_tg_client_proxy_pairs

import os

if not os.path.exists(path="sessions"):
    os.mkdir(path="sessions")
