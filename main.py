#!/usr/bin/env python3

from ip import get_public_ip_address, get_local_ip_address


def main():
    messages = [
        { "label": "Local IP address","value": get_local_ip_address() },
        { "label": "Public IPv4 address","value": get_public_ip_address() },
        { "label": "Public IPv6 address","value": get_public_ip_address(ipv6=True) }
    ]

    maxLen = 0
    lines = []

    for message in messages:
        line = message["label"] + "\t | \t" + message["value"]
        l = len(line)

        if l > maxLen:
            maxLen = l + 8  # 8 = \t * 2

        lines.append(line)

    separator = "-" * maxLen
    print(separator)

    for line in lines:
        print(line)
        print(separator)


if __name__ == "__main__":
    main()
