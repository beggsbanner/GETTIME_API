from setuptools import setup, find_packages

setup(
    name="gettime-api",
    version="1.0.0",
    author="Your Name",
    author_email="your-email@example.com",
    description="A Flask API with a Tkinter GUI for retrieving US time zones",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/beggsbanner/GETTIME_API",
    packages=find_packages(),
    install_requires=[
        "flask",
        "tkinter",  # Add any other dependencies from requirements.txt
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "gettime-api=GETTIMEAPI:main",  # Assuming GETTIMEAPI.py has a 'main()' function
        ]
    },
    python_requires=">=3.6",
)
