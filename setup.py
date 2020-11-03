import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pkg_hb",
    version="0.0.1",
    author="Preyansh Nagpal",
    author_email="preyansh7499@gmail.com",
    description="Voice Based Personal Assistant",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Preyansh7499/Personal_Assistant",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)