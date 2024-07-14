cmake_minimum_required(VERSION 3.28)
project(day02 C)

set(CMAKE_C_STANDARD 23)

add_executable(day02 main.c)


# Treat warnings as errors + expanded errors/warnings
set (CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall -Wextra -Werror -Wpedantic")