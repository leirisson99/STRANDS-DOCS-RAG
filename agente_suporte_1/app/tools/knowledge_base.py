from strands import tool

_KB = [
    {"tags": ["vpn", "conexão"], "solucao": "Reinicie o cliente VPN; confira data/hora do sistema; reconecte."},
    {"tags": ["impressora", "fila"], "solucao": "Reinicie o spooler de impressão e remova trabalhos travados."},
    {"tags": ["outlook", "email"], "solucao": "Feche o Outlook, abra em modo de segurança e desative suplementos."},
    {"tags": ["senha", "bloqueio"], "solucao": "Use o portal de autoatendimento; se a conta estiver bloqueada, abra ticket."},
]

@tool
def search_kb(query: str) -> str:
    """Busca soluções conhecidas na base de conhecimento. Consulte SEMPRE antes de sugerir solução.

    Args:
        query: Palavras-chave do problema, ex: "vpn não conecta".
    """
    #query
    q = query.casefold()
    hits = [a["solucao"] for a in _KB if any(t in q for t in a["tags"])]
    return "\n".join(hits) if hits else "Nenhum artigo encontrado."
