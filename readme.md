# Python Appium Framework
[![Build Status](https://travis-ci.org/prashanth-sams/python-appium-framework.svg?branch=master)](https://travis-ci.org/prashanth-sams/python-appium-framework)

## Pre-requisites
```
pip3 install -r requirements.txt
```
## Runner
```
python3 -m pytest src/spec/* --app=android
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
## HTML Report
```
python3 -m pytest src/spec/*.py* --html=report/report.html
```
## Support
- [x] Locator strategy
- [x] Hooks (unittest)
- [x] Screenshot on failure
- [x] HTML report
- [x] Allure report
- [x] CLI arguments as a fixture (Pytest)
- [x] Runner (Pytest)