import dns.resolver

class DNSTransport:
    def send(self, domain, data):
        query = f"{data}.{domain}"
        try:
            dns.resolver.resolve(query, 'TXT')
            return True
        except Exception:
            return False
