from setuptools import setup, find_packages

# setup(
#     name='Home work 2',
#     version='0.0.1',
#     description='I study Python',
#     author='Illia Yermolayev',
#     author_email='illeayermolayev@gmail.com',
#     url='https://github.com/Illia101/Home_work',
#     packages=find_packages(),
#     entry_points={
#         'console_scripts': [
#             'clean-folder = clean_folder.clean:main',
#         ],
#     },
# )
   

setup(
    name='clean_folder',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'clean-folder = clean_folder.clean:main',
        ],
    },
)