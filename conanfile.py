from conans import ConanFile

class ConanBugDemo(ConanFile):
    name = "test_package-bug-demo"
    version = "0.1"

    no_copy_source = True

    def package(self):
        self.output.info("Test!")
