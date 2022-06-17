import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="json2ast",
    version="1.0.0",
    author="Adam Nichols",
    description="The opposite of ast2json",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HacMan137/json2ast",
    project_urls={
        "Bug tracker": "https://github.com/HacMan137/json2ast/issues"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    package_dir={"": "src"},
    python_requires=">=3.10",
)