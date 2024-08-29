cmake_minimum_required(VERSION 3.15...3.27)

project(${SKBUILD_PROJECT_NAME} VERSION ${SKBUILD_PROJECT_VERSION} LANGUAGES CXX)

find_package(Python REQUIRED COMPONENTS Interpreter Development.Module)
find_package(pybind11 CONFIG REQUIRED)

include_directories(include)

add_library(module src/base26.cpp src/base52.cpp src/common.cpp)

pybind11_add_module(_core src/bindings.cpp)

target_link_libraries(_core PRIVATE module)
target_compile_definitions(_core PRIVATE __versioninfo__=${PROJECT_VERSION})

install(TARGETS _core DESTINATION ${SKBUILD_PROJECT_NAME})
