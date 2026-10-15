from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="deploynator",
    version="1.0.0",
    description="Multi-platform deployer for GitHub, GitLab, and Bitbucket",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/grisuno/deploynator",
    author="Gris Iscomeback",
    license="AGPL-3.0",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "pyyaml>=6.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
            "readmenator>=1.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "deploynator=deploynator.__main__:main",
            "deploynator-mcp=deploynator._mcp_server:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Software Development :: Version Control",
        "Topic :: Software Development :: Build Tools",
    ],
)
