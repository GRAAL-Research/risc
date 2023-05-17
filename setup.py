import glob
import os
import subprocess

from setuptools import setup, find_packages

current_file_path = os.path.abspath(os.path.dirname(__file__))


def get_readme():
    readme_file_path = os.path.join(current_file_path, "README.md")
    with open(readme_file_path, "r", encoding="utf-8") as f:
        return f.read()


def get_version():
    version_file_path = os.path.join(current_file_path, "version.txt")
    with open(version_file_path, "r", encoding="utf-8") as f:
        version = f.read().strip()

    try:
        sha = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode("ascii").strip()
    except Exception:  # pylint: disable=broad-except
        sha = "Unknown"

    if os.getenv("RISC_RELEASE_BUILD") != "1":
        version += ".dev1"
        if sha != "Unknown":
            version += "+" + sha[:7]
    return version


def write_version_python_file(version):
    version_python_file = os.path.join(current_file_path, "risc_generator", "version.py")
    with open(version_python_file, "w", encoding="utf-8") as f:
        f.write(f"__version__ = {repr(version)}\n")


def main():
    readme = get_readme()

    version = get_version()
    print("Building version", version)
    write_version_python_file(version)

    packages = find_packages()
    setup(
        name="risc_generator",
        version=version,
        author="David Beauchemin",
        author_email="david.beauchemin.5@ulaval.ca",
        download_url="https://github.com/GRAAL-Research/risc/archive/v" + version + ".zip",
        license="LGPLv3",
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Intended Audience :: Education",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Topic :: Software Development :: Libraries",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Topic :: Scientific/Engineering",
            "Topic :: Scientific/Engineering :: Artificial Intelligence",
        ],
        packages=packages,
        data_files=[("resources", glob.glob('*/*/*.pkl'))],
        include_package_data=True,
        python_requires=">=3.8",
        description="RISC, an open-source Python package data generator. RISC generates look-alike automobile "
        "insurance contracts based on the Quebec regulatory insurance form in French and English.",
        long_description=readme,
        long_description_content_type="text/markdown",
    )


if __name__ == "__main__":
    main()
