import requests


DEVELOPER = "Selcuk Cihan"


def remote_call():
    r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
    return r.status_code
