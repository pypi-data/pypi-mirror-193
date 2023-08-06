from setuptools import setup, find_packages

VERSION = '1.0.6' 
DESCRIPTION = 'a small package with quality of life unilities to data analysis with pyspark'
LONG_DESCRIPTION = 'a small package with quality of life unilities to data analysis with pyspark'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="lushalytics", 
        version=VERSION,
        author="Moran Reznik",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'first package'],
        classifiers= [
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)