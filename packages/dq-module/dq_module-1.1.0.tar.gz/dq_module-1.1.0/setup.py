# Databricks notebook source
import setuptools

# COMMAND ----------

setuptools.setup(
    name="dq_module",
    version="1.1.0",
    author="Sweta",
    author_email="sweta.swami@decisionpoint.in",
    description="data profiling and basic data quality rules check",
    # packages=setuptools.find_packages(include=['*']),
    packages=['dataqualitycheck', 'dataqualitycheck.datasources'],
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
    ],
    #.....assuming pyspark, pyarrow is preinstalled 
    install_requires=['polars'],
    python_requires='>=3.8',
)

# COMMAND ----------


