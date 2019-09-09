from config import app
from config.clv_base import SlaveHandler


__all__ = ["slave"]


slave = SlaveHandler(app)
