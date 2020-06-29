from setuptools import setup, find_packages
import os

with open("README.md") as f:
    readme = f.read()


def package_files():
    paths = []
    for (path, _, filenames) in os.walk("extra_files"):
        for filename in filenames:
            paths.append(os.path.join("..", path, filename))
    return paths


extra_files = package_files()

setup(
    name="mystify",
    version="0.0.1",
    description="NYI",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="NYI",
    author_email="NYI",
    url="https://github.com/machine-learning-apps/mystify",
    license="MIT License",
    keywords=["Jupyter", "Machine Learning", "Mystify"],  # Keywords that define your package best
    install_requires=[
        "wheel",
        'jupyter',
        'myst-parser'
    ],
    packages=["mystify"],
    include_package_data=True,
    package_data={"": extra_files},
    zip_safe=False,
    classifiers=[
        "Development Status :: 3 - Alpha",  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        "Intended Audience :: Developers",  # Define that your audience are developers
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",  # Again, pick a license
        "Programming Language :: Python :: 3",  # Specify which pyhton versions that you want to support
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.8",
    ],
)
