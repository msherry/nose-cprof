import os
import re

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages


# Try to convert the readme to RST, which is what PyPi supports. The only
# developers who need pypandoc installed are maintainers of this plugin
try:
    import pypandoc
    long_description = pypandoc.convert_file('README.md', 'rst')
except ImportError:
    long_description = open('README.md').read()


setup(
    name='nose-cprof',
    version=(
        re
        .compile(r".*__version__ = '(.*?)'", re.S)
        .match(open(os.path.join('nose_cprofile', '__init__.py')).read())
        .group(1)
    ),
    description=(
        'A python nose plugin to profile using cProfile rather than '
        'the default Hotshot profiler.'),
    long_description=long_description,
    author='Marc Sherry',
    author_email='msherry@gmail.com',
    url='https://github.com/msherry/nose-cprof',
    install_requires=[
        'nose >=1.0.0',
    ],
    setup_requires=[],
    test_suite='nose.collector',
    zip_safe=False,
    packages=find_packages(),
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    entry_points={
        'nose.plugins.0.10': [
            'nose_cprofile = nose_cprofile:cProfiler',
        ]
    },
)
