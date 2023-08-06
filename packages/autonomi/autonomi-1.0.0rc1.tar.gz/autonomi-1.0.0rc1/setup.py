import re
import sys

if sys.version_info < (3, 7, 0):
    raise RuntimeError("Autonomi AI python client requires Python 3.7.0 or later.")


from setuptools import setup


def find_version(file_path: str) -> str:
    version_file = open(file_path).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if not version_match:
        raise RuntimeError(f"Unable to find version string in {file_path}")
    return version_match.group(1)


# open readme file and set long description
with open("README.md", encoding="utf-8") as fh:
    long_description = fh.read()


def load_requirements(filename: str):
    with open(filename) as f:
        return [x.strip() for x in f.readlines() if "-r" != x[0:2]]


requirements = load_requirements("requirements/requirements.txt")
requirements_extras = {"dev": load_requirements("requirements/requirements.dev.txt")}
requirements_extras["all"] = requirements_extras["dev"]

if __name__ == "__main__":
    setup(
        version=find_version("autonomi/client/_version.py"),
        author="Sudeep Pillai",
        author_email="sudeep@autonomi.ai",
        url="https://www.autonomi.ai",
        download_url="https://github.com/autonomi-ai/autonomi-client",
        long_description=long_description,
        long_description_content_type="text/markdown",
        setup_requires=["pytest-runner"],
        tests_require=["pytest"],
        install_requires=requirements,
        extras_require=requirements_extras,
    )
