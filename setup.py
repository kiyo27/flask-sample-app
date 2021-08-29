import io
import os

from setuptools import setup, find_packages

def pip(filename):
    requirements = []
    for line in io.open(os.path.join("requirements", "{0}.pip".format(filename))):
        line = line.strip()
        if not line or "://" in line or line.startswith("#"):
            continue
        requirements.append(line)
    return requirements

install_requires = pip("install")

setup(
    name="flask-app",
    version="1.0.0",
    url="https://github.com/kiyo27/flask-sample-app",
    install_requirements=install_requires
)