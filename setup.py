from setuptools import setup, find_packages

setup(
    name='iron-bracken',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'cryptography>=41.0.0',
        'scapy>=2.5.0',
        'pyyaml>=6.0',
        'requests>=2.31.0',
    ],
    entry_points={
        'console_scripts': [
            'bracken=iron_bracken.cli:main',
        ],
    },
)
