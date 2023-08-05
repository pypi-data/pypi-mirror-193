# Try to find the KenLM library
#
# Options:
#   KENLM_DISABLE_UTILS_SEARCH: disable searching for libkenlm_utils
#
# The following variables are optionally searched for defaults
#   KENLM_ROOT: Base directory where all KENLM components are found
#
# The following are set after configuration is done:
#  KENLM_FOUND
#  KENLM_LIBRARIES
#  KENLM_INCLUDE_DIRS
#

message(STATUS "Looking for KenLM.")

if (NOT KENLM_DISABLE_UTILS_SEARCH)
  # Required for KenLM to read ARPA files in compressed format
  find_package(LibLZMA REQUIRED)
  find_package(BZip2 REQUIRED)
  find_package(ZLIB REQUIRED)
endif()

find_library(
  KENLM_LIB
  NAMES
  kenlm
  kenlm.dll
  HINTS
  ${KENLM_LIB_PATH}
  ${KENLM_ROOT}
  ${KENLM_ROOT}/lib
  ${KENLM_ROOT}/build/lib
  PATHS
  $ENV{KENLM_LIB_PATH}
  $ENV{KENLM_ROOT}
  $ENV{KENLM_ROOT}/lib
  $ENV{KENLM_ROOT}/build/lib
  )

if (WIN32)
  find_library(
    KENLM_IMPLIB
    NAMES
    kenlm.lib
    HINTS
    ${KENLM_LIB_PATH}
    ${KENLM_ROOT}
    ${KENLM_ROOT}/lib
    ${KENLM_ROOT}/build/lib
    PATHS
    $ENV{KENLM_LIB_PATH}
    $ENV{KENLM_ROOT}
    $ENV{KENLM_ROOT}/lib
    $ENV{KENLM_ROOT}/build/lib
    )
endif()

if (NOT KENLM_DISABLE_UTILS_SEARCH)
  find_library(
    KENLM_UTIL_LIB
    kenlm_util
    HINTS
    ${KENLM_UTIL_LIB_PATH}
    ${KENLM_ROOT}
    ${KENLM_ROOT}/lib
    ${KENLM_ROOT}/build/lib
    PATHS
    $ENV{KENLM_UTIL_LIB_PATH}
    $ENV{KENLM_ROOT}
    $ENV{KENLM_ROOT}/lib
    $ENV{KENLM_ROOT}/build/lib
    )

  if (WIN32)
    find_library(
      KENLM_UTIL_IMPLIB
      NAMES
      kenlm_util.lib
      HINTS
      ${KENLM_LIB_PATH}
      ${KENLM_ROOT}
      ${KENLM_ROOT}/lib
      ${KENLM_ROOT}/build/lib
      PATHS
      $ENV{KENLM_LIB_PATH}
      $ENV{KENLM_ROOT}
      $ENV{KENLM_ROOT}/lib
      $ENV{KENLM_ROOT}/build/lib
      )
  endif()
endif()

if(KENLM_LIB)
  message(STATUS "Using kenlm library found in ${KENLM_LIB}")
else()
  message(STATUS "kenlm library not found; if you already have kenlm installed, please set CMAKE_LIBRARY_PATH, KENLM_LIB or KENLM_ROOT environment variable")
endif()

if(KENLM_UTIL_LIB)
  message(STATUS "Using kenlm utils library found in ${KENLM_UTIL_LIB}")
else()
  if (NOT KENLM_DISABLE_UTILS_SEARCH)
    message(STATUS "kenlm utils library not found; if you already have kenlm installed, please set CMAKE_LIBRARY_PATH, KENLM_UTIL_LIB or KENLM_ROOT environment variable")
  else()
    message(STATUS "Findkenlm: KENLM_DISABLE_UTILS_SEARCH enabled - not searching for kenlm utils. Will not link when building")
  endif()
endif()

# find a model header, then get the entire include directory. We need to do this because
# cmake consistently confuses other things along this path
find_path(KENLM_MODEL_HEADER
  model.hh
  PATH_SUFFIXES
  kenlm/lm
  include/kenlm/lm
  HINTS
  ${KENLM_HEADER_PATH}
  ${KENLM_ROOT}
  ${KENLM_ROOT}/lm
  ${KENLM_ROOT}/include/kenlm/lm
  PATHS
  $ENV{KENLM_HEADER_PATH}
  $ENV{KENLM_ROOT}
  $ENV{KENLM_ROOT}/lm
  $ENV{KENLM_ROOT}/include/kenlm/lm
  )

if(KENLM_MODEL_HEADER)
  message(STATUS "kenlm model.hh found in ${KENLM_MODEL_HEADER}")

  get_filename_component(KENLM_INCLUDE_LM ${KENLM_MODEL_HEADER} DIRECTORY)
  get_filename_component(KENLM_INCLUDE_DIR ${KENLM_INCLUDE_LM} DIRECTORY)
else()
  message(STATUS "kenlm model.hh not found; if you already have kenlm installed, please set CMAKE_INCLUDE_PATH, KENLM_MODEL_HEADER or KENLM_ROOT environment variable")
endif()

set(COMPRESSION_LIBS
  ${LIBLZMA_LIBRARIES}
  ${BZIP2_LIBRARIES}
  ${ZLIB_LIBRARIES}
  )

set(KENLM_LIBRARIES
  ${KENLM_LIB}
  ${COMPRESSION_LIBRARIES}
  )
if (NOT KENLM_DISABLE_UTILS_SEARCH)
  # only need utils if finding it is not disabled
  list(APPEND KENLM_LIBRARIES ${KENLM_UTIL_LIB})
endif()

# Some KenLM include paths are relative to [include dir]/kenlm, not just [include dir] (bad)
set(KENLM_INCLUDE_DIRS "${KENLM_INCLUDE_DIR};${KENLM_INCLUDE_LM}")

include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(kenlm DEFAULT_MSG KENLM_INCLUDE_DIRS KENLM_LIBRARIES)

if (kenlm_FOUND)
  message(STATUS "Found kenlm (include: ${KENLM_INCLUDE_DIRS}, library: ${KENLM_LIBRARIES})")
  mark_as_advanced(KENLM_ROOT KENLM_INCLUDE_DIRS KENLM_LIBRARIES)

  if (BUILD_SHARED_LIBS)
    set(LIB_TYPE SHARED)
  else()
    set(LIB_TYPE STATIC)
  endif()

  if (NOT TARGET kenlm::kenlm)
    add_library(kenlm::kenlm ${LIB_TYPE} IMPORTED)
    set_property(TARGET kenlm::kenlm PROPERTY INTERFACE_INCLUDE_DIRECTORIES ${KENLM_INCLUDE_DIRS})
    set_property(TARGET kenlm::kenlm PROPERTY IMPORTED_LOCATION ${KENLM_LIB})
    set_property(TARGET kenlm::kenlm PROPERTY IMPORTED_IMPLIB ${KENLM_IMPLIB})
  endif()

  if (NOT TARGET kenlm::kenlm_util AND NOT KENLM_DISABLE_UTILS_SEARCH)
    add_library(kenlm::kenlm_util ${LIB_TYPE} IMPORTED)
    set_property(TARGET kenlm::kenlm_util PROPERTY INTERFACE_INCLUDE_DIRECTORIES ${KENLM_INCLUDE_DIRS})
    set_property(TARGET kenlm::kenlm_util PROPERTY IMPORTED_LOCATION ${KENLM_UTIL_LIB})
    set_property(TARGET kenlm::kenlm_util PROPERTY IMPORTED_IMPLIB ${KENLM_UTIL_IMPLIB})
    set_property(TARGET kenlm::kenlm_util PROPERTY IMPORTED_LINK_INTERFACE_LIBRARIES ${COMPRESSION_LIBS})
  endif()
endif()
