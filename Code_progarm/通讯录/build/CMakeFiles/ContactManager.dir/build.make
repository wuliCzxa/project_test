# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.30

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = E:\Software\CMake\bin\cmake.exe

# The command to remove a file.
RM = E:\Software\CMake\bin\cmake.exe -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = E:\Software\Code_progarm\通讯录

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = E:\Software\Code_progarm\通讯录\build

# Include any dependencies generated for this target.
include CMakeFiles/ContactManager.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/ContactManager.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/ContactManager.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/ContactManager.dir/flags.make

CMakeFiles/ContactManager.dir/ContactManager_autogen/mocs_compilation.cpp.obj: CMakeFiles/ContactManager.dir/flags.make
CMakeFiles/ContactManager.dir/ContactManager_autogen/mocs_compilation.cpp.obj: CMakeFiles/ContactManager.dir/includes_CXX.rsp
CMakeFiles/ContactManager.dir/ContactManager_autogen/mocs_compilation.cpp.obj: ContactManager_autogen/mocs_compilation.cpp
CMakeFiles/ContactManager.dir/ContactManager_autogen/mocs_compilation.cpp.obj: CMakeFiles/ContactManager.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=E:\Software\Code_progarm\通讯录\build\CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/ContactManager.dir/ContactManager_autogen/mocs_compilation.cpp.obj"
	E:\Software\Qt\Qt5.12.12\Tools\mingw730_32\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/ContactManager.dir/ContactManager_autogen/mocs_compilation.cpp.obj -MF CMakeFiles\ContactManager.dir\ContactManager_autogen\mocs_compilation.cpp.obj.d -o CMakeFiles\ContactManager.dir\ContactManager_autogen\mocs_compilation.cpp.obj -c E:\Software\Code_progarm\通讯录\build\ContactManager_autogen\mocs_compilation.cpp

CMakeFiles/ContactManager.dir/ContactManager_autogen/mocs_compilation.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/ContactManager.dir/ContactManager_autogen/mocs_compilation.cpp.i"
	E:\Software\Qt\Qt5.12.12\Tools\mingw730_32\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E E:\Software\Code_progarm\通讯录\build\ContactManager_autogen\mocs_compilation.cpp > CMakeFiles\ContactManager.dir\ContactManager_autogen\mocs_compilation.cpp.i

CMakeFiles/ContactManager.dir/ContactManager_autogen/mocs_compilation.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/ContactManager.dir/ContactManager_autogen/mocs_compilation.cpp.s"
	E:\Software\Qt\Qt5.12.12\Tools\mingw730_32\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S E:\Software\Code_progarm\通讯录\build\ContactManager_autogen\mocs_compilation.cpp -o CMakeFiles\ContactManager.dir\ContactManager_autogen\mocs_compilation.cpp.s

# Object files for target ContactManager
ContactManager_OBJECTS = \
"CMakeFiles/ContactManager.dir/ContactManager_autogen/mocs_compilation.cpp.obj"

# External object files for target ContactManager
ContactManager_EXTERNAL_OBJECTS =

ContactManager.exe: CMakeFiles/ContactManager.dir/ContactManager_autogen/mocs_compilation.cpp.obj
ContactManager.exe: CMakeFiles/ContactManager.dir/build.make
ContactManager.exe: E:/Software/Qt/Qt5.12.12/5.12.12/mingw73_32/lib/libQt5Widgetsd.a
ContactManager.exe: E:/Software/Qt/Qt5.12.12/5.12.12/mingw73_32/lib/libQt5Guid.a
ContactManager.exe: E:/Software/Qt/Qt5.12.12/5.12.12/mingw73_32/lib/libQt5Cored.a
ContactManager.exe: CMakeFiles/ContactManager.dir/linkLibs.rsp
ContactManager.exe: CMakeFiles/ContactManager.dir/objects1.rsp
ContactManager.exe: CMakeFiles/ContactManager.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir=E:\Software\Code_progarm\通讯录\build\CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable ContactManager.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\ContactManager.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/ContactManager.dir/build: ContactManager.exe
.PHONY : CMakeFiles/ContactManager.dir/build

CMakeFiles/ContactManager.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\ContactManager.dir\cmake_clean.cmake
.PHONY : CMakeFiles/ContactManager.dir/clean

CMakeFiles/ContactManager.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" E:\Software\Code_progarm\通讯录 E:\Software\Code_progarm\通讯录 E:\Software\Code_progarm\通讯录\build E:\Software\Code_progarm\通讯录\build E:\Software\Code_progarm\通讯录\build\CMakeFiles\ContactManager.dir\DependInfo.cmake "--color=$(COLOR)"
.PHONY : CMakeFiles/ContactManager.dir/depend

