from conans import ConanFile, CMake, tools
import os


class TestPackageConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake_find_package"

    def build(self):
        cmake = CMake(self)
        cmake.configure(defs={'CMAKE_VERBOSE_MAKEFILE': 'ON'})
        cmake.build()

    def test(self):
        if not tools.cross_building(self.settings):
            bin_path = os.path.join(self.build_folder, "test_package")
            self.run(bin_path, run_environment=True)
