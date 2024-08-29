#include "base26.hpp"


static const std::string _encoding = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
static const std::unordered_map<char, uint64_t> _decoding = [] {
    std::unordered_map<char, uint64_t> _decoding;

    for (size_t i = 0; i < _encoding.size(); ++i) {
        _decoding[_encoding[i]] = i;
    }

    return _decoding;
}();


std::string base26_encode(const std::string& string) {
    uint64_t number = string_to_base256_int(string);

    if (number == 0) {
        return std::string(1, _encoding[0]);  // empty string or string that equals 0
    }

    std::vector<char> coding;

    while (number > 0) {
        coding.push_back(_encoding[number % 26]);
        number = number / 26;
    }

    return std::string(coding.rbegin(), coding.rend());
}


std::string base26_decode(const std::string& string) {
    uint64_t number = 0;

    for (char character : string) {
        number = number * 26 + _decoding.at(character);
    }

    return base256_int_to_string(number);
}
