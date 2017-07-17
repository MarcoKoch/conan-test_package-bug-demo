from conans import ConanFile
import os

version = "0.1"
channel = os.getenv("CONAN_CHANNEL", "testing")
username = os.getenv("CONAN_USERNAME", "marcokoch")


class ConanBugDemoTest(ConanFile):
    requires = "test_package-bug-demo/%s@%s/%s" % (version, username, channel)
    
    def test(self):
        pass
