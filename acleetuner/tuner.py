import requests
import time
from acleetuner import channel_list


def current_milli_time():
    return str(round(time.time() * 1000))


def get_channel_number(channel_name):
    try:
        channel = [channel for channel in channel_list if channel["channel"] == channel_name]
        return channel[0]['channelid']
    except IndexError as e:
        err_msg = f"{channel_name} wasn't found, but I found the following channels: \n"
        channel = [channel for channel in channel_list if channel_name.lower() in channel["channel"].lower()]
        for name in channel:
            err_msg += (name["channel"]+"\n")
        print(err_msg)
        print(e)
    except Exception as e:
        print(f"OH SHIT SOMETHING WENT WRONG: {e}")


def tuner(channel_name):
    """name goes here, ex: tuner(`Cartoon Network`)"""
    channel_number = get_channel_number(channel_name)
    headers = {
        'Connection': 'keep-alive',
        'Authorization': 'Basic base64_username:password',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'DNT': '1',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
        'Content-Type': 'application/json',
        'Origin': 'http://remoteurl:port',
        'Referer': 'http://remoteurl:port/',
        'Accept-Language': 'en-US,en;q=0.9',
        'sec-gpc': '1',
    }
    data = '{"jsonrpc":"2.0","method":"Player.Open","params":{"item":{"channelid":'+channel_number+'}},"id":'+current_milli_time()+'}'
    requests.post(
        'http://remoteurl:port/jsonrpc',
        headers=headers,
        data=data,
        verify=False
    )
    return f"Tuning to {channel_name} ({channel_number})"
