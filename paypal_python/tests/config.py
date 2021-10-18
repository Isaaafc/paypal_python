import toml
import os

config = toml.load(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.toml'))
