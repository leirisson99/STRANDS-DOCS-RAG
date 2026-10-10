import platform
import socket
import subprocess 
from strands import tool

@tool
def ping_host(host: str) -> str :
    """Teste se um  host responde na rede. Use para problemas de conexão
    args: 
        host: Nome ou IP do host, ex: 8.8.8.8 ou "intranet.empresa.com"
    """
    flag = "-n" if platform.system() == "windows" else "-c"
    try:
        r = subprocess.run([
            "ping", flag, "2", host
        ],
                           capture_output=True, text=True, timeout=10)
        return "response" if r.returncode == 0 else "não responde"
    except subprocess.TimeoutExpired :
        return "Tempo esgotado."