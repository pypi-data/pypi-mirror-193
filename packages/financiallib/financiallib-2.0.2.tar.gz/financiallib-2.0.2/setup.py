from setuptools import setup, find_packages

try:
    REQUIRES = list()
    f = open("requirements.txt", "rb")
    for line in f.read().decode("utf-8").split("\n"):
        line = line.strip()
        if "#" in line:
            line = line[: line.find("#")].strip()
        if line:
            REQUIRES.append(line)
except FileNotFoundError:
    print("'requirements.txt' not found!")
    REQUIRES = list()

url_path = ''

setup(name='financiallib',
      version = '2.0.2',
      license = f"Financial Services Ltd.{url_path}",
      author = "Neelakash Chatterjee",
      packages = find_packages(),
      install_requires = REQUIRES,
      description = "Financial-Lib: A Library for Financial Data Analysis and Pre-Processing.",
      )
