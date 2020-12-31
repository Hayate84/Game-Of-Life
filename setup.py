import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Game-of-life-pkg-Hayate84",
    version="0.0.1",
    author="Dimitris Dimitriou",
    author_email="dddimitriou84@gmail.com",
    description="A Pygame visualization of Conway's Game of Life",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hayate84/Game-Of-Life",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
