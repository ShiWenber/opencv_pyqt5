# OpenGL Example Project

A modern C++ graphics project using OpenGL, FreeGLUT, and fmt library for high-performance rendering applications.

## Dependencies

This project uses vcpkg for package management with the following dependencies:

- **fmt**: Modern C++ formatting library
- **freeglut**: OpenGL Utility Toolkit for window management
- **gtest**: Google Test framework for unit testing

All dependencies are automatically managed through `vcpkg.json`.

## Prerequisites

- CMake 3.10 or higher
- Visual Studio 2022 (or compatible C++ compiler)
- vcpkg package manager

## Setup Instructions

### 1. Install vcpkg

If you haven't installed vcpkg yet:

```powershell
git clone https://github.com/Microsoft/vcpkg.git
cd vcpkg
.\bootstrap-vcpkg.bat
```

### 2. Configure vcpkg Environment

#### Option A: Environment Variable (Recommended)

Set the system environment variable:

```powershell
# PowerShell - Temporary
$env:VCPKG_ROOT = "YOUR_VCPKG_PATH"

# PowerShell - Permanent
[System.Environment]::SetEnvironmentVariable("VCPKG_ROOT", "YOUR_VCPKG_PATH", "User")
```

Replace `YOUR_VCPKG_PATH` with your actual vcpkg installation path, e.g., `C:\tools\vcpkg`.

#### Option B: User Preset File

Copy the example file and customize it:

```powershell
Copy-Item CMakeUserPresets.json.example CMakeUserPresets.json
```

Edit `CMakeUserPresets.json` and replace placeholders:

```json
{
  "version": 2,
  "configurePresets": [
    {
      "name": "default",
      "inherits": "vcpkg",
      "generator": "Visual Studio 17 2022",
      "environment": {
        "VCPKG_ROOT": "<path-to-vcpkg>",
        "VCPKG_DEFAULT_TRIPLET": "<vcpkg-triplet, e.g. x64-windows>",
        "VCPKG_DEFAULT_HOST_TRIPLET": "<vcpkg-triplet, e.g. x64-windows>",
      },
      "cacheVariables": {
        "CMAKE_C_COMPILER": "<path-to-compiler>",
        "CMAKE_CXX_COMPILER": "<path-to-compiler>",
      }
    }
  ],
  "buildPresets": [
    {
      "name": "Debug",
      "description": "Build with debug information",
      "displayName": "Debug Build",
      "configurePreset": "default"
    },
    {
      "name": "Release",
      "description": "Build with optimizations",
      "displayName": "Release Build",
      "configurePreset": "default"
    }
  ]
}
```

**Note**: The `CMakeUserPresets.json` file is ignored by Git to keep personal configurations private.

## Building the Project

### 1. Configure the Project

```powershell
cmake --preset=default
```

### 2. Build the Project

```powershell
# Build Debug version
cmake --build build/default --config Debug

# Build Release version
cmake --build build/default --config Release

# Alternative: Use build presets
cmake --build --preset=Debug
cmake --build --preset=Release
```

### 3. Run the Application

```powershell
# Run main application
.\build\default\Debug\main.exe

# Run tests
.\build\default\Debug\test_main.exe

# Or use CTest
cd build\default
ctest --output-on-failure
```

## Development Guide

### Adding New Source Files

The project uses CMake's `file(GLOB)` to automatically collect source files:

1. Add `.cpp` files to the `src/` directory
2. Add corresponding `.h` files to the `include/` directory
3. Re-run cmake configuration to include new files

### Adding New Tests

1. Create `test_*.cpp` files in the `tests/` directory
2. Use Google Test framework for writing tests
3. CMake will automatically create individual test executables for each test file

### Project Features

- **Automatic source file collection**: No need to manually maintain source file lists
- **Individual test executables**: Each test file generates its own executable
- **Modern CMake practices**: Uses target-specific commands instead of global settings
- **vcpkg integration**: Automatic dependency management

## Troubleshooting

### Common Issues

#### Q: vcpkg path not found

Ensure the `VCPKG_ROOT` environment variable is correctly set, or specify the correct path in `CMakeUserPresets.json`.

#### Q: Build failures

1. Verify vcpkg has installed all project dependencies
2. Check Visual Studio and CMake version compatibility
3. Clean build directory and retry: `Remove-Item -Recurse -Force build`

#### Q: Test execution failures

Ensure dependency DLL files are available in the executable directory or system PATH.

#### Q: Package installation issues

```powershell
# Manually install packages if needed
vcpkg install fmt:x64-windows
vcpkg install freeglut:x64-windows
vcpkg install gtest:x64-windows
```
