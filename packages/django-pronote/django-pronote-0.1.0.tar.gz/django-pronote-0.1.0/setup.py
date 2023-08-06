from setuptools import setup
from os import path

from pronote import __version__

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="django-pronote",
    version=__version__,
    description="Handle CAS login for Pronote (index éducation)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/briefmnews/django-pronote",
    author="Brief.me",
    author_email="tech@brief.me",
    license="GNU GPL v3",
    packages=["pronote"],
    python_requires=">=3.9",
    install_requires=[
        "Django>=3.2",
        "djangorestframework>=3",
    ],
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    include_package_data=True,
    zip_safe=False,
)
