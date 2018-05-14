from os.path import isfile
from setuptools import find_packages, setup
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
    description="This is check50, with which you can check solutions to problems for CS50.",
    install_requires=["argparse", "bs4", "pexpect", "requests", "backports.shutil_which", "six",
                      "termcolor", "submitRC>=2.4.5",  "submit50>=2.4.5"],
    keywords=["check50", "checkRC"],
    name="checkRC",
    py_modules=["checkRC", "config"],
    cmdclass={
        "develop": CustomDevelop,
        "install": CustomInstall
    },
    packages=find_packages(),
    entry_points={
        "console_scripts": ["check50=checkRC:main"]
    },
    url="https://github.com/RefugeesCodeAT/check50-RC-edition",
    version="2.2.2"
)
