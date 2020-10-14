# Python Appium Framework
> Complete Python Appium framework in 360 degree 

## Features
- [x] Locator strategy
- [x] Hooks (unittest)
- [x] Helper methods
- [x] Database connectivity + SSH Tunneling
- [x] Screenshot on failure
- [x] Docker support for Android
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

#### Docker Run
> Android test - x1 run
```shell script
docker run --privileged -d -p 6080:6080 -p 4723:4723 -p 5554:5554 -p 5555:5555 \ 
-v $(pwd)/data/apps/Android-NativeDemoApp-0.2.1.apk:/root/tmp/Android-NativeDemoApp-0.2.1.apk \
-e DEVICE="Samsung Galaxy S9" -e APPIUM=true --name android-container \
budtmo/docker-android-x86-11.0
```
**noVnc interface:** http://localhost:6080

## Test Report
| Type           | Command            |
| -------------- | ---------          |
| HTML Report    | `python3 -m pytest src/spec/android/*.py --html-report=report/report.html --app=android` |
| JSON Report    | `python3 -m pytest src/spec/android/*.py --json=report/json/report.json --app=android` |
| Allure Report    | `python3 -m pytest src/spec/android/* --alluredir=report --app=android` |

- Download allure commandline 
https://github.com/allure-framework/allure2/releases

>  generate allure report
```
allure serve report/
```

## Wrapper Methods
| Methods                  | Usage                                                                  |
| --------------           | ---------                                                              |
| element                  | `App.element(self, locator)`                                           |
| elements                 | `App.elements(self, locactor)`                                         |
| is_displayed             | `App.is_displayed(self, locator)`                                      |
| is_displayed > elements  | `App.is_displayed(self, locator, index=0)`                             |
| is_exist                 | `App.is_exist(self, locator)`                                          |
| is_exist > elements      | `App.is_exist(self, locator, index=0)`                                 |
| tap                      | `App.tap(self, locator)`                                               |
| tap > elements           | `App.tap(self, locator, index=0)`                                      |
| double_tap               | `App.double_tap(self, locator)`                                        |
| double_tap > elements    | `App.double_tap(self, locator, index=0)`                               |
| click                    | `App.click(self, locator)`                                             |
| click > elements         | `App.click(self, locator, index=0)`                                    |
| swipe                    | `App.swipe(self, start=locator, dest=locator)`                         |
| swipe > elements         | `App.swipe(self, start=(locator, 2), dest=(locator, 1))`               |
| send_keys                | `App.send_keys(self, locator, 'text')`                                 |
| send_keys > elements     | `App.send_keys(self, locator, 'text', index=0)`                        |
| get_screen_size          | `App.get_screen_size(self)`                                            |
| back                     | `App.back(self)`                                                       |
| close                    | `App.close(self)`                                                      |
| reset                    | `App.reset(self)`                                                      | 
| launch_app               | `App.send_keys(self, locator, 'text'`                                  | 
| tap_by_coordinates       | `App.tap_by_coordinates(self, x=338, y=204)`                           |
| assert_text              | `App.assert_text(self, 'actual', 'expected')`                          |
| assert_text > elements   | `App.assert_text(self, 'actual', 'expected', index=0)`                 |
| assert_size              | `App.assert_size(self, locator, 'more than 1')`                        |
|                          | `App.assert_size(self, locator, 'greater than 1')`                     |
|                          | `App.assert_size(self, locator, 'above 1')`                            |
|                          | `App.assert_size(self, locator, '> 1')`                                |
|                          | `App.assert_size(self, locator, 'less than 1')`                        |
|                          | `App.assert_size(self, locator, 'below 1')`                            |
|                          | `App.assert_size(self, locator, '< 1')`                                |
|                          | `App.assert_size(self, locator, 'equal to 1')`                         |
|                          | `App.assert_size(self, locator, '== 1')`                               |
| assert_boolean           | `App.assert_boolean(True, True)`                                       |
| swipe_until              | `App.swipe_until(self, locator, start_x=144, start_y=434, count=20)`   |

![](https://i.imgur.com/5vjklOb.png)