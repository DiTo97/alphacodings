from . import _core
from . import _native


base26_encode = _native.base26_encode
base26_decode = _native.base26_decode
base52_encode = _native.base52_encode
base52_decode = _native.base52_decode


base26_encode.__doc__ = _core.base26_encode.__doc__
base26_decode.__doc__ = _core.base26_decode.__doc__
base52_encode.__doc__ = _core.base52_encode.__doc__
base52_decode.__doc__ = _core.base52_decode.__doc__


__doc__ = _core.__doc__
__version__ = _core.__version__


__all__ = [
    "__doc__",
    "__version__",
    "base26_encode",
    "base26_decode",
    "base52_encode",
    "base52_decode",
]
