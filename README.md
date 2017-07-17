# Demonstration of a bug in conan-io/conan

Build this test package with

    conan test_package

The message "Test!" should be displayed twice in conan's output.
That indicates that the `package()` method of [conanfile.py](conanfile.py)
is executed twice during a single build.

Change the line

    no_copy_source = True
    
in [conanfile.py](conanfile.py) to

    no_copy_source = False

and build the package again:

    conan test_package

Now "Test!" should be displayed only once.
