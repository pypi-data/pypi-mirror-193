import os
import sys

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

packages = ["aioanixart"]

requires = ["aiohttp"]

# 'setup.py publish' shortcut.
if sys.argv[-1] == "publish":
    os.system("py -m build")
    os.system("py -m twine upload --repository testpypi dist/*")
    os.system("py -m twine upload --repository pypi dist/*")
    sys.exit()

setup(
    name="aioanixart",
    version="24.02.23",
    description="Asynchronous wrapper for Anixart API",
    long_description="ok",
    long_description_content_type="text/markdown",
    author="ca4tuk",
    author_email="ca4tuk@gmail.com",
    url="https://github.com/ca4tuk/aioanixart",
    packages=packages,
    package_data={"": ["LICENSE"]},
    package_dir={"aioanixart": "src/aioanixart"},
    include_package_data=True,
    install_requires=requires,
    license="GPL-3.0",
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: Russian",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    project_urls={
        "Source": "https://github.com/ca4tuk/manga-in-ua",
    },
    python_requires=">=3.8",
)
