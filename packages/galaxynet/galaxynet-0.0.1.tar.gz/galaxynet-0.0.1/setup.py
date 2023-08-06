from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Diffusion model for galaxy generation'
LONG_DESCRIPTION = 'Will update later'

# Setting up
setup(
        name="galaxynet", 
        version=VERSION,
        author="Matt Sampson",
        author_email="<matt.sampson@princeton.edu",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'diffusion'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
