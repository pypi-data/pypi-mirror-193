from setuptools import setup, find_packages

VERSION = '0.0.3' 
DESCRIPTION = 'Sinhala Language Tool Kit'
LONG_DESCRIPTION = 'Sinhala Language Tool Kit'

# Setting up

# python setup.py sdist bdist_wheel
# python -m twine upload dist/*

setup(
       # the name must match the folder name 'sltk'
        name="sltkpy", 
        version=VERSION,
        author="Buddhi Kavindra Ranasinghe",
        author_email="info@buddhilive.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages
        # include_package_data=True,
        data_files=[('shared', ['sltkpy/shared/pre.txt', 'sltkpy/shared/abbr.json', 'sltkpy/shared/dict.json'])],
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Intended Audience :: Developers",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)