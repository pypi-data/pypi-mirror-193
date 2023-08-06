import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


__version__ = "0.0.2"


REPO_NAME = "videoIpynbRenderer"
AUTHOR_USER_NAME = "SoumitSarkar"
SRC_REPO = REPO_NAME
AUTHOR_EMAIL = "sayhi2soumit@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="a small python package",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},
    # to find the package src\ipynbRenderer directory
    packages=setuptools.find_packages(where="src"),
)
