from setuptools import find_packages, setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

VERSION = "1.0.0"
PACKAGE_NAME = "IREX"
INSTALL_REQUIRES = [
    "joblib>=1.1.0",
    "dice-ml>=0.8",
    "shap>=0.41.0",
    "lime>=0.2.0.1",
    "seaborn>=0.11.2",
    "pandas>=1.4.3",
    "matplotlib>=3.5.2",
    "matplotlib-inline>=0.1.3",
    "numpy>=1.16.0",
    "sklearn>=0.0",
    "explainerdashboard>=0.4.0",
    "imblearn>=0.0",
    "alibi>=0.7.0"
    ]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    install_requires=INSTALL_REQUIRES,
    packages=find_packages(),
    py_modules=["Funciones"],
    long_description=long_description,
    long_description_content_type='text/markdown'
    )