from distutils.core import setup
setup(
  name = 'SCHLOADER',         # How you named your package folder (MyLib)
  packages = ['SCHLOADER'],   # Chose the same as "name"
  version = '0.1.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Library to upload SAP downloaded file into a DB',   # Give a short description about your library
  author = 'Michael Huwiler',                   # Type in your name
  author_email = 'michael.huwiler@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/mikehummell/schloader',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/mikehummell/schloader/archive/v0.1.1.tar.gz',    # I explain this later on
  keywords = ['BI', 'SQL', 'Alchemy'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pandas',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package

    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',

    'License :: OSI Approved :: MIT License',   # Again, pick a license

    'Programming Language :: Python :: 3.5',    #Specify which pyhton versions that you want to support
  ],
)