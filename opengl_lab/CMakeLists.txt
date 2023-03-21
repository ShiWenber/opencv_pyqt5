cmake_minimum_required(VERSION 3.0.0)

message("CMAKE_TOOLCHAIN_FILE: ${CMAKE_TOOLCHAIN_FILE}")
message("CMAKE_PROJECT_NAME: ${CMAKE_PROJECT_NAME}")
message("CMAKE_PROJECT_VERSION: ${CMAKE_PROJECT_VERSION}")
# CMAKE_PROJECT_NAME 和 PROJECT_NAME 的区别：CMAKE_PROJECT_NAME是顶层的项目名称，PROJECT_NAME是当前项目名称
# CMAKE_PROJECT_NAME表示最顶层的CMakeLists.txt中调用project()命令时指定的项目名称1。
# PROJECT_NAME表示当前目录范围或以上最近调用project()命令时指定的项目名称2。如果在第一个project()命令之前调用了set(PROJECT_NAME xxx)，那么PROJECT_NAME会被设置为xxx。
# 如果一个CMakeLists.txt中有多个project()命令，那么CMAKE_PROJECT_NAME只会被第一个project()命令设置，而PROJECT_NAME会被每个project()命令更新3。

## cmakelists中指定CMAKE_TOOLCHAIN_FILE变量，指定vcpkg的toolchain文件
# set(CMAKE_TOOLCHAIN_FILE "${CMAKE_CURRENT_SOURCE_DIR}/vcpkg/scripts/buildsystems/vcpkg.cmake" CACHE STRING "Vcpkg toolchain file")

project(opengl_lab VERSION 0.1.0) # cmake默认LANGUAGES是CXX 也可以使用 LANGUAGES CXX 来指定

message("PROJECT_NAME: ${PROJECT_NAME}")
message("PROJECT_VERSION: ${PROJECT_VERSION}")

include(CTest)
enable_testing()

# file(GLOB SRC_FILES
#     "${PROJECT_SOURCE_DIR}/src/*.h"
#     "${PROJECT_SOURCE_DIR}/src/*.cpp"
#     "${PROJECT_SOURCE_DIR}/src/*.c"
#     "${PROJECT_SOURCE_DIR}/src/*.hpp"
#     "${PROJECT_SOURCE_DIR}/src/*.cc"
#     "${PROJECT_SOURCE_DIR}/src/*.cxx"
#     "${PROJECT_SOURCE_DIR}/src/*.inl"
# )


find_package(FreeGLUT CONFIG REQUIRED)

find_package(GLU REQUIRED)

include_directories(include) # 同 gcc 的 -I<path> 相同 添加头文件

aux_source_directory(src SRC_FILES) # 添加源文件

# add_compile_options(-lglut) # 同 gcc 的 -l<lib> 相同

add_executable(${CMAKE_PROJECT_NAME} main.cpp ${SRC_FILES}) # 生成可执行文件 同 gcc 的 gcc ${SRC_FILES} -o ${CMAKE_PROJECT_NAME} 相同

target_link_libraries(${CMAKE_PROJECT_NAME} $<IF:$<TARGET_EXISTS:FreeGLUT::freeglut>,FreeGLUT::freeglut,FreeGLUT::freeglut_static>)

target_link_libraries(${CMAKE_PROJECT_NAME} OpenGL::GLU)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
message("PROJECT_NAME: ${PROJECT_NAME}")
message("PROJECT_VERSION: ${PROJECT_VERSION}")
include(CPack)
