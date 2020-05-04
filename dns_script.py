import dns.resolver

resolver = dns.resolver.Resolver()

host = input("DNS ime ili IP adresa: ")
dns_type = input("Tip DNS zapisa(A, MX, PTR): ")

try:
    req = host
    if (dns_type == "PTR"):
        req = '.'.join(reversed(host.split("."))) + ".in-addr.arpa"

    answers = resolver.query(req, dns_type)
    for data in answers:
        print(data)
except:
    print("Neispravan unos")