from setuptools import setup, find_packages

setup(
    name='daorion',
    version='0.1.0',
    description='My Python Package',
    author='daOrion',
    author_email='himangshu.biswas@daorion.com',
    url='https://github.com/SurjeetSingh2022/daorion_pdf_automation_version2',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
