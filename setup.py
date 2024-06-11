from setuptools import setup, find_packages

setup(
    name="agentx-python",
    version="0.2.1",  # Update this version number each time you make a release
    packages=find_packages(),
    install_requires=[
        "urllib3>=1.26.11",
        "certifi",
    ],
    author="Robin Wang and AgentX Team",
    author_email="contact@agentx.so",
    description="Offical Python SDK for AgentX (https://www.agentx.so/)",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/AgentX-ai/AgentX-python-sdk",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
