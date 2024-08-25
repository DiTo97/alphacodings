#include <pybind11/pybind11.h>
#include <string>

#define stringify(x) #x
#define macrostringify(x) stringify(x)


namespace py = pybind11;


std::string base26_encode(const std::string& str) {
    unsigned int base256_int = 0;

    for (char character : str) {
        base256_int = base256_int * 256 + static_cast<unsigned int>(character);
    }

    if (base256_int == 0) {
        return "A";  // empty input or input that equals 0
    }

    std::string base26_str;

    while (base256_int > 0) {
        base26_str = static_cast<char>((base256_int % 26) + 65) + base26_str;
        base256_int /= 26;
    }

    return base26_str;
}


std::string base26_decode(const std::string& str) {
    unsigned int base26_int = 0;

    for (char character : str) {
        base26_int = base26_int * 26 + (static_cast<unsigned int>(character) - 65);
    }

    std::string bytestring;

    while (base26_int > 0) {
        bytestring.insert(bytestring.begin(), static_cast<char>(base26_int % 256));
        base26_int /= 256;
    }

    return bytestring;
}


std::string base52_encode(const std::string& str) {
    unsigned int base256_int = 0;

    for (char character : str) {
        base256_int = base256_int * 256 + static_cast<unsigned int>(character);
    }

    if (base256_int == 0) {
        return "a";  // empty input or input that equals 0
    }

    std::string base52_str;

    while (base256_int > 0) {
        unsigned int remainder = base256_int % 52;

        if (remainder < 26) {
            base52_str = static_cast<char>(remainder + 65) + base52_str;  // uppercase
        } else {
            base52_str = static_cast<char>(remainder - 26 + 97) + base52_str;  // lowercase
        }

        base256_int /= 52;
    }

    return base52_str;
}


std::string base52_decode(const std::string& str) {
    unsigned int base52_int = 0;

    for (char character : str) {
        if ('A' <= character && character <= 'Z') {
            base52_int = base52_int * 52 + (static_cast<unsigned int>(character) - 65);  // uppercase
        } else {
            base52_int = base52_int * 52 + (static_cast<unsigned int>(character) - 97 + 26);  // lowercase
        }
    }

    std::string bytestring;

    while (base52_int > 0) {
        bytestring.insert(bytestring.begin(), static_cast<char>(base52_int % 256));
        base52_int /= 256;
    }

    return bytestring;
}


PYBIND11_MODULE(_core, M) {
    M.doc() = R"pbdoc(
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

    M.def("base26_encode", &base26_encode, "encodes a string to base26");
    M.def("base26_decode", &base26_decode, "decodes a base26 string");
    M.def("base52_encode", &base52_encode, "encodes a string to base52");
    M.def("base52_decode", &base52_decode, "decodes a base52 string");

#ifdef __versioninfo__
    m.attr("__version__") = macrostringify(__versioninfo__);
#else
    m.attr("__version__") = "contrib";
#endif
}
