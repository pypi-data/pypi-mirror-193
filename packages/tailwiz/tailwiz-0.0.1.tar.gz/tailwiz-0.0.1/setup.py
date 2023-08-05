from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='tailwiz',
    version='0.0.1',
    description='',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        'scikit-learn',
        'transformers',
        'evaluate',
        'pandas',
        'torch',
        'numpy',
    ],
    author='Timothy Dai',
    author_email='timdai@stanford.edu',
    url='https://github.com/timothydai/tailwiz', 
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    py_modules=['tailwiz'],
    package_dir={'': '.'},
)
