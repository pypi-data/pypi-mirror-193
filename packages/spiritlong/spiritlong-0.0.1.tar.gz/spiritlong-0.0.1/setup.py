import	setuptools
import	re

with open("readme.txt", "r", encoding="utf-8") as f:
	description = f.read()

version	= '0.0.1'

setuptools.setup(
	name				= "spiritlong",
	version				= version,
	author				= "SpiritLong",
	author_email			= "arthuryang@spiritlong.com",
	maintainer			= "SpiritLong",
	maintainer_email		= "shun@spiritlong.com",
	description			= "SpiritLong tools",
	long_description		= description,
	long_description_content_type	= "text/markdown",
	url				= "https://spiritlong-exon.com/pip",
	packages			= setuptools.find_packages(),
	classifiers			= [
						'Development Status :: 3 - Alpha',
						"Programming Language :: Python :: 3",
						'Intended Audience :: Developers',
						'Operating System :: OS Independent',
					],
	python_requires			= '>=3.6',
	install_requires		= ['docutils>=0.3'],
)

# python setup.py sdist bdist_wheel
# twine upload dist/*