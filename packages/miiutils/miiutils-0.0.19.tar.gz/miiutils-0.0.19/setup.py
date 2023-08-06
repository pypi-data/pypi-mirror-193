import pathlib
from setuptools import setup
HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
setup(
  name="miiutils",
  version="0.0.19",
  description="",
  long_description=README,
  long_description_content_type="text/markdown",
  author="",
  author_email="",
  license="MIT",
  packages=["colorprint", "fileutils", "anotherpackage"], #module (second directory) name
  zip_safe=False
)
