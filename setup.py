from setuptools import setup, find_packages

setup(
    name='eduautoml',
    version='0.1.0',
    author='Diksha Wagh',
    author_email='waghdiksha935@gmail.com',  # (Optional) Update before PyPI
    description='🎓 A beginner-friendly AutoML library for students and educators.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Diksha-3905/eduAutoML',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'matplotlib',
        'typer[all]',
        'gradio'
    ],
    entry_points={
        'console_scripts': [
            'eduautoml=CLI.cli:app',  # CLI: eduautoml run input.csv target
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Education',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Education',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.7',
)
