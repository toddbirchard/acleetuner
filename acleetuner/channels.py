import simplejson as json


def get_channels():
    with open('channels.json') as fp:
        return json.load(fp)["result"]["channels"]
