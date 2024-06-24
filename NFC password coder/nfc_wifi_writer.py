import nfc
import ndef

def encode_wifi_config(ssid, password, auth_type='WPA'):
    """
    Encodes WiFi configuration data in the NDEF format for NFC.
    :param ssid: WiFi SSID
    :param password: WiFi Password
    :param auth_type: Authentication type (WPA or WEP)
    :return: NDEF message
    """
    wifi_data = f"WIFI:T:{auth_type};S:{ssid};P:{password};;"
    return ndef.UriRecord(f"wifi:{wifi_data}")

def write_to_nfc_tag(ssid, password):
    clf = nfc.ContactlessFrontend('usb')
    if not clf:
        raise RuntimeError("Failed to open NFC device.")

    ndef_message = encode_wifi_config(ssid, password)

    def connected(tag):
        if tag.ndef:
            tag.ndef.records = [ndef_message]
            print("WiFi credentials written to NFC tag successfully.")
        else:
            print("NFC tag is not NDEF formatted.")
        return True

    try:
        clf.connect(rdwr={'on-connect': connected})
    finally:
        clf.close()

if __name__ == "__main__":
    ssid = input("Enter the WiFi SSID: ")
    password = input("Enter the WiFi Password: ")
    write_to_nfc_tag(ssid, password)
