#ifndef base52_H
#define base52_H


#include <unordered_map>
#include "common.hpp"


std::string base52_encode(const std::string& string);
std::string base52_decode(const std::string& string);


#endif // base52_H
