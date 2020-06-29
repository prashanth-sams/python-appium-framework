from src.helpers.business import notify_slack
from invoke import task


@task
def test(c, env='staging', lang='en', slack='on', app='android'):
    c.run(f'python3 -m pytest src/spec/{app}/login_test.py --app={app}')
    if slack == 'on': notify_slack()
