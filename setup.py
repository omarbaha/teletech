from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in teletech/__init__.py
from teletech import __version__ as version

setup(
	name="teletech",
	version=version,
	description="teletech",
	author="info@wowit.sa",
	author_email="info@wowit.sa",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
