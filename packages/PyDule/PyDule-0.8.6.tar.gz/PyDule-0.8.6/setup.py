from setuptools import setup
import setuptools

with open('README.md','r') as fh:
	long_description = fh.read()

setup(
	name='PyDule',
	version='0.8.6',
	description='It Creates List,Tuple,Set,Dictionary in One Command,It gives Weather Information,It opens any App and File,It has Color Picker,It Plays Songs and More',
	author='Tamil Mutharasan',
	long_description=long_description,
	long_description_content_type='text/markdown',
	packages=setuptools.find_packages(),
	keywords=['python','PyDule','Module','Pydule','pydule','weather','list','tuple','set','dictionary','clear','color','pick_color','open','app','search','play','mp3','song','restart','system','shutdown','date','time','text_to_speech','text','speech'],
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Intended Audience :: Education",
		"Operating System :: Microsoft :: Windows :: Windows 10",
		"Development Status :: 5 - Production/Stable"
	],
	python_requires='>=3.10.7',
	py_modules=['PyRex'],
	package_dir={'':'src'},
	install_requires=[
		'beautifulsoup4',
		'pyttsx3',
		'pywhatkit',
		'playsound',
		'datetime',
		'requests',
		'AppOpener'
	]

)