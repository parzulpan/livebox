cmake_minimum_required(VERSION 3.5)

project(admin LANGUAGES CXX)

set(CMAKE_INCLUDE_CURRENT_DIR ON)

set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# QtCreator supports the following variables for Android, which are identical to qmake Android variables.
# Check http://doc.qt.io/qt-5/deployment-android.html for more information.
# They need to be set before the find_package(Qt5 ...) call.

#if(ANDROID)
#    set(ANDROID_PACKAGE_SOURCE_DIR "${CMAKE_CURRENT_SOURCE_DIR}/android")
#    if (ANDROID_ABI STREQUAL "armeabi-v7a")
#        set(ANDROID_EXTRA_LIBS
#            ${CMAKE_CURRENT_SOURCE_DIR}/path/to/libcrypto.so
#            ${CMAKE_CURRENT_SOURCE_DIR}/path/to/libssl.so)
#    endif()
#endif()

set(CMAKE_PREFIX_PATH /home/parzulpan/App/Qt5.12.9/5.12.9/gcc_64)

find_package(Qt5Widgets  REQUIRED)

if(ANDROID)
  add_library(admin SHARED
    main.cpp
    widget.cpp
    widget.h
  )
else()
  add_executable(admin
    main.cpp
    widget.cpp
    widget.h
  )
endif()

target_link_libraries(admin Qt5::Widgets)
message("parzulpan: build with debug mode.")