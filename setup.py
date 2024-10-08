from setuptools import setup, find_packages

with open('README.md','r',encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='FluroView',
    version = "0.2.0",
    author='Biswanath Saha',
    author_email='bsaha0659@gmail.com',
    description = 'A Python package for visualization of biological data, similar to how composite images are viewed in ImageJ',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    package_dir = {'':'src'},
    packages = find_packages(where='src'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.7",
    install_requires=[
        "numpy",
        "matplotlib",
        "matplotlib-scalebar",
    ],
)