#include <pybind11/pybind11.h>
#include <cstdint>
#include <string>
#include <unordered_map>
#include <vector>


#define stringify(x) #x
#define macrostringify(x) stringify(x)


namespace py = pybind11;


static const std::string _encoding_base26 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
static const std::unordered_map<char, uint64_t> _decoding_base26 = [] {
    std::unordered_map<char, uint64_t> _decoding;

    for (size_t i = 0; i < _encoding_base26.size(); ++i) {
        _decoding[_encoding_base26[i]] = i;
    }

    return _decoding;
}();


static const std::string _encoding_base52 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
static const std::unordered_map<char, uint64_t> _decoding_base52 = [] {
    std::unordered_map<char, uint64_t> _decoding;

    for (size_t i = 0; i < _encoding_base52.size(); ++i) {
        _decoding[_encoding_base52[i]] = i;
    }

    return _decoding;
}();


static uint64_t string_to_int(const std::string& string) {
    uint64_t number = 0;
    
    for (char character : string) {
        number = (number << 8) + static_cast<uint64_t>(character);
    }
    
    return number;
}


static std::string int_to_string(uint64_t number) {
    std::vector<char> coding;

    while (number > 0) {
        coding.push_back(static_cast<char>(number & 0xFF));
        number = number >> 8;
    }

    return std::string(coding.rbegin(), coding.rend());
}


std::string base26_encode(const std::string& string) {
    uint64_t number = string_to_int(string);

    if (number == 0) {
        return std::string(1, _encoding_base26[0]);  // empty string or string that equals 0
    }

    std::vector<char> coding;

    while (number > 0) {
        coding.push_back(_encoding_base26[number % 26]);
        number = number / 26;
    }

    return std::string(coding.rbegin(), coding.rend());
}


std::string base26_decode(const std::string& string) {
    uint64_t number = 0;

    for (char character : string) {
        number = number * 26 + _decoding_base26.at(character);
    }

    return int_to_string(number);
}


std::string base52_encode(const std::string& string) {
    uint64_t number = string_to_int(string);

    if (number == 0) {
        return std::string(1, _encoding_base52[0]);  // empty string or string that equals 0
    }

    std::vector<char> coding;

    while (number > 0) {
        coding.push_back(_encoding_base52[number % 52]);
        number = number / 52;
    }

    return std::string(coding.rbegin(), coding.rend());
}


std::string base52_decode(const std::string& string) {
    uint64_t number = 0;

    for (char character : string) {
        number = number * 52 + _decoding_base52.at(character);
    }

    return int_to_string(number);
}


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
    m.def("base52_encode", &base52_encode, "encodes a string to base52" py::arg("string"));
    m.def("base52_decode", &base52_decode, "decodes a base52 string" py::arg("string"));

#ifdef __versioninfo__
    m.attr("__version__") = macrostringify(__versioninfo__);
#else
    m.attr("__version__") = "contrib";
#endif
}
