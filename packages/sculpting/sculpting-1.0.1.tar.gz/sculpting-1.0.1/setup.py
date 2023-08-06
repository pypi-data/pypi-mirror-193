from setuptools import setup, find_packages


PACKAGE_NAME = "sculpting"

VERSION = "1.0.1"

REQUIRES = ("pyannotating==1.2.1", "Pyhandling==2.2.0")

with open('README.md') as readme_file:
    LONG_DESCRIPTION = readme_file.read()

setup(
    name=PACKAGE_NAME,
    description="Library for sculpting objects from others",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license_files = ("LICENSE", ),
    version=VERSION,
    install_requires=REQUIRES,
    url="https://github.com/TheArtur128/Sculpting",
    download_url=f"https://github.com/TheArtur128/Sculpting/archive/refs/tags/v{VERSION}.zip",
    author="Arthur",
    author_email="s9339307190@gmail.com",
    python_requires='>=3.11',
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    keywords=[
        "library", "tools", "mapping", "utils", "data-mapping", "annotations",
        "mutability", "object-mapping", "attribute-mapping", "method-mapping",
        "imutability", "utils-library"
    ],
    packages=find_packages()
)