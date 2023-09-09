import setuptools

with open("README.md", "r", encoding="utf-8") as f_reader:
    readme_description = f_reader.read()

setuptools.setup(
    name="family-tree-tool",
    version="0.0.1",
    author="Akash Kumar",
    author_email="ashky.236@gmail.com",
    description=("A family tree CLI tool wrapped as a python package to "
                "track a family tree with all the CRUD operations available on the family tree."),
    long_description=readme_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ashky23/Family-Tree-CLI-pkg",
    project_urls={
        "Bug Tracker": "https://github.com/ashky23/Family-Tree-CLI-pkg/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[""],
    packages=setuptools.find_packages(),
    python_requires=">=3.10",
    entry_points={
        "console_scripts": [
            "family-tree = cli.main:main",
        ]
    }
)