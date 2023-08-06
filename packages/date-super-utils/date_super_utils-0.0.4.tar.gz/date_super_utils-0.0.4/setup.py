import setuptools


print('YOOO')
p = setuptools.find_packages()
print('FIND PACKAGES', p)

setuptools.setup(
    name='date_super_utils',
    version='0.0.4',
    author='Vladyslav Zadorozhnyi',
    description='Date utils',
    packages=p,
    include_package_data=True,
    author_email='zadorozhnyi.devback@gmail.com',
    license='MIT',
    install_requires=['babel', 'python-dateutil', 'pytz'],
)
