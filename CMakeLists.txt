cmake_minimum_required(VERSION 3.10)

project(truebearing)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# - - - Eigen - - -
include(FetchContent)

set(BUILD_TESTING OFF CACHE BOOL "" FORCE)
set(EIGEN_BUILD_DOC OFF CACHE BOOL "" FORCE)

FetchContent_Declare(
  Eigen
  GIT_REPOSITORY https://gitlab.com/libeigen/eigen.git
  GIT_TAG        3.4.0
)

FetchContent_MakeAvailable(Eigen)

# - - - Core library - - -
add_library(truebearing_core src/truebearing.cpp)

target_include_directories(truebearing_core PUBLIC include)
target_link_libraries(truebearing_core PUBLIC Eigen3::Eigen)

# - - - Simulation executable - - -
add_executable(truebearing_sim src/main.cpp)
target_link_libraries(truebearing_sim PRIVATE truebearing_core)

# - - - GoogleTest - - -
FetchContent_Declare(
  googletest
  GIT_REPOSITORY https://github.com/google/googletest.git
  GIT_TAG        v1.18.0
)
FetchContent_MakeAvailable(googletest)

set(BUILD_TESTING ON CACHE BOOL "" FORCE)

enable_testing()
add_subdirectory(tests)