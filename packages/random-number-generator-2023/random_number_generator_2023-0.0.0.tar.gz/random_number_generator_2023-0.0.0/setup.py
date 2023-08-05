import setuptools
from pathlib import Path

setuptools.setup(
    name="random_number_generator_2023",
    long_description=Path("README.md").read_text(),
    packages=setuptools.find_packages(exclude=["data", "tests"])
)