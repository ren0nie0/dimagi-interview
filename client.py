import requests


class Dimagi_Client:
    def run(self):
        url = 'https://www.commcarehq.org/a/data-engineer-interview/api/v0.5/case/?type=patient&format=json'
        r = requests.get(url, auth=('mr.brian.rennie@gmail.com', '#######'))
        return r.json()


