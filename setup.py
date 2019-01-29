import setuptools

import mkalias

setuptools.setup(
    name='mkalias',
    version=mkalias.version,
    description='CLI app to create Finder aliases in OS X',
    url='https://github.com/iamcb/mkalias',
    packages=['mkalias'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: MacOS :: MacOS X",
    ],
    entry_points={
        'console_scripts': ['mkalias = mkalias.mkalias:main'],
    },
)
