import socket


def resolve_dns(hostname: str) -> str:
    """Resolve um nome de host para IP. Use para distinguir falha de DNS de falha de rede.

    Args:
        hostname: Nome a resolver, ex: "google.com".
    """
    try:
        return socket.gethostbyname(hostname)
    except socket.gaierror:
        return "falha na resolução."