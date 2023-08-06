from setuptools import setup, Extension

with open("README.md", "r") as fh:
    long_description = fh.read()

extras_nds=["ndspy", "crcmod"]
extras_armips=["pyarmips"]
extras_xdelta=["pyxdelta"]
extras_iso=["pycdlib", "pymkpsxiso"]
extras_ips=["ips_util"]
extras_graphics=["Pillow", "psd-tools>=1.8,<1.9"]

setup(
    name="hacktools",
    version="0.27.4",
    author="Illidan",
    description="A set of utilities and tools for rom hacking and translations.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Illidanz/hacktools",
    packages=["hacktools"],
    ext_modules=[
        Extension("hacktools.cmp_lzss", sources=["hacktools/c_ext/cmp_lzss.c"]),
        Extension("hacktools.cmp_misc", sources=["hacktools/c_ext/cmp_misc.c"]),
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "click",
        "tqdm",
    ],
    extras_require = {
        "nds": extras_nds,
        "armips": extras_armips,
        "xdelta": extras_xdelta,
        "graphics": extras_graphics,
        "iso": extras_iso,
        "ips": extras_ips,
        "all": extras_nds + extras_armips + extras_xdelta + extras_iso + extras_ips + extras_graphics,
    },
    python_requires=">=3.7",
)
