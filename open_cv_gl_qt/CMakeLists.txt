cmake_minimum_required(VERSION 3.10.0)
project(open_gl_qt VERSION 0.1.0 LANGUAGES C CXX)

include(CTest)
enable_testing()

find_package(fmt CONFIG REQUIRED)
find_package(FreeGLUT CONFIG REQUIRED)
find_package(GTest CONFIG REQUIRED)

# vcpkg include and custom include
# 从环境变量中获取
set(VCPKG_ROOT $ENV{VCPKG_ROOT})
message("VCPKG_ROOT: ${VCPKG_ROOT}")
# include_directories(${VCPKG_ROOT}/include)

set(SRC_DIR ${CMAKE_CURRENT_SOURCE_DIR}/src)
set(INCLUDE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/include)
set(TEST_DIR ${CMAKE_CURRENT_SOURCE_DIR}/tests)


# 自动搜集源文件
file(GLOB MAIN_SOURCES
    "${SRC_DIR}/*.cpp"
)
file(GLOB TEST_SOURCES
    "${TEST_DIR}/*.cpp"
)

# main
add_executable(main ${MAIN_SOURCES})
target_include_directories(main PRIVATE ${INCLUDE_DIR})

target_link_libraries(main PRIVATE fmt::fmt-header-only)
target_link_libraries(main PRIVATE $<IF:$<TARGET_EXISTS:FreeGLUT::freeglut>,FreeGLUT::freeglut,FreeGLUT::freeglut_static>)

# add tests
# 为每个测试源文件创建一个独立的可执行文件和测试
foreach(test_src ${TEST_SOURCES})
    get_filename_component(test_name ${test_src} NAME_WE)
    add_executable(${test_name} ${test_src})
    target_include_directories(${test_name} PRIVATE ${INCLUDE_DIR})
    target_link_libraries(${test_name} PRIVATE GTest::gtest GTest::gtest_main GTest::gmock GTest::gmock_main)
    add_test(NAME ${test_name} COMMAND ${test_name})
endforeach()
