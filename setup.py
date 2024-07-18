# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

PKG = 'Liquirizia.Serializer.Implements.Text'
SRC = 'src'
EXCLUDES = []
DESC = 'Text Serializer of Liquirizia'
WHO = 'Heo Yongseon'

PKGS = [PKG]
DIRS = {PKG: SRC}
for package in find_packages(SRC, exclude=EXCLUDES):
	PKGS.append('{}.{}'.format(PKG, package))
	DIRS['{}.{}'.format(PKG, package)] = '{}/{}'.format(SRC, package.replace('.', '/'))

setup(
	name=PKG,
	description=DESC,
	long_description=open('README.md', encoding='utf-8').read(),
	long_description_content_type='text/markdown',
	author=WHO,
	version=open('VERSION', encoding='utf-8').read(),
	packages=PKGS,
	package_dir=DIRS,
	include_package_data=False,
	classifiers=[
		'Programming Language :: Python :: 3.8',
		'Programming Language :: Python :: 3.9',
		'Programming Language :: Python :: 3.10',
		'Programming Language :: Python :: 3.11',
		'Liquirizia',
		'Liquirizia :: Serializer',
		'Liquirizia :: Serializer :: Text',
	],
	install_requires=[
		'Liquirizia@git+https://github.com/yong5eon/Liquirizia.git',
	],
	python_requires='>=3.8'
)
