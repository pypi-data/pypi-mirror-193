from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="hil-test-framework",
    version="0.0.1",
    author="Pass Testing Solutions GmbH",
    description="HiL Self Test Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author_email="shuparna@pass-testing.de",
    url="https://gitlab.com/pass-testing-solutions/hil-test-framework",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    py_modules=["hil-test-framework"],
    packages=find_packages(include=['hil-test-framework']),
    include_package_data=True,
)
