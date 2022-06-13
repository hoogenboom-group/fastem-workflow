from setuptools import setup

DISTNAME = "fastem-workflow"
DESCRIPTION = "Post-processing workflow for FAST-EM data."
MAINTAINER = "Arent Kievits"
MAINTAINER_EMAIL = "a.j.kievits@tudelft.nl"
LICENSE = "LICENSE"
URL = "https://github.com/hoogenboom-group/FAST-EM_workflow"
VERSION = "0.1.dev"
PACKAGES = [
    "fastemworkflow",
]
INSTALL_REQUIRES = [
    "beautifulsoup4",
    "matplotlib",
    "numpy",
    "pandas",
    "render-python",
    "scipy",
    "scikit-image",
    "seaborn",
    "shapely",
    'icat-workflow @ git+https://github.com/hoogenboom-group/iCAT-workflow.git'
]

if __name__ == '__main__':

    setup(
        name=DISTNAME,
        version=VERSION,
        author=MAINTAINER,
        author_email=MAINTAINER_EMAIL,
        packages=PACKAGES,
        include_package_data=True,
        url=URL,
        license=LICENSE,
        description=DESCRIPTION,
        long_description=open("README.md").read(),
        install_requires=INSTALL_REQUIRES,
    )
