from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="edint_eyetracking",
    version="0.1.0",
    author="Edint",
    author_email="sonjuhy@edint.io",
    description="MediaPipe 기반의 시선 추적(Eye Tracking) 라이브러리",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/edint-Hub/eye-tracking",
    packages=find_packages(exclude=("tests", "examples")),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["opencv-python", "mediapipe", "numpy"],
    python_requires=">=3.8",
)
