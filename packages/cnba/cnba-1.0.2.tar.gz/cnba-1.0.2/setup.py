from setuptools import find_packages, setup

setup(
    name="cnba",
    version='1.0.2',
    author = 'Ayushman Kumar Banerjee',
    author_email = 'ayushmaan.banerjee@gmail.com',
    url = 'https://github.com/namhsuya/cnba/',
    packages=find_packages(),
    install_requires=[
        'click',
        'pandas',
        'statsmodels',
        'scipy',
        'console_logging',
        'tqdm'
    ],
    entry_points='''
    [console_scripts]
    cnba=cnba.__main__:main
    '''

)