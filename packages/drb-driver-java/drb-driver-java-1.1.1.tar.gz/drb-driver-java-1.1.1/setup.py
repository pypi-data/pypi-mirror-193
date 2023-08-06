import versioneer
from setuptools import setup, find_namespace_packages
import os

HERE = os.path.relpath(os.path.dirname(os.path.abspath(__file__)))

with open('requirements.txt') as f:
    REQUIREMENTS = f.readlines()

with open('README.md') as fh:
    long_description = fh.read()

setup(
    name='drb-driver-java',
    packages=find_namespace_packages(include=['drb.*', 'drb_driver_java_jars']),
    description='DRB java driver',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='GAEL Systems',
    author_email='drb-python@gael.fr',
    url='https://gitlab.com/drb-python/impl/java',
    install_requires=REQUIREMENTS,
    setup_requires=['cython'],
    test_suite='tests',
    data_files=[('.', ['requirements.txt'])],
    package_dir={"drb_driver_java_jars": "drb_driver_java_jars"},
    package_data={"drb_driver_java_jars": ["*.jar"]},
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: "
        "GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.8',
    entry_points={
        'drb.driver': 'java = drb.drivers.java:DrbJavaFactory',
    },


    use_scm_version=True,
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    project_urls={
        'Documentation': 'https://drb-python.gitlab.io/impl/java',
        'Source': 'https://gitlab.com/drb-python/impl/java',
    }
)
