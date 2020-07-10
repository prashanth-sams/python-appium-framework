# Python Appium Framework
[![Build Status](https://travis-ci.org/prashanth-sams/python-appium-framework.svg?branch=master)](https://travis-ci.org/prashanth-sams/python-appium-framework)
> Complete Python Appium framework in 360 degree 

## Features
- [x] Locator strategy
- [x] Hooks (unittest)
- [x] Helper methods
- [x] Database connectivity + SSH Tunneling
- [x] Screenshot on failure
- [x] Handle local storage
- [x] Bash Runner
- [x] Slack notify
- [x] Define environment variable
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
- [x] Test script validation

## Installation
Install python libraries

    pip3 install -r requirements.txt

## Test Runner

| Action         | Command            |
| -------------- | ---------          |
| Bash runner    | `bash runner/android/smoke_run.sh` |
| Default        | `python3 -m pytest src/spec/* --app=android` |
| Rerun failures | `python3 -m pytest src/spec/home_test.py --app=android --reruns 1` |
| Parallel Test  | `python3 -m pytest src/spec/home_test.py --app=android -v -n2` |

## Test Report
| Type           | Command            |
| -------------- | ---------          |
| HTML Report    | `python3 -m pytest src/spec/*.py --html=report/report.html` |
| JSON Report    | `python3 -m pytest src/spec/*.py --json=report/json/report.json` |
| Allure Report    | `python3 -m pytest src/spec/* --alluredir=report` |

- Download allure commandline 
https://github.com/allure-framework/allure2/releases

>  generate allure report
```
allure serve report/
```

![](https://i.imgur.com/u7lBA0x.png)