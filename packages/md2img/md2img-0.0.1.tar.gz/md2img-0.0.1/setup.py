from distutils.core import setup
from setuptools import find_packages

with open("README.rst", "r", encoding="utf-8") as f:
  long_description = f.read()

setup(name='md2img',
      version='0.0.1',
      description='Markdown text to image',
      long_description=long_description,
      author='FishC',
      author_email='205204@qq.com',
      url='https://mp.weixin.qq.com/s/9FQ-Tun5FbpBepBAsdY62w',
      install_requires=["pillow"],
      license='GNU GPLv3 License',
      packages=find_packages(),
      platforms=["all"],
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Natural Language :: Chinese (Simplified)',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
          'Programming Language :: Python :: 3.11',
          'Topic :: Software Development :: Libraries'
      ],
      )
