import os

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages


PATH_TO_FILE = os.path.dirname(__file__)


with open(os.path.join(PATH_TO_FILE, 'README.md')) as f:
    long_description = f.read()


VERSION = (0, 1, 2)


# Dynamically calculate the version based on VERSION tuple
if len(VERSION) > 2 and VERSION[2] is not None:
    str_version = "%s.%s_%s" % VERSION[:3]
else:
    str_version = "%s.%s" % VERSION[:2]


version = str_version


setup(
    name='nose-cprof',
    version=version,
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
