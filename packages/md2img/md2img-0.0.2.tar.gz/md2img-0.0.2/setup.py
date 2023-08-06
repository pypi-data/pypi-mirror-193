from distutils.core import setup
from setuptools import find_namespace_packages

with open("README.rst", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(name = 'md2img',
      version = '0.0.2',
      description = 'Markdown text to image',
      long_description = long_description,
      author = 'FishC',
      author_email = '205204@qq.com',
      url = 'https://fishc.com.cn',
      install_requires = ["pillow"],
      packages = find_namespace_packages(include=["md2img", "im2img.*"],),
      include_package_data = True,
      license = 'GNU GPLv3 License',
      # packages = find_packages(),
      platforms = ["all"],
      classifiers = [
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Natural Language :: Chinese (Simplified)',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Topic :: Software Development :: Libraries'
      ],
      )
