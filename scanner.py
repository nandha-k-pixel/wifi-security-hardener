
import subprocess
import urllib.request
import urllib.error


def get_network_info():
    """Detect the default network interface and gateway."""

    print("[*] Detecting network information...")

    try:
        route_output = subprocess.check_output(
            ["ip", "route"],
            text=True
        )

        gateway = None
        interface = None

        for line in route_output.splitlines():
            if line.startswith("default"):
                parts = line.split()

                if "via" in parts:
                    gateway = parts[parts.index("via") + 1]

                if "dev" in parts:
                    interface = parts[parts.index("dev") + 1]

                break

        print(f"[+] Interface: {interface}")
        print(f"[+] Gateway: {gateway}")

        return gateway, interface

    except subprocess.CalledProcessError as error:
        print(f"[-] Route detection failed: {error}")
        return None, None


def check_router_http(gateway):
    """Check whether the router responds over HTTP."""

    if not gateway:
        print("[-] Gateway not detected.")
        return

    url = f"http://{gateway}/"

    print(f"\n[*] Checking router HTTP: {url}")

    try:
        request = urllib.request.Request(
            url,
            method="GET"
        )

        with urllib.request.urlopen(request, timeout=5) as response:
            print(f"[+] HTTP Status: {response.status}")
            print(f"[+] Server: {response.headers.get('Server', 'Unknown')}")
            print(f"[+] Final URL: {response.geturl()}")

    except urllib.error.HTTPError as error:
        print(f"[+] HTTP Status: {error.code}")
        print(f"[+] Server: {error.headers.get('Server', 'Unknown')}")
        print(f"[+] Location: {error.headers.get('Location', 'None')}")

    except urllib.error.URLError as error:
        print(f"[-] Router HTTP check failed: {error.reason}")

    except Exception as error:
        print(f"[-] Unexpected error: {error}")


if __name__ == "__main__":
    print("===================================")
    print(" Wi-Fi Security Network Scanner")
    print("===================================\n")

    gateway, interface = get_network_info()


    # check_router_http(gateway)

    print("\n[!] NAT gateway detected.")
    print("[!] Router audit requires your router's local network connection.")