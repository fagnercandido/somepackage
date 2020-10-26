from .version import __version__
from .server import server

# if somebody does "from calls import *", this is what they will
# be able to access:
__all__ = [
    'server'
]
