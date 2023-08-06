from setuptools import setup


with open("README.md", "r") as readme:
    readme = readme.read()

setup(
    name="imstegapy",
    description="A small image steganography tool.",
    version="0.1.0",
    long_description=readme,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/Jedddy/imsteg",
    author="Jedddy",
    packages=["imsteg"],
    install_requires=[
        "numpy==1.24.2",
        "Pillow==9.4.0"
    ]
)
