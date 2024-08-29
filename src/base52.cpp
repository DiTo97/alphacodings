#include "base52.hpp"


static const std::string _encoding = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
static const std::unordered_map<char, uint64_t> _decoding = [] {
    std::unordered_map<char, uint64_t> _decoding;

    for (size_t i = 0; i < _encoding.size(); ++i) {
        _decoding[_encoding[i]] = i;
    }

    return _decoding;
}();


std::string base52_encode(const std::string& string) {
    uint64_t number = string_to_base256_int(string);

    if (number == 0) {
        return std::string(1, _encoding[0]);  // empty string or string that equals 0
    }

    std::vector<char> coding;

    while (number > 0) {
        coding.push_back(_encoding[number % 52]);
        number = number / 52;
    }

    return std::string(coding.rbegin(), coding.rend());
}


std::string base52_decode(const std::string& string) {
    uint64_t number = 0;

    for (char character : string) {
        number = number * 52 + _decoding.at(character);
    }

    return base256_int_to_string(number);
}
