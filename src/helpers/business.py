import datetime
import pymysql
import requests
import json
from sshtunnel import SSHTunnelForwarder


def subtract_days(days=7):
    return datetime.date.today() - datetime.timedelta(days)


def past_day_with_double_subtraction(first_check_day, second_check_day):
    return (subtract_days(first_check_day) - datetime.timedelta(second_check_day)).strftime("%d")


def roi_weekly_header(first_check_day, second_check_day):
    return str(past_day_with_double_subtraction(first_check_day, second_check_day) + ' - ' + subtract_days(
        first_check_day).strftime("%d-%b-%Y").replace('-', ' '))


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


def notify_slack(self):
    """
    modify web_hook_url with apt data
    """
    web_hook_url = 'https://hooks.slack.com/services/xxxxxxx/xxxxxxx/xxxxxxxxxxxxxxxx'
    slack_msg = {
        "attachments": [
            {
                "fallback": "Required plain-text summary of the attachment.",
                "color": "#36a64f",
                # "pretext": "Optional text that appears above the attachment block",
                "author_name": "Mobile Automation Results",
                "author_link": "https://twitter.com/prashanthsams",
                "author_icon": "https://avatars3.githubusercontent.com/u/2948696?s=460&v=4",
                "title": "Lead Tracker - Android",
                "title_link": "https://twitter.com/prashanthsams",
                "text": "Optional text",
                "fields": [
                    {
                        "title": f"AE => :white_check_mark: {str(4)} Passed :exclamation: {str(0)} Failed",
                        # "value": "3",
                        "short": False
                    },
                    {
                        "title": f"SA => :white_check_mark: {str(6)} Passed :exclamation: {str(0)} Failed",
                        "short": False
                    }
                ],
                "image_url": "http://my-website.com/path/to/image.jpg",
                "thumb_url": "http://example.com/path/to/thumb.png",
                "footer": "Property Finder",
                "footer_icon": "https://platform.slack-edge.com/img/default_application_icon.png",
                "ts": int(datetime.datetime.now().strftime("%s"))
            }
        ]
    }
    requests.post(web_hook_url, data=json.dumps(slack_msg))


class dotdict(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__