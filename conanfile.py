from conans import ConanFile, CMake, tools


class MkxpConan(ConanFile):
    name = "mkxp"
    version = "0.0.0"
    license = "GPLv2"
    url = "https://github.com/Ancurio/mkxp"
    description = "Free Software implementation of the Ruby Game Scripting System (RGSS)"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "*"
    requires = (
        "boost/1.68.0@conan/stable",
        "openal/1.18.2@bincrafters/stable",
        "physfs/3.0.1@eliza/stable",
        "pixman/0.34.0@bincrafters/testing",
        "ruby-mkxp/2.5.1@eliza/stable",
        "sdl2/2.0.8@bincrafters/stable",
        "sdl2_image/2.0.3@bincrafters/stable",
        "sdl2_ttf/2.0.14@eliza/stable",
        "sdl_sound-mkxp/0.0.0@eliza/stable",
        "sigc++/2.10.0@eliza/stable",
    )
    options = {
        "ini_encoding": [True, False],
    }
    disabled_boost_components = (
        'math', 'wave', 'container', 'contract', 'exception', 'graph',
        'iostreams', 'locale', 'log', 'random', 'regex', 'mpi',
        'serialization', 'signals', 'coroutine', 'fiber', 'context', 'timer',
        'thread', 'chrono', 'date_time', 'atomic', 'filesystem', 'system',
        'graph_parallel', 'python', 'stacktrace', 'test', 'type_erasure',
    )
    default_options = (
        "ini_encoding=True",
    ) + tuple("boost:without_{}=True".format(c) for c in disabled_boost_components)

    def requirements(self):
        if self.options.ini_encoding:
            self.requires("libiconv/1.15@bincrafters/stable")
            self.requires("libguess/0.0.0@eliza/stable")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="hello")
        self.copy("*hello.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
