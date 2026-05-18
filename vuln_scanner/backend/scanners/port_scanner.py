import nmap
from urllib.parse import urlparse

def run_port_scan(target):

    try:

        # Extract hostname only

        parsed = urlparse(target)

        hostname = parsed.netloc if parsed.netloc else parsed.path

        scanner = nmap.PortScanner()

        scanner.scan(hostname, '1-1024')

        results = []

        for host in scanner.all_hosts():

            for proto in scanner[host].all_protocols():

                ports = scanner[host][proto].keys()

                for port in ports:

                    results.append({
                        "port": port,
                        "state": scanner[host][proto][port]['state']
                    })

        return results

    except Exception as e:

        return {
            "error": str(e)
        }
