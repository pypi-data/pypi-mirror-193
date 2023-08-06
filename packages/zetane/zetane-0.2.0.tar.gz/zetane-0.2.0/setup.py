from setuptools import setup, find_packages

setup(
    name = "zetane",
    author="Zetane Systems",
    author_email="info@zetane.com",
    description = "Zetane Protector API",
    long_description="""Zetane Protector API is an automated platform for testing and improving the robustness of machine learning models and their data. It provides data scientists and operators with insights into proposed machine learning solutions and helps validate, understand, and analyze the operational boundaries of machine learning data and models prior to deployment.\n\nVisit our [docs](https://docs.zetane.com) for more details.""",
    long_description_content_type="text/markdown",
    version = "0.2.0",
    license="LICENSE.md",
    url="https://zetane.com",
    packages=find_packages(include=('protector.*','zetane')),
    entry_points = {
        'console_scripts': [
            'zetane = zetane.__main__:main'
        ]
    },
    python_requires='>=3.7',
    install_requires = ['python-dotenv', 'tqdm', 'requests', 'numpy'],
    include_package_data=True,
    package_data={'zetane': ['*.json']},)
