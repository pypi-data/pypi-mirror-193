import pathlib
from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent.resolve()

install_requires = (here / 'requirements.txt').read_text(encoding='utf-8').splitlines()

setup(
    name="freedom_utils",
    version="0.0.2",
    keywords=("dev tools", "dev utils"),
    description="dev utils, help developer coding, then have more freedom",
    long_description="dev utils, help developer coding, then have more freedom",
    license="MIT Licence",

    url="https://github.com/wujunwei928/freedom_utils",
    author="wujunwei",
    author_email="1399952803@qq.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    python_requires=">=3.7",
    install_requires=install_requires,
)
