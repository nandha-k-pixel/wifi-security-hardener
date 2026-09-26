
import socket


SERVICES = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    80: "HTTP",
    443: "HTTPS",
    8080: "Alternative HTTP"
}


def check_services(gateway):
    """Check common TCP services on the authorized router."""

    print("\n[*] Checking router services...")

    results = []

    for port, service in SERVICES.items():

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        try:
            connection_result = sock.connect_ex(
                (gateway, port)
            )

            if connection_result == 0:
                status = "OPEN"
                print(f"[+] {service} (Port {port}): OPEN")
            else:
                status = "CLOSED"
                print(f"[-] {service} (Port {port}): CLOSED")

            results.append({
                "service": service,
                "port": port,
                "status": status
            })

        except socket.error as error:

            results.append({
                "service": service,
                "port": port,
                "status": "ERROR",
                "error": str(error)
            })

        finally:
            sock.close()

    return results


def generate_service_findings(results):
    """Generate recommendations from service results."""

    findings = []

    for result in results:

        if result["status"] != "OPEN":
            continue

        service = result["service"]
        port = result["port"]

        if service in ("Telnet", "FTP"):

            severity = "REVIEW"

            description = (
                f"{service} is reachable on port {port}. "
                "Disable it in the router administration "
                "interface if it is not required."
            )

        elif service == "SSH":

            severity = "REVIEW"

            description = (
                "SSH is reachable. Verify that remote "
                "administration is required and restricted "
                "to trusted local users or networks."
            )

        else:

            severity = "INFO"

            description = (
                f"{service} is reachable on port {port}. "
                "Verify that this management service is "
                "required and properly secured."
            )

        findings.append({
            "severity": severity,
            "title": f"{service} service detected",
            "description": description
        })

    return findings


if __name__ == "__main__":

    gateway = input(
        "Enter router IP [192.168.1.1]: "
    ).strip()

    if not gateway:
        gateway = "192.168.1.1"

    results = check_services(gateway)
    findings = generate_service_findings(results)

    print("\n===================================")
    print(" Service Audit Findings")
    print("===================================")

    for finding in findings:

        print(
            f"\n[{finding['severity']}] "
            f"{finding['title']}"
        )

        print(f"  {finding['description']}")