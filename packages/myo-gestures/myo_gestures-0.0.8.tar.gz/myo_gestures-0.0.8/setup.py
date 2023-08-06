from setuptools import setup, find_packages

VERSION = '0.0.8' 
DESCRIPTION = 'Myo Armband Gesture Classification'
LONG_DESCRIPTION = 'Package for real time gesture classification using the Myo Armband'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="myo_gestures", 
        version=VERSION,
        author="Allan Garcia",
        author_email="allang@u.northwestern.edu",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        scripts=['scripts/real_time.py','scripts/data_loader.py','scripts/train_net.py', 'scripts/transfer_learn.py'],
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)