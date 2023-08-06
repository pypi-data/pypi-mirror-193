from setuptools import setup, find_packages
from torch.utils.cpp_extension import BuildExtension, CUDAExtension


ext_modules = [
    CUDAExtension(
        "megablocks_ops",
        ["csrc/ops.cu", "csrc/binned_scatter.cu"],
        include_dirs = ["csrc"],
        extra_compile_args={
            "cxx": ["-fopenmp"],
            "nvcc": [
                "--ptxas-options=-v",
                "--optimize=2",
                "--generate-code=arch=compute_80,code=sm_80"
            ]
        })
]


setup(
    name="megablocks",
    version="0.0.2",
    author="Trevor Gale",
    author_email="tgale@stanford.edu",
    description="MegaBlocks",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/stanford-futuredata/megablocks",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: Unix",
    ],
    packages=find_packages(),
    ext_modules=ext_modules,
    cmdclass={"build_ext": BuildExtension},
    install_requires=["absl-py", "numpy", "torch", "stanford-stk"],
)
