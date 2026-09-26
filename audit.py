
import http.client
import ssl


def check_http(gateway):
    """Check the router's HTTP management service."""

    print("\n[*] Checking HTTP management...")

    connection = http.client.HTTPConnection(
        gateway,
        80,
        timeout=5
    )

    try:
        connection.request("GET", "/")
        response = connection.getresponse()

        headers = dict(response.getheaders())

        print(f"[+] HTTP Status: {response.status}")
        print(f"[+] Server: {headers.get('Server', 'Unknown')}")
        print(f"[+] Location: {headers.get('Location', 'None')}")

        return {
            "status": response.status,
            "server": headers.get("Server", "Unknown"),
            "location": headers.get("Location", "None")
        }

    except (OSError, http.client.HTTPException) as error:
        print(f"[-] HTTP check failed: {error}")
        return None

    finally:
        connection.close()


def check_https(gateway):
    """Check whether HTTPS responds on port 443."""

    print("\n[*] Checking HTTPS management...")

    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    connection = http.client.HTTPSConnection(
        gateway,
        443,
        timeout=5,
        context=context
    )

    try:
        connection.request("GET", "/")
        response = connection.getresponse()

        print(f"[+] HTTPS Status: {response.status}")

        return {
            "status": response.status,
            "available": True
        }

    except (
        OSError,
        ssl.SSLError,
        http.client.HTTPException
    ) as error:
        print(f"[!] HTTPS connection failed: {error}")

        return {
            "available": False,
            "error": str(error)
        }

    finally:
        connection.close()


def generate_findings(http_result, https_result):
    """Generate security findings from HTTP and HTTPS checks."""

    findings = []

    # HTTP check
    if http_result is None:

        findings.append({
            "severity": "INFO",
            "title": "HTTP check unavailable",
            "description": (
                "The HTTP service could not be reached. "
                "Check network connectivity and the "
                "authorized target IP."
            )
        })

    else:

        status = http_result["status"]
        location = http_result["location"]

        findings.append({
            "severity": "REVIEW",
            "title": "HTTP management detected",
            "description": (
                f"HTTP returned status {status}. "
                "Review whether HTTP management should "
                "be disabled or redirected to HTTPS."
            )
        })

        # Redirect analysis
        if status in (301, 302, 303, 307, 308):

            if location.startswith("https://"):

                findings.append({
                    "severity": "INFO",
                    "title": "HTTP redirects to HTTPS",
                    "description": (
                        f"HTTP redirects to {location}. "
                        "This indicates an HTTPS redirect "
                        "was detected."
                    )
                })

            else:

                findings.append({
                    "severity": "REVIEW",
                    "title": "HTTP redirect does not confirm HTTPS",
                    "description": (
                        f"HTTP redirects to {location}. "
                        "Verify whether the router enforces "
                        "secure HTTPS management."
                    )
                })

        # Server banner
        if http_result["server"] != "Unknown":

            findings.append({
                "severity": "INFO",
                "title": "Server banner detected",
                "description": (
                    f"Server: {http_result['server']}. "
                    "Check official vendor documentation "
                    "for firmware and supported versions."
                )
            })

    # HTTPS check
    if https_result and https_result["available"]:

        findings.append({
            "severity": "INFO",
            "title": "HTTPS management responding",
            "description": (
                f"HTTPS returned status "
                f"{https_result['status']}. "
                "Review certificate configuration and "
                "secure management settings."
            )
        })

        findings.append({
            "severity": "REVIEW",
            "title": "Verify HTTPS certificate",
            "description": (
                "The current connection test does not "
                "validate the router's certificate. "
                "Review certificate trust, TLS settings, "
                "and management access restrictions."
            )
        })

    elif https_result and not https_result["available"]:

        findings.append({
            "severity": "REVIEW",
            "title": "HTTPS connection failed",
            "description": (
                "The HTTPS test did not complete. "
                "Verify whether secure management is "
                "supported and enabled on the router."
            )
        })

    # General recommendation
    findings.append({
        "severity": "INFO",
        "title": "Router security hardening recommendation",
        "description": (
            "Use a strong unique administrator password, "
            "keep router firmware updated, disable remote "
            "WAN administration if unnecessary, and use "
            "WPA2-AES or WPA3 when supported."
        )
    })

    return findings


if __name__ == "__main__":

    gateway = input(
        "Enter router IP [192.168.1.1]: "
    ).strip()

    if not gateway:
        gateway = "192.168.1.1"

    http_result = check_http(gateway)
    https_result = check_https(gateway)

    findings = generate_findings(
        http_result,
        https_result
    )

    print("\n===================================")
    print(" Security Audit Findings")
    print("===================================")

    for index, finding in enumerate(findings, start=1):

        print(
            f"\n{index}. "
            f"[{finding['severity']}] "
            f"{finding['title']}"
        )

        print(
            f"   {finding['description']}"
        )