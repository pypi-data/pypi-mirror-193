from setuptools import setup, find_packages,Distribution
# 若Discription.md中有中文 須加上 encoding="utf-8"
#with open("Discription.md", "r",encoding="utf-8") as f:
#    long_description = f.read()
    
class BinaryDistribution(Distribution):
    def has_ext_modules(self):
        return True
setup(
    name = "cathay_trade",
    version = "1.0.5",
    author = "pei-jan",
    author_email="orangepower856@hotmail.com",
    description="call trade function",
    packages=find_packages(),
    install_requires=['pythonnet'],
    package_data={'cathay_trade': ['dll/CSAPIComm.dll','dll/CSTrader.dll','dll/ICSharpCode.SharpZipLib.dll','dll/Interop.CGCAPIATLLib.dll','dll/Interop.FSCAPIATLLib.dll']},
    distclass=BinaryDistribution
    #license=
    #long_description=long_description,
    #long_description_content_type="text/markdown",
    #url="https://github.com/seanbbear/VerdictCut",                                         packages=setuptools.find_packages(),     
    #classifiers=[
    #    "Programming Language :: Python :: 3",
    #    "License :: OSI Approved :: MIT License",
    #    "Operating System :: OS Independent",
    #],
    #python_requires='>=3.6'
    )