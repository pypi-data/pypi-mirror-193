# To work with PyPI.org

from pathlib import Path
import setuptools


setuptools.setup(
    name="stevenpdf",
    version=1.3,
    long_description=Path("./README.md").read_text(encoding="utf-8"),
    packages=setuptools.find_packages(exclude=["tests", "data"]),
)
