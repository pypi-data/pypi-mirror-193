# -*- coding:utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


setup(
    name="kimstockquant",
    version="1.0.3",
    packages=[
        "kimstockquant",
        "kimstockquant/source",
        "kimstockquant/utils"
    ],
    platforms="any",
    description="Professional quant framework",
    url="https://github.com/Gary-Hertel/StockQuant",
    author="mrkim",
    author_email="kim0201@gmail.com",
    license="MIT",
    keywords=[
        "kimstockquant", "quant", "framework"
    ],
    install_requires=[
        "numpy",
        "requests",
        "concurrent-log-handler",
        "colorlog",
        "pandas",
        "matplotlib",
        "tushare",
        "talib",
        "baostock",
        "finplot",
        "akshare",
        "easytrader"
    ]
)