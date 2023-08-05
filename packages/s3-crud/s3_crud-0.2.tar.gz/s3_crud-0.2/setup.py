from setuptools import setup, find_packages
setup(
   name='s3_crud',
   version='0.2',
   packages=find_packages(),
   install_requires=[
       'boto3',
       'os',
       'logging',
       'robot.libraries.BuiltIn',
       'dotenv'
   ]
   
)