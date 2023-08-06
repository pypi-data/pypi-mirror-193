from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Wigner quantum state and process tomography'
LONG_DESCRIPTION = 'Package for state and process tomography in the context of Wigner reprsentation for near term quantum devices.'

# Setting up
setup(
    name="DROPStomo",
    version=VERSION,
    author="Amit Devra, Dennis Huber, Niklas J. Glaser, Steffen J. Glaser",
    author_email="<amit.devra@tum.de>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=['DROPStomo', 'DROPStomo.WQST1Q', 'DROPStomo.WQST2Q', 'DROPStomo.WQPT1Q'],
    install_requires=['ipython','qiskit', 'matplotlib', 'scipy', 'plotly', 'numpy', 'pandas','mpl_toolkits'],
    keywords=['python', 'quantum physics', 'quantum computing', 'quantum information processing', 'quantum tomography', 'quantum state tomography', 'quantum process tomography', 'Wigner tomography'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
