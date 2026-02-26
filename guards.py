import re

PALAVRAS_BLOQUEADAS = [
    "ignore",
    "ignore as instruções",
    "system prompt",
    "mostre todas",
    "dump",
    "exporte",
    "liste todos",
    "reveal",
    "mostre o segredo",
    "imprima tudo"
]

def detectar_prompt_injection(prompt):
    prompt_lower = prompt.lower()

    for palavra in PALAVRAS_BLOQUEADAS:
        if palavra in prompt_lower:
            return True, f"Possível tentativa de prompt injection detectada: '{palavra}'"

    return False, None


def mascarar_pii(texto):
    # CPF simples
    texto = re.sub(r"\d{3}\.\d{3}\.\d{3}-\d{2}", "[CPF_REDACTED]", texto)

    # Emails
    texto = re.sub(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", "[EMAIL_REDACTED]", texto)

    # Telefones simples
    texto = re.sub(r"\(?\d{2}\)?\s?\d{4,5}-\d{4}", "[PHONE_REDACTED]", texto)

    return texto
