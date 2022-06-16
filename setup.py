import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="json2ast",
    version="1.0.0",
    author="Adam Nichols",
    description="The opposite of ast2json",
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    package_dir={"": "src"},
    python_requires=">=3.10",
)