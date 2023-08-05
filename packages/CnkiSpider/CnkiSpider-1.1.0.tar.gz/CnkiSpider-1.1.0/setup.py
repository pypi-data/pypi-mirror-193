import setuptools

with open("README.md", "r",encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="CnkiSpider",
    version='1.1.0',
    author="zemengchuan",
    author_email="zemengchuan@gmail.com",
    license="MIT",
    description="CnkiSpider是一个高效爬取知网文章信息的包",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zemengchuan/CnkiSpider",
    packages=setuptools.find_packages(),
    install_requires=[
        "requests",
        "pandas",
    ],
    keywords=["CNKI", "webcrawler", "data", "lxml"],
    package_data={"": ["*.py"]},
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)