cmake_minimum_required(VERSION 3.10)
project(orgChartUnitTests)

set(CMAKE_CXX_STANDARD 17)

# Adjust include paths
include_directories(orgChartApi tests)

# Match source files
file(GLOB_RECURSE SRC_SOURCES "orgChartApi/*.cc" "orgChartApi/*.cpp")
file(GLOB_RECURSE TEST_SOURCES "tests/*.cpp")

# Debug: show how many files matched
message(STATUS "Found source files: ${SRC_SOURCES}")
message(STATUS "Found test files: ${TEST_SOURCES}")

# Only add executable if tests are found
if(TEST_SOURCES)
  add_executable(runTests ${SRC_SOURCES} ${TEST_SOURCES})
  target_link_libraries(runTests gtest gtest_main pthread)
else()
  message(FATAL_ERROR "❌ No test files found in tests/ folder.")
endif()

