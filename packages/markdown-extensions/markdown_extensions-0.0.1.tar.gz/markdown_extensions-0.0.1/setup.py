import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="markdown_extensions",
    version="0.0.1",
    author="James Zhan",
    author_email="zhiqiangzhan@gmail.com",
    description="Markdown Extensions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jameszhan/markdown-extensions",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
    install_requires=['emojidb>=0.0.3'],
)
