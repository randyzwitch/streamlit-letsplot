import setuptools

setuptools.setup(
    name="streamlit-letsplot",
    version="0.0.2",
    author="Randy Zwitch",
    author_email="randy@streamlit.io",
    description="Streamlit component for Lets Plot visualization library",
    long_description="Streamlit component for Lets Plot visualization library",
    long_description_content_type="text/plain",
    url="https://github.com/randyzwitch/streamlit-letsplot",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=["streamlit >= 0.63", "lets-plot >= 2.0.0"],
)
