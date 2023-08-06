from setuptools import setup, find_packages


VERSION = "0.0.4"
DESCRIPTION = "Python API to upload data to ILVO's minio server"

setup(
    name="minilvo",
    version=VERSION,
    author="Lorenzo Mogicato",
    author_email="<lorenzo.mogicato@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["minio", "pillow", "pydantic"],
    # keywords=['tag1test', 'lollo', '3rdtag'],
    # classifiers=[
    #     "Development Status :: 1 - Planning",
    #     # "Intended Audience :: ILVOTeam",
    #     "Programming Language :: Python :: 3",
    #     "Operating System :: Unix",
    #     "Operating System :: MacOS :: MacOS X",
    #     "Operating System :: Microsoft :: Windows",
    # ]
)
