import setuptools

with open("README.md", 'r') as f:
    long_description = f.read()
    
setuptools.setup(
    name="outlinr",
    version="0.0.1",
    author="Thetis",
    author_email="736396627@qq.com",
    description="Outlier",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent"
    ],
    python_requires='>3.6'
)    
