from setuptools import setup



classifiers = [
       'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System ::  Microsoft :: Windows :: Windows 10',
]


setup(
    name ='epydz',
    version='1.0.0',
    author='talbi mohamed',
    authors_nickname = "alexmm",
    author_email='monwin966@gmail.com',
    description='A Python library containing useful functions in the Algerian language.',
    long_description=open('README.md').read(),
    keywords = ["Algerian","language", "library", "useful", "functions"],
    classifiers=classifiers,
    license='MIT License',
    python_requires='>=3.0',
)

   

