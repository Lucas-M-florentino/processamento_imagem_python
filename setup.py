from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    requirements = fh.read().splitlines()

setup(
    name="processamento_imagem_python",
    version="0.1.0",
    author="Lucas Florentino",
    author_email="lucas.florentino2014@gmail.com",
    description="Processamento de imagem em Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Lucas-M-florentino/processamento_imagem_python",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)