from setuptools import setup, find_packages

setup(name='lymboy-lstm',
      version='v1.2',
      description='Some boxed time series forecasting model based lstm',
      url='https://github.com/lymboy',
      author='lymboy.com',
      author_email='liusairo@gmail.com',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
            'keras'
      ],
      zip_safe=True)
