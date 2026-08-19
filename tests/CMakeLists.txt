add_executable(truebearing_tests test_truebearing.cpp)

target_link_libraries(truebearing_tests
    PRIVATE
    truebearing_core
    gtest_main
)

include(GoogleTest)
gtest_discover_tests(truebearing_tests)