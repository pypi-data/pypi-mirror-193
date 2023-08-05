from setuptools import setup, find_packages

setup(
    name='replicate_api_utils',
    version='0.1.4',
    author='Julian Otto',
    author_email="julianotto@outlook.com",
    description='Python package for accessing the Replicate API',
    packages=find_packages(),
    install_requires=[
        'click',
        'replicate',
        'tqdm',
    ],
    entry_points={
        "console_scripts": [
            "whisper=replicate_api_utils.whisper.cli:main"
        ]
    },
)
