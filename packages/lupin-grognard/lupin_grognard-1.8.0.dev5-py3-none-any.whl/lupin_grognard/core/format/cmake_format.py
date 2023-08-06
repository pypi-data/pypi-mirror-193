import logging
import os
import shutil
import subprocess
from typing import List

from lupin_grognard.core.tools.utils import die


class CMakeFormatter:
    def format_cmake_files(self) -> None:
        if not self._check_cmake_format_tool():
            die(msg="could not find CMake-Format, install it from https://github.com/cheshirekow/cmake_format")
        cmake_files = self._find_cmake_files()
        if len(cmake_files) == 0:
            die(msg="no CMake files found")
        for file in cmake_files:
            self._format_file(file)

    def _check_cmake_format_tool(self) -> bool | None:
        """Check if cmake-format tool is installed on the system and available in the PATH"""
        path = shutil.which("cmake-format")
        return path is not None

    def _find_cmake_files(self) -> List[str]:
        """Search all CMake files in the code directory and subdirectories
        return a list of CMake files paths"""
        cmake_files = []
        for root, dirs, files in os.walk(os.getcwd()):
            for file in files:
                if file == "CMakeLists.txt" or file.endswith(".cmake"):
                    cmake_file_path = os.path.join(root, file)
                    cmake_files.append(cmake_file_path.replace("/", "\\"))
        return cmake_files

    def _format_file(self, file: str) -> None:
        """Format the CMake files"""
        logging.info(f"Formatting CMake file: {file}")
        subprocess.run(["cmake-format", "-i", file])
