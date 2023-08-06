import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="emojidb",
    version="0.0.2",
    author="James Zhan",
    author_email="zhiqiangzhan@gmail.com",
    description="Emoji DB package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jameszhan/emojidb",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)