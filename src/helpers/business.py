import datetime
import pymysql
import requests
import json
import random
from sshtunnel import SSHTunnelForwarder
from settings import *


def db(query):
    with SSHTunnelForwarder(
            ('<remote-host>', 22),
            ssh_username="<remote-username>",
            ssh_pkey="/Users/prashanth/.ssh/id_rsa",
            remote_bind_address=('<db-host>', 3306)
    ) as tunnel:
        conn = pymysql.connect(host='127.0.0.1', user='<username>', password='<passwd>', db='<dbname>',
                               port=tunnel.local_bind_port)
        cur = conn.cursor()
        cur.execute(query)
        conn.close()
        return get_db_results(cur)


def get_db_results(db_cursor):
    desc = [d[0] for d in db_cursor.description]
    results = [dotdict(dict(zip(desc, res))) for res in db_cursor.fetchall()]
    return results


def notify_slack():
    """
    modify web_hook_url with apt data
    """
    web_hook_url = f'https://hooks.slack.com/services/{SLACK_TOKEN}'

    with open("./report/json/report.json") as json_file:
        json_object = json.load(json_file)
        json_file.close()

    passed = int(status_count(json_object, 'passed'))
    failed = int(status_count(json_object, 'failed'))
    color = '#36a64f' if failed == 0 else '#a30001'
    text = "#Build Passed" if failed == 0 else "#Build Failed"

    slack_msg = {
        "attachments": [
            {
                "fallback": "Excuse Me! I've something for you!",
                "color": f"{color}",
                "pretext": f"@here {quote()}",
                "author_name": "Mobile Automation Results",
                "author_link": "https://twitter.com/prashanthsams",
                "author_icon": "https://avatars3.githubusercontent.com/u/2948696?s=460&v=4",
                "title": "Your App - Android",
                "title_link": "https://twitter.com/prashanthsams",
                "text": f"{text}",
                "fields": [
                    {
                        "title": f"AE => :white_check_mark: {str(passed)} Passed :exclamation: {str(failed)} Failed",
                        # "value": "3",
                        "short": False
                    },
                    {
                        "title": f"SA => :white_check_mark: {str(passed)} Passed :exclamation: {str(failed)} Failed",
                        "short": False
                    }
                ],
                "image_url": "http://my-website.com/path/to/image.jpg",
                "thumb_url": "http://example.com/path/to/thumb.png",
                "footer": "Appium Framework",
                "footer_icon": "https://platform.slack-edge.com/img/default_application_icon.png",
                "ts": int(datetime.datetime.now().strftime("%s"))
            }
        ]
    }
    requests.post(web_hook_url, data=json.dumps(slack_msg))


def quote():
    quotes = [
        "Tests without assertions are not tests - Prashanth Sams",
        "In God we Trust for the rest we Test"
    ]
    return random.choice(quotes)


def status_count(json_object, status):
    try:
        return json_object['report']['summary'][f'{status}']
    except KeyError as e:
        try:
            return json_object['data'][0]['attributes']['summary'][f'{status}']
        except KeyError as e:
            return 0


class dotdict(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__