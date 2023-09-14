from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Common Library for ZiTrade'
LONG_DESCRIPTION = 'Common Library for ZiTrade'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="common_lib", 
        version=VERSION,
        author="Ziii",
        author_email="<canamg2000@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)