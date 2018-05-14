from glob import glob
from os import walk
from os.path import isfile, join, splitext
from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install
from subprocess import call
from sys import platform, version_info

def install_certs(cmd):
    """
    Decorator for classes subclassing one of setuptools commands.

    Installs certificates before installing the package when running
    Python >= 3.6 on Mac OS.
    """
    orig_run = cmd.run

    def run(self):
        if platform == "darwin" and version_info >= (3, 6):
            INSTALL_CERTS = "/Applications/Python 3.6/Install Certificates.command"
            if not isfile(INSTALL_CERTS) or call(INSTALL_CERTS) != 0:
                raise RuntimeError("Error installing certificates.")
        orig_run(self)

    cmd.run = run
    return cmd


@install_certs
class CustomDevelop(develop):
    pass


@install_certs
class CustomInstall(install):
    pass


setup(
    author="Fozat",
    author_email="fozatkardouh@gmail.com",
    classifiers=[
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Topic :: Education",
        "Topic :: Utilities"
    ],
    description="This is submitRC, with which you can submit solutions to \
problems for submitRC.",
    install_requires=[
        "backports.shutil_get_terminal_size", "backports.shutil_which",
        "pexpect>=4.0", "requests", "six", "termcolor"
    ],
    keywords=["submitRC", "submitRC"],
    name="submitRC",
    py_modules=["submitRC"],
    cmdclass={
        "develop": CustomDevelop,
        "install": CustomInstall
    },
    entry_points={
        "console_scripts": ["submitRC=submitRC:main"]
    },
    url="https://github.com/RefugeesCodeAT/submitRC",
    version="2.4.7"
)
