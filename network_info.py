import subprocess
import re


def get_network_info():
    """Automatically detect the active local network."""

    try:
        result = subprocess.run(
            ["ip", "route"],
            capture_output=True,
            text=True,
            check=True
        )

        routes = result.stdout.splitlines()

        gateway = None
        interface = None
        network = None

        for route in routes:

            if route.startswith("default"):
                gateway_match = re.search(
                    r"default via (\S+) dev (\S+)",
                    route
                )

                if gateway_match:
                    gateway = gateway_match.group(1)
                    interface = gateway_match.group(2)

            elif "scope link" in route and "src" in route:
                network_match = re.match(
                    r"(\S+) dev (\S+)",
                    route
                )

                if network_match:
                    network = network_match.group(1)

        if gateway and interface and network:
            print("\n[+] Network information detected")
            print(f"    Gateway: {gateway}")
            print(f"    Interface: {interface}")
            print(f"    Network: {network}")

            return gateway, interface, network

        print("[-] Could not detect network information.")
        return None, None, None

    except subprocess.CalledProcessError as error:
        print(f"[-] Command failed: {error}")
        return None, None, None


if __name__ == "__main__":
    get_network_info()