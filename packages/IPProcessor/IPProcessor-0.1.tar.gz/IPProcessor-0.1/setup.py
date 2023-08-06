from distutils.core import setup
setup(
  name = 'IPProcessor',         # How you named your package folder (MyLib)
  packages = ['IPProcessor'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Process any image and replaces each color to it is more similar from a selected palette',   # Give a short description about your library
  author = 'Jesús Guillén',                   # Type in your name
  author_email = 'jesus.guilleny@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/JGuillenY/ImagePixelProcessor',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/JGuillenY/ImagePixelProcessor/archive/refs/tags/0.1.tar.gz',    # I explain this later on
  keywords = ['PIXEL', 'IMAGE', 'PROCESSOR', 'PNG'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pillow',
          'numpy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
)