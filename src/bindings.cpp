#include <pybind11/pybind11.h>
#include "base26.hpp"
#include "base52.hpp"


#define stringify(x) #x
#define macrostringify(x) stringify(x)


namespace py = pybind11;


PYBIND11_MODULE(_core, m) {
    m.doc() = R"pbdoc(
        alphacodings
        -----------------------

        base26 ([A-Z]) and base52 ([A-Za-z]) encodings.

        .. currentmodule:: alphacodings

        .. autosummary::
           :toctree: _generate

           base26_encode
           base26_decode
           base52_encode
           base52_decode
    )pbdoc";

    m.def("base26_encode", &base26_encode, "encodes a string to base26", py::arg("string"));
    m.def("base26_decode", &base26_decode, "decodes a base26 string", py::arg("string"));
    m.def("base52_encode", &base52_encode, "encodes a string to base52", py::arg("string"));
    m.def("base52_decode", &base52_decode, "decodes a base52 string", py::arg("string"));

#ifdef __versioninfo__
    m.attr("__version__") = macrostringify(__versioninfo__);
#else
    m.attr("__version__") = "contrib";
#endif
}
