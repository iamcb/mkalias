import setuptools


setuptools.setup(
    name='mkalias',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    description='CLI app to create Finder aliases in OS X',
    url='https://github.com/iamcb/mkalias',
    packages=['mkalias'],
    scripts=['bin/mkalias.py'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: MacOS :: MacOS X",
    ],
)
