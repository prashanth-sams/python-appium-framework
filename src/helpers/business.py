import datetime
import pymysql
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


class dotdict(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__