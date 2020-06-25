# Python Appium Framework
[![Build Status](https://travis-ci.org/prashanth-sams/python-appium-framework.svg?branch=master)](https://travis-ci.org/prashanth-sams/python-appium-framework)
> Complete Python Appium framework in 360 degree 

## Features
- [x] Locator strategy
- [x] Hooks (unittest)
- [x] Helper methods
- [x] Database connectivity + SSH Tunneling
- [x] Screenshot on failure
- [x] HTML report
- [x] JSON report
- [x] Allure report
- [x] CLI arguments as a fixture (Pytest)
- [x] In-house data storage
- [x] Logger
- [x] Runner (Pytest)
- [x] Runner percentage with style (Pytest)
- [x] Parallel Tests (Pytest) x2
- [x] Re-run failures (Pytest)

## Installation
Install python libraries

    pip3 install -r requirements.txt

## Test Runner
> Default
```shell script
python3 -m pytest src/spec/* --app=android
```
> Rerun failures
```shell script
python3 -m pytest src/spec/home_test.py --app=android --reruns 1
```
> Parallel Test
```shell script
python3 -m pytest src/spec/home_test.py --app=android -v -n2
```

## Test Report
#### HTML Report
    python3 -m pytest src/spec/*.py --html=report/report.html
#### JSON Report
    python3 -m pytest src/spec/*.py --json=report/json/report.json
#### Allure Report
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

![](https://i.imgur.com/q4rKprd.png)