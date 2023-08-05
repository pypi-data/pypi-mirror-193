import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="canheting",
    version="0.0.0",
    author="canheting",
    author_email="2380348167@qq.com",
    description="This is a test",  # 介绍
    long_description=long_description,
    long_description_content_type="text/markdown",
    # 如果自己写的，在GitHub有就写GitHub地址，或者其他地址，没有就写pypi自己的url地址
    url="https://upload.pypi.org/OnePush",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],  # 这个文件适用的python版本，安全等等，我这里只写入了版本
)
