import netifaces


def get_mac_address(interface: str = None) -> str:
    if interface is None:
        interface = netifaces.interfaces()[0]

    mac = netifaces.ifaddresses(interface)[netifaces.AF_LINK][0]["addr"]        # type: str

    return mac


def get_formatted_mac_address(interface: str = None) -> int:
    mac = get_mac_address(interface)
    mac = mac.replace(":", "")
    return int(mac, 16)
