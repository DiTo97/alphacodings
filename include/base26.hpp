#ifndef base26_H
#define base26_H


#include <unordered_map>
#include "common.hpp"


std::string base26_encode(const std::string& string);
std::string base26_decode(const std::string& string);


#endif // base26_H
