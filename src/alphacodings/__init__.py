"""
base26 ([A-Z]) and base52 ([A-Za-z]) encodings.

.. currentmodule:: alphacodings

.. autosummary::
   :toctree: _generate

   base26_encode
   base26_decode
   base52_encode
   base52_decode
"""

from .base26 import base26_decode, base26_encode
from .base52 import base52_decode, base52_encode


__all__ = ["base26_decode", "base26_encode", "base52_decode", "base52_encode"]
