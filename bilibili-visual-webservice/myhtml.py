import requests


def getRequestsContentUtf8(url, referee=""):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        'Referer': referee
    }
    return requests.get(url, headers=headers).content.decode("utf-8")


def getRequestsText(url, referee=""):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        'Referer': referee
    }
    return requests.get(url, headers=headers).text


def getRequestsContent(url, referee=""):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        'Referer': referee
    }
    return requests.get(url, headers=headers).content