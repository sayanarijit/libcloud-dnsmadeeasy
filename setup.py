#!/usr/bin/env python
# coding=utf-8

import setuptools
import sys

from setuptools.command.test import test


NAME = "libcloud-dnsmadeeasy"
DESCRIPTION = "A driver for DNSMadeEasy for libcloud DNS"
URL = "https://github.com/moses-palmer/libcloud-dnsmadeeasy"
AUTHOR_NAME = "Moses Palmér"
AUTHOR_EMAIL = "moses.palmer@gmail.com"
INSTALL_REQUIRES = ["hammock >=0.2.4", "apache-libcloud >=0.14.1"]
SETUP_REQUIRES = INSTALL_REQUIRES
VERSION = "1.1"


class test_runner(test):
    user_options = [("suites=", "s", "A list of test suites separated by comma (,)")]

    def initialize_options(self):
        self.suites = None

    def finalize_options(self):
        if self.suites is not None:
            self.suites = self.suites.split(",")

    def run(self):
        import tests

        failures = tests.run(self.suites)

        print("")
        print("All test suites completed with %d failed tests" % len(failures))
        if failures:
            sys.stderr.write(
                "Failed tests:\n%s\n"
                % "\n".join(
                    "\t%s - %s" % (test.name, test.message) for test in failures
                )
            )
        sys.exit(len(failures))


setuptools.setup(
    name=NAME,
    description=DESCRIPTION,
    version=VERSION,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    url=URL,
    packages=setuptools.find_packages(exclude=["contrib", "docs", "tests"]),
    scripts=[],
    install_requires=INSTALL_REQUIRES,
    setup_requires=SETUP_REQUIRES,
    zip_safe=True,
    cmdclass={"test": test_runner},
)

