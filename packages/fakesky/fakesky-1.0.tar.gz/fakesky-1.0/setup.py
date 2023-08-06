from setuptools import setup, find_packages

setup(
    name='fakesky',
    version='1.0',
    license='CC0 1.0',
    author="Drew Weisserman",
    author_email='drewweis@umich.edu',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/drewweis/fakesky',
    keywords='sky image',
    install_requires=[
        'matplotlib',
        'mpl_toolkits',
        'numpy',
        'pandas',
        'scipy',
        'astropy'
      ],

)