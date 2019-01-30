import setuptools


setuptools.setup(
    name='mkalias',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    description='CLI app to create Finder aliases in OS X',
    url='https://github.com/iamcb/mkalias',
    packages=['mkalias_cli'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: MacOS :: MacOS X",
    ],
    entry_points={
        'console_scripts':
            ['mkalias = mkalias_cli.mkalias:main', ],
    }
)
