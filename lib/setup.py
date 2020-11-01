import os

from setuptools import find_packages, setup


def get_version():
    with open(os.path.join("src", "lg", "__init__.py")) as f:
        for line in f:
            if line.startswith("__version__"):
                return eval(line.split("=")[-1])


def get_long_description():
    descr = []
    with open("README.md") as f:
        descr.append(f.read())
    return "\n\n".join(descr)


setup(
    name="lg.lib",
    version=get_version(),
    description="Learning genie data access library",
    long_description=get_long_description(),
    keywords="learning genie",
    author="Raul Chacon",
    url="https://github.com/rchacon/learning-genie",
    license="MIT license",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=["requests==2.24.0"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
