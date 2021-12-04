from setuptools import setup

if __name__ == "__main__":
    try:
        setup()
    except Exception as e:
        print(
            f"Exception occurred:  {e}"
            "please ensure you have the right version of python and the most updated version of setuptools and wheels"
            "python --version"
            "pip install wheel setuptools"
        )
        raise
