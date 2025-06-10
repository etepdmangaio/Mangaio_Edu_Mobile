import re

def email_valido(email: str) -> bool:
    """Valida formato padrão de e-mail"""
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(padrao, email) is not None
