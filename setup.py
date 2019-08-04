from distutils.core import setup

setup(
		name = 'python-candy',
		version = '0.0.1',
		description = 'Python common utilities',
		author = 'Chris Chou',
		author_email = 'm2chrischou@gmail.com',
		url = 'https://github.com/mongmong/python-candy',
		classifiers = [
			'Programming Language :: Python',
			'Development Status :: 2 - Pre-Alpha',
			'Topic :: Software Development :: Libraries :: Python Modules',
			],
		package_dir = {'': 'src'},
		packages = ['candy'],
)

