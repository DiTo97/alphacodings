#ifndef common_H
#define common_H


#include <cstdint>
#include <string>
#include <vector>


uint64_t string_to_base256_int(const std::string& string);
std::string base256_int_to_string(uint64_t number);


#endif // common_H
