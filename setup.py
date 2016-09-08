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
