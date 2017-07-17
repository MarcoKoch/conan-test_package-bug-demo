# Demonstration of ~~a bug~~ some unintuitive behavior in conan-io/conan

This demonstrates issue [conan-io/conan#1509].

**NOTE:**
As discussed in [the issue][conan-io/conan#1509],
the behavior demonstrated here is actually intentional and has now been
documented (see [conan-io/docs@46f10a1] and [conan-io/docs@72b1fcb]).

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

[conan-io/conan#1509]: https://github.com/conan-io/conan/issues/1509
[conan-io/docs@46f10a1]: https://github.com/conan-io/docs/commit/46f10a1e7ea050f661021a175835e303e329a0fe
[conan-io/docs@72b1fcb]: https://github.com/conan-io/docs/commit/72b1fcbee094a33299567b11c0424874e5905aea
