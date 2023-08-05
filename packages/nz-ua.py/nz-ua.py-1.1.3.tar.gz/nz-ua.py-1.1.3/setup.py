from setuptools import setup, find_packages



long_description = 'With the help of this library, you can embed api from the nz-ua application into your projects.'
link = 'https://github.com/xXxCLOTIxXx/nz-ua.py/archive/refs/heads/main.zip'
ver = '1.1.3'

setup(
	name = "nz-ua.py",
	version = ver,
	url = "https://github.com/xXxCLOTIxXx/nz-ua.py",
	download_url = link,
	license = "MIT",
	author = "Xsarz",
	author_email = "xsarzy@gmail.com",
	description = "Library for working with the nz-ua application.",
	long_description = long_description,
	keywords = [
		"nz",
		"nz.py",
		"nz-ua",
		"nz-ua.py",
		"async"
		"api",
		"python",
		"python3",
		"python3.x",
		"xsarz",
		"official"
	],
	install_requires = [
		"colored",
		"aiohttp",
		"requests"
	],
	packages = find_packages()
)
