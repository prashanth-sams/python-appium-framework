# Python Appium Framework
[![Build Status](https://travis-ci.org/prashanth-sams/python-appium-framework.svg?branch=master)](https://travis-ci.org/prashanth-sams/python-appium-framework)

## Pre-requisites
```
pip3 install -r requirements.txt
```
## Runner
```
python3 -m pytest src/spec/*
```
## Allure Report
- Download allure commandline 
https://github.com/allure-framework/allure2/releases

> runner
```
python3 -m pytest src/spec/* --alluredir=report
```
>  generate report
```
allure serve report/
```
## Support
- [x] Page Objects
- [x] Screenshot on failure
- [x] Allure report