# import setuptools

# setuptools.setup(
#     include_package_data=True,
#     name='catlyst',
#     version='0.0.1',
#     description='catlyst Data Scraping Module',
#     url='https://github.com/limegurutech/examples/tree/main/python/pip%20installable%20package',
#     author='Bhupendra Singh Solanki',
#     author_email='Bhupsa.5550@gmail.com',
#     packages=setuptools.find_packages(),
#     install_requires=['python','scrapy'
#     ],
#     long_description='catlyst Data Scraping Module which scrap data of school data like teachers name, designation and contact detail.',
#     long_description_content_type="text/markdown",
#     classifiers=[
#         "Programming Language :: Python :: 3",
#          "Operating System :: OS Independent",
#     ],
# )

from setuptools import setup, find_packages

VERSION = '1'
DESCRIPTION = 'Extracting Data using scrapy framework'
long_description = 'A package that allows to extract data from a website which have information of schools and employees of schools '

# Setting up
setup(
    name="catlyst",
    version=VERSION,
    author="Bhupendra Singh Solanki",
    author_email="<bhupsa.5550@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['python', 'scrapy'],
    keywords=['python', 'data', 'school data', 'scraping'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
        # "Operating System :: Unix",
        # "Operating System :: MacOS :: MacOS X",
        # "Operating System :: Microsoft :: Windows",
    ]
)
