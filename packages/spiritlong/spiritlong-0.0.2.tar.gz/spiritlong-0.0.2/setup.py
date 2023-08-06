import	setuptools
import	re

with open("readme.txt", "r", encoding="utf-8") as f:
	description = f.read()


# 寻找特定的值
def find_value(text, key, default_value):
	value	= re.findall(r"^"+key+r"[\s]*(.*)", text, re.M)
	if not value:
		print(f"没找到{key}，使用默认值")
		value	= default_value
	else:
		value	= value[0].strip()
	return value
version	= find_value(description, 'version', '0.0.1')

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
	install_requires		= [
						'openpyxl',
						'mysqlclient',
						'psycopg2',
						'dbutils',
						'openpyxl',
					],
)

# python setup.py sdist bdist_wheel
# twine upload dist/* -u spiritlong