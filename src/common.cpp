#include "common.h"


uint64_t string_to_base256_int(const std::string& string) {
    uint64_t number = 0;
    
    for (char character : string) {
        number = (number << 8) + static_cast<uint64_t>(character);
    }
    
    return number;
}


std::string base256_int_to_string(uint64_t number) {
    std::vector<char> coding;

    while (number > 0) {
        coding.push_back(static_cast<char>(number & 0xFF));
        number = number >> 8;
    }

    return std::string(coding.rbegin(), coding.rend());
}
