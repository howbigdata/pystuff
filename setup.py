import setuptools

setuptools.setup(
    name="python playground",
    version="1.0.0",
    description="whatever",
    packages=setuptools.find_packages("src"),
    package_dir={'':'src'},
    install_requires=[
          'pytest',
])
