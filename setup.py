from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="tfilterpy",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    author="Thabang L. Mashinini-Sekgoto",
    author_email="thabangline@gmail.com",
    description="A Python package for Bayesian filtering models such as Kalman and Particle Filters.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://leparalamapara.github.io/tfilterpy/",
    project_urls={
        "Documentation": "https://leparalamapara.github.io/tfilterpy/",
        "Source": "https://github.com/LeparaLaMapara/tfilterpy",
        "Tracker": "https://github.com/LeparaLaMapara/tfilterpy/issues",
        "Logo": "https://raw.githubusercontent.com/LeparaLaMapara/tfilterpy/main/branding/logo/tfilters-logo.jpeg",
    },
    packages=find_packages(),
    install_requires=[
        "dask>=2024.8.0",
    ],
    extras_require={
        "dev": ["pytest", "sphinx"],
    },
    keywords="kalman filter, particle filter, Bayesian filtering, distributed computing, Dask, UAIE, Ubunye-AI-Ecosystems",
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_data={
        "": ["examples/*.ipynb"],
    },
    include_package_data=True,
    # Uncomment the following if you have command-line tools
    # entry_points={
    #     "console_scripts": [
    #         "tfilterpy=tfilterpy.cli:main",
    #     ],
    # },
)
