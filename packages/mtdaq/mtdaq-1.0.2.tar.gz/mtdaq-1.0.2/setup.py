from setuptools import setup, find_packages

setup(
    name="mtdaq",
    version="1.0.2",
    description = "MangoTree DAQ Device",
    author="MangoTree",
    author_email = "support@mangotree.cn",
    url = "https://www.mangotree.cn/",
    packages=find_packages(),
    include_package_data=True,
    license = "MIT",
    zip_safe=True,
)