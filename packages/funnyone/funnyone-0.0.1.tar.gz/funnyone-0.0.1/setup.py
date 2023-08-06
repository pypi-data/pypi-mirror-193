from setuptools import setup

setup(name='funnyone',
      version='0.0.1',
      description='The funnyone joke in the world',
      url='http://github.com/storborg/funnyone',
      author='Flying Circus',
      author_email='cdchinmoy@gmail.com',
      license='MIT',
      packages=['funnyone'],
      zip_safe=False,
      keywords = ['funny', 'funnyone', 'comedy'],
      install_requires=[ 
            'pandas',
            ],
      classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Build Tools',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
      ],)