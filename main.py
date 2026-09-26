import scanner
import audit
import service_audit
import device_discovery
import firmware_check
import report_generator
from network_info import get_network_info
from security_score import calculate_score, score_label

def get_router_ip():
    gateway, interface, network = get_network_info()
    if gateway:
        router_ip = input(f"Enter router IP [{gateway}]: ").strip() or gateway
    else:
        router_ip = input("Enter authorized router IP: ").strip()
    return router_ip, gateway, interface, network

def print_findings(findings):
    print("\n===================================")
    print(" Security Findings")
    print("===================================")
    for index, finding in enumerate(findings, start=1):
        print(f"\n{index}. [{finding.get('severity', 'INFO')}] {finding.get('title', 'Finding')}")
        print(f"   {finding.get('description', '')}")

def run_full_audit():
    router_ip, gateway, interface, network = get_router_ip()
    if not router_ip:
        print("[-] Router IP is required.")
        return

    http_result = audit.check_http(router_ip)
    https_result = audit.check_https(router_ip)
    findings = audit.generate_findings(http_result, https_result)

    print("\n[*] Running service audit...")
    service_results = service_audit.check_services(router_ip)
    findings.extend(
        service_audit.generate_service_findings(service_results)
    )

    print("\n[*] Discovering local devices...")
    devices = device_discovery.discover_devices(interface, network)

    firmware_info = firmware_check.collect_firmware_info()

    print_findings(findings)
    score = calculate_score(findings)
    print(f"\n[*] Security score: {score}/100 ({score_label(score)})")

    report_generator.generate_report(
        gateway=router_ip,
        findings=findings,
        devices=devices,
        service_results=service_results,
        firmware_info=firmware_info,
        network_info={
            "gateway": gateway,
            "interface": interface,
            "network": network
        }
    )

def run_device_discovery():
    devices = device_discovery.discover_devices()
    gateway, interface, network = get_network_info()
    report_generator.generate_report(
        gateway or "Unknown",
        [],
        devices=devices,
        network_info={
            "gateway": gateway,
            "interface": interface,
            "network": network
        }
    )

def run_service_audit():
    router_ip, _, _, _ = get_router_ip()
    if not router_ip:
        print("[-] Router IP is required.")
        return
    results = service_audit.check_services(router_ip)
    findings = service_audit.generate_service_findings(results)
    print_findings(findings)

def run_firmware_check():
    return firmware_check.collect_firmware_info()

def main():
    while True:
        print("\n===================================")
        print(" Wi-Fi Security Hardening Tool")
        print("===================================")
        print("[1] Network Scanner")
        print("[2] Complete Router Security Audit")
        print("[3] Device Discovery")
        print("[4] Generate Combined Security Report")
        print("[5] Service Audit")
        print("[6] Firmware Security Check")
        print("[0] Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            scanner.get_network_info()
        elif choice == "2":
            run_full_audit()
        elif choice == "3":
            run_device_discovery()
        elif choice == "4":
            run_full_audit()
        elif choice == "5":
            run_service_audit()
        elif choice == "6":
            run_firmware_check()
        elif choice == "0":
            print("\n[+] Exiting tool. Goodbye!")
            break
        else:
            print("\n[-] Invalid choice. Try again.")

if __name__ == "__main__":
    main()
