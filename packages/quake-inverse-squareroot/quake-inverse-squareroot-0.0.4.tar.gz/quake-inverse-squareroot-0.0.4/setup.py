
from setuptools import setup, Extension
import sys

extra_link_args = []
extra_compile_args = []

# Add debug symbols for Windows and Linux and darwin 

if sys.platform in ('win32','nt'):
    extra_link_args.append('/DEBUG')
    extra_compile_args.append('/Zi')
elif sys.platform in ('linux','linux2','darwin'):
    extra_compile_args.append('-g')
    extra_link_args.append('-g')

if not extra_link_args and not extra_compile_args:
    print("No extra arguments for linking or compiling. You may not see any symbols exported.")    

sqrt = Extension('quake_inverse_sq._sqrt', sources=['quake_inverse_sq/_sqrt.c'], extra_link_args=extra_link_args, extra_compile_args=extra_compile_args)

setup(
    name="quake-inverse-squareroot",
    version="0.0.4",
    description="A Python port from Quake 3's fast inverse square root algorithm",
    ext_modules=[sqrt],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/timelessnesses/quake-inverse-squareroot',
    packages=['quake_inverse_sq']
)