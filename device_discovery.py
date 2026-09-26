from network_info import get_network_info
import subprocess
import re


def discover_devices(interface=None, network=None):
    """Discover devices on the authorized local network."""
    if interface is None or network is None:
        _, detected_interface, detected_network = get_network_info()

        if detected_interface is None or detected_network is None:
            print("[-] Could not detect local network.")
            return []

        interface = detected_interface
        network = detected_network
    print("\n[*] Discovering local network devices...")

    command = [
        "sudo",
        "arp-scan",
        "--interface", interface,
        network
    ]

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=30
        )

        devices = []

        pattern = re.compile(
            r"^(\d+\.\d+\.\d+\.\d+)\s+"
            r"([0-9a-fA-F:]{17})\s*(.*)$"
        )

        for line in result.stdout.splitlines():
            match = pattern.match(line.strip())

            if match:
                ip = match.group(1)
                mac = match.group(2)
                vendor = match.group(3).strip()

                device = {
                  "ip": ip,
                  "mac": mac.lower(),
                  "vendor": vendor or "Unknown"
                }

               # Avoid duplicate IP and MAC entries
                if not any(
                   existing["ip"] == device["ip"]
                   and existing["mac"] == device["mac"]
                   for existing in devices
                ):
                   devices.append(device)

        print(f"[+] Devices discovered: {len(devices)}")

        for device in devices:
            print(
                f"- {device['ip']} | "
                f"{device['mac']} | "
                f"{device['vendor']}"
            )

        return devices

    except subprocess.TimeoutExpired:
        print("[-] Device discovery timed out.")
        return []

    except Exception as error:
        print(f"[-] Discovery failed: {error}")
        return []


if __name__ == "__main__":
    discover_devices()