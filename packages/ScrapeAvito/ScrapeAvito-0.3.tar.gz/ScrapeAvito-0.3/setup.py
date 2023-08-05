from setuptools import setup

setup(
    name='ScrapeAvito',
    version='0.3',
    packages=[r'C:\Users\Amine Lahouani\Desktop\infomineo_web_scraping_tool_v3'],
    install_requires=[
        'numpy',
        'pandas',
        'requests',
        'pyfiglet'
    ],
    entry_points={
        'console_scripts': [
            'ScrapeAvito = ScrapeAvito:main'
        ]
    }
)

