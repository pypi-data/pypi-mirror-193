from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="fibonacci_rattrapages-BS",
    version="0.2",
    author="Mon Nom",
    author_email="mon.email@example.com",
    description="Une brève description de mon projet",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mon-nom/mon-projet",
    packages=["fibonacci_rattrapages-BS"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "matplotlib>=3.4.0",
    ],
)
