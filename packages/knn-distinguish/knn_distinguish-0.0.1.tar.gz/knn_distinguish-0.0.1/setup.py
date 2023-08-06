from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'In traditioanl knn, the model trys its best to classify the object even though there is no fit class. Our model introduces a p-value to help the machine learns whether the object actually fit the existing classes or not'
setup(
    name='knn_distinguish',
    packages=find_packages(include=['knn_distinguish']),
    version=VERSION,
    description=DESCRIPTION,
    author='Wayne Hayes, Jingcheng Li',
    license='MIT',
    install_requires=[],
    # setup_requires=['pytest-runner'],
    # tests_require=['pytest==4.4.1'],
    # test_suite='tests',
    keywords=['python', 'knn', 'p value'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)