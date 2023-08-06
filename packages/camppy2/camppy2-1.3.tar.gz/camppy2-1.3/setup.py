from setuptools import setup, find_packages
import camppy2
setup(
    name="camppy2",
    version=camppy2.__version__,
    author=camppy2.__author__,
    author_email="contactcampsmm@gmail.com",
    description="CXMP MODULE",
    packages=['camppy2', 'camppy2'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "requests",
        "user_agent",
    ],
)
