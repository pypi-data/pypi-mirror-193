import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ProstateNetLoaders",
    version="0.0.1",
    author="Dimitris Zaridis",
    author_email="dimzaridis@email.com",
    description="Prostate Net loading functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dzaridis/ProstateNetLoading",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
