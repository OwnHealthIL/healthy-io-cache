from setuptools import setup

setup(
    name='HealthyIoCache',
    version='0.0.1',
    packages=['healthyiocache.redis', ],
    long_description='The Backend\'s wrapper for all cache operations',
    url='https://github.com/OwnHealthIL/healthy-io-cache',
    author='Liad',
    author_email='liad@healthy.io',
    python_requires='>=2.7, <4',
    classifiers=[
        'Development Status :: 5 - Production/Stable'
    ],
    install_requires=['redis==2.10.3'],
)
