from setuptools import setup
import os

packages = []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

for dirpath, dirnames, filenames in os.walk('wurst'):
    # Ignore dirnames that start with '.'
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)

setup(
    name='wurst',
    version="0.1.dev",
    packages=packages,
    author="Chris Mutel",
    author_email="cmutel@gmail.com",
    license=open('LICENSE').read(),
    install_requires=[
        "appdirs",
        "docopt",
        "numpy",
        "pandas",
        "python-json-logger",
        "tqdm",
    ],
    entry_points = {
        'console_scripts': [
            'wurst-cli = wurst.bin.wurst_cli:main',
        ]
    },
    url="https://github.com/cmutel/wurst",
    long_description=open('README.md').read(),
    description=('Wurst is a python package for linking and modifying '
                 'industrial ecology models'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Mathematics',
    ],
)
