import setuptools

with open("README.md", "r",encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "text_summarizer"
AUTHOR_USER_NAME = "arpit000000"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "tarpit324@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A Python package for summarizing text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/" + AUTHOR_USER_NAME + "/" + SRC_REPO,
    project_urls={
        "Bug Tracker": "https://github.com/" + AUTHOR_USER_NAME + "/" + SRC_REPO + "/issues",

    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)