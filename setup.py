from setuptools import setup, find_packages


def get_version():
    """Read version from version.py file"""
    version_file = "agentx/version.py"
    with open(version_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("VERSION"):
                return line.split("=")[1].strip().strip('"').strip("'")
    raise RuntimeError("Unable to find version string.")


def get_long_description():
    """Read README.md file"""
    with open("README.md", "r", encoding="utf-8") as f:
        return f.read()


setup(
    name="agentx-python",
    version=get_version(),
    packages=find_packages(),
    install_requires=[
        "urllib3>=1.26.11",
        "certifi",
    ],
    author="Robin Wang and AgentX Team",
    author_email="contact@agentx.so",
    description="Official Python SDK for AgentX (https://www.agentx.so/)",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/AgentX-ai/AgentX-python-sdk",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
