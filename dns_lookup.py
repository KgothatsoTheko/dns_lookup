# Install dependency:
# pip install dnspython rich

import dns.resolver
from rich.console import Console
from rich.table import Table

def get_dns_records(domain: str):
    record_types = ["A", "AAAA", "SOA", "MX", "NS", "TXT", "CNAME"]
    resolver = dns.resolver.Resolver()
    console = Console()

    table = Table(title=f"DNS Records for {domain}")
    table.add_column("Record Type", style="cyan", no_wrap=True)
    table.add_column("Value", style="green")

    for record_type in record_types:
        try:
            answers = resolver.resolve(domain, record_type)
            values = [r.to_text() for r in answers]
            table.add_row(record_type, "\n".join(values))
        except dns.resolver.NoAnswer:
            table.add_row(record_type, "No answer")
        except dns.resolver.NXDOMAIN:
            console.print(f"[red]Error:[/] Domain {domain} does not exist.")
            return
        except dns.resolver.Timeout:
            table.add_row(record_type, "Query timed out")
        except Exception as e:
            table.add_row(record_type, f"Error: {e}")

    console.print(table)

if __name__ == "__main__":
    domain = input("Enter a domain name (e.g., example.com): ").strip()
    if domain:
        get_dns_records(domain)
    else:
        print("No domain entered.")
