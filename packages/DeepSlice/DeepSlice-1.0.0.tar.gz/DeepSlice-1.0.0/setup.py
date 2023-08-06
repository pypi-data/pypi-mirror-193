from distutils.core import setup
setup(
    name='DeepSlice',
    packages=['DeepSlice'],
    version='1.0.0',
    license='GPL-3.0',
    description='A package to align histology to 3D brain atlases',
    author='DeepSlice Team',
    author_email='harry.carey@medisin.uio.no',
    url='https://github.com/PolarBean/DeepSlice',
    download_url='https://github.com/PolarBean/DeepSlice/archive/refs/tags/1.0.tar.gz',
    keywords=['histology', 'brain', 'atlas', 'alignment'],
    install_requires=[
        'numpy',
        'scikit-learn',
        'scikit-image',
        'tensorflow==1.15.0',
        'typing',
        'pandas'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.7',
    ],

)   