from setuptools import setup, find_packages

with open("README.MD", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="myllm",
    version="0.1.0",
    author="0xrushi",
    author_email="0xrushi@example.com",
    description="A Python package for MCP (Model Context Protocol) chatbot interactions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/0xrushi/myllm",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "myllm=myllm.cli:run",
        ],
    },
    include_package_data=True,
    package_data={
        "myllm": ["*.json"],
    },
)
