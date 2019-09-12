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
## Rerun failures
```
python3 -m pytest src/spec/home_test.py:19 --app=android --reruns 1
```
## Parallel Test
```
python3 -m pytest src/spec/home_test.py --app=android -v -n2
```
## HTML Report
```
python3 -m pytest src/spec/*.py* --html=report/report.html
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
- [x] Locator strategy
- [x] Hooks (unittest)
- [x] Screenshot on failure
- [x] HTML report
- [x] Allure report
- [x] CLI arguments as a fixture (Pytest)
- [x] Logger
- [x] Runner (Pytest)
- [x] Runner percentage with style (Pytest)
- [x] Parallel Tests (Pytest) x2
- [x] Re-run failures (Pytest)