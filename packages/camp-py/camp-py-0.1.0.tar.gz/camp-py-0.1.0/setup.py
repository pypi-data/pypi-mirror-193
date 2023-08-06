from setuptools import setup, find_packages

setup(
    name="camp-py",
    version="0.1.0",
    author="CAMP",
    author_email="contactcampsmm@gmail.com",
    description="CXMP MODULE",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "requests",
        "user-agent",
        "random",
    ],
)
