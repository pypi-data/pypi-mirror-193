import setuptools
from pathlib import Path

setuptools.setup(
    name="taxmin_raqam_gen",
    version="0.0.1",
    long_description=Path("README.md").read_text(),
    packages=setuptools.find_packages(exclude=["data", "tests"])
)