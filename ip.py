from socket import socket, AF_INET, SOCK_DGRAM
from requests import get
from requests.exceptions import ConnectionError


ipify = {
    "ipv4": "https://api.ipify.org?format=json",
    "ipv6": "https://api64.ipify.org?format=json"
}

dns = ("8.8.8.8", 80)


def get_local_ip_address():
    """Get IP Address

    Returns
    -------
    string
        The IP address
    """
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(dns)
    return s.getsockname()[0]


def get_public_ip_address(ipv6=False):
    """Get Public IPv4 or IPv6 Address

    Arguments
    ---------
    boolean
        Search IPv6 public address

    Returns
    -------
    string
        The IP address
    """
    url = ipify["ipv4"] if not ipv6 else ipify["ipv6"]

    try:
        req = get(url)
        data = req.json()
    except ConnectionError as e:
        data = {"ip": "ConnectionError: {}".format(e.args[-1])}
    except Exception as e:
        data = {"ip": "Exception: {}".format(e.args[-1])}

    return data["ip"] if "ip" in data else ""
