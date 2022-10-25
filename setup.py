from distutils.core import setup
setup(
  name = 'Data_Stats',
  packages = ['Data_Stats'],
  version = '0.1',
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'This library consists of obtaining data from an open database "statsbombpy".',
  author = 'Iñigo Ugarte & Paulo Cagigal',
  author_email = 'paulo.cagigal@alumni.mondragon.edu',
  url = 'https://github.com/pauloo1010/Paulo-Inigo-Progra',
  download_url = 'https://github.com/pauloo1010/Paulo-Inigo-Progra/archive/refs/tags/v_01.tar.gz',
  keywords = ['Dataset', 'Easy-working', 'Open'],
  install_requires=[
          'pandas',
          'statsbombpy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha', 
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.10.6'
  ],
)