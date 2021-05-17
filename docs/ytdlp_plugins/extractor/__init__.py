# flake8: noqa
import os
import sys

# Import extractors plugins if using Bundle App
if hasattr(sys, "frozen"):
    # for load_module extractor (plugins)
    HERE = os.path.realpath(os.path.abspath(__file__))
    sys.path.insert(0, os.path.dirname(HERE))

# ⚠ Dont use relative import beyond top-level package
from picta import PictaIE, PictaChannelPlaylistIE, PictaUserPlaylistIE  # type: ignore
