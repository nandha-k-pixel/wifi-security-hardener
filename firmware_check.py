
from datetime import datetime


def collect_firmware_info():
    """Collect firmware information provided by the router administrator."""

    print("\n===================================")
    print(" Firmware Security Check")
    print("===================================")

    manufacturer = input("Router manufacturer: ").strip()
    model = input("Router model: ").strip()
    firmware_version = input("Current firmware version: ").strip()

    if not manufacturer:
        manufacturer = "Unknown"

    if not model:
        model = "Unknown"

    if not firmware_version:
        firmware_version = "Unknown"

    result = {
        "timestamp": datetime.now().isoformat(),
        "manufacturer": manufacturer,
        "model": model,
        "current_firmware": firmware_version,
        "verification_status": "User-provided",
        "recommendation": (
            "Check the official manufacturer support website "
            "for the latest firmware version. "
            "Verify the exact model and hardware revision "
            "before installing an update."
        )
    }

    print("\n[*] Firmware Information")
    print(f"Manufacturer: {manufacturer}")
    print(f"Model: {model}")
    print(f"Current Firmware: {firmware_version}")

    print("\n[!] Recommendation")
    print(result["recommendation"])

    return result


if __name__ == "__main__":
    collect_firmware_info()