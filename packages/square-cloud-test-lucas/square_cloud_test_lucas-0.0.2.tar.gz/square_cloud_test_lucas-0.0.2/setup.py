from setuptools import setup

with open("README.md", "r") as file:
    readme = file.read()

setup(name='square_cloud_test_lucas',
    version='0.0.2',
    license='MIT License',
    author='Lucas Alves',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='lucasal072@gmail.com',
    keywords='square_cloud_lucas_test',
    description=u'Implementacao da api da square cloud não oficial',
    packages=['square_cloud'],
    install_requires=['requests'],)