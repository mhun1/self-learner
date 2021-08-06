from setuptools import setup, find_packages

setup(
  name = 'TODO',
  packages = find_packages(exclude=['examples']),
  version = '0.0.0',
  license='MIT',
  description = 'TODO',
  author = 'Manuel Hun',
  author_email = 'hunmanu2@aol.com',
  url = 'https://github.com/mhun1/TODO',
  keywords = [
    'artificial intelligence',
    'attention mechanism',
    'image recognition'
  ],
  install_requires=[
    'einops>=0.3',
    'torch>=1.6',
    'torchvision'
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)
