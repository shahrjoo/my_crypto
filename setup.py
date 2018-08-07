import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="my_crypto",
    version="1.0.0",
    author="Ali Shahrjoo",
    author_email="ali.shahrjoo@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shahrjoo/my_crypto",
    packages=setuptools.find_packages(),
    license='MIT',
#    classifiers=(
#        "Programming Language :: Python :: 3",
#        "License :: OSI Approved :: MIT License",
#        "Operating System :: OS Independent",
#    ),
)

