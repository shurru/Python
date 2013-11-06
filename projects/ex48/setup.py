#edit this to have all the information for the project. 
try: 
	from setuptools import setuptools
except ImportError: 
	from distutils.core import setuptools

config= {
	'Description': 'My Project', 
	'author': 'My name', 
	'url': 'URL to get it at', 
	'download_url': 'where to dnwload it', 
	'author_email': 'my email',
	'version': '0.1', 
	'install_requires': ['nose'], 
	'packages': ['ex48'], 
	'scripts': [ ], 
	'name': 'projectname'
}
setup(**config)
}