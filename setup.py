from setuptools import setup, find_packages

setup(
    name='Upload',
    version='1.0.0',
    author='Veni kota',
    author_email='venichowdary1234@gmail.com',
    description='A module to upload files and Images to AWS S3 and Google Cloud Storage.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/VeniKota/upload/',
    packages=find_packages(),
    install_requires=[
        'boto3',
        'google-cloud-storage'
    ],
    
    python_requires='>=3.6',
)
