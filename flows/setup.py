import os, urllib.request, tarfile
from setuptools import setup, find_packages

COMMIT = "59d7914a3457a12be76ae92d13c31861df90fa99"

url = f"https://github.com/rhandberg/flows/tarball/{COMMIT}"
filename, _ = urllib.request.urlretrieve(url)

tar = tarfile.open(filename)
directory = tar.getmembers()[0].name
tar.extractall()

os.system(f"mv {directory} flows")
os.system(f"cp config.cfg flows/flows/config.ini")
os.system(f"cp configure.py flows/flows/configure.py")

with open("flows/requirements.txt", 'r') as fd:
    requirements = fd.read().strip().split('\n')
links = [requirement for requirement in requirements if "http" in requirement]
requirements = list(set(requirements) - set(links))

setup(
    name = "flows",
    version = COMMIT,
    packages = find_packages(where="./flows"),
    package_dir = {"": "./flows"},
    install_requires = requirements,
    dependency_links = links,
    entry_points = {
        "console_scripts": [
            "flows-configure = flows.configure:main",
        ]
    },
    package_data = {"flows": ["config.ini"]},
    include_package_data = True
)
