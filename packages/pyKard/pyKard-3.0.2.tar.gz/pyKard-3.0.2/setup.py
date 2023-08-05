import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


setuptools.setup(
    name="pyKard",
    version="3.0.2",
    author="Gaëtan Hérault",
    author_email="dev@ghr.lt",
    description="Python wrapper for Kard's private API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ghrlt/py-kard",
    project_urls={
    	"Developer website": "https://ghr.lt",
        "Bug Tracker": "https://github.com/ghrlt/py-kard/issues",
    },
    install_requires=[
        "requests"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    packages=["kard_private_api", "kard_private_api.kard", "kard_private_api.kard.karder"],
    python_requires=">=3.6",
)