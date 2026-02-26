from oci_client import perguntar_modelo
from guards import detectar_prompt_injection, mascarar_pii
from logger import log_event

MODEL_NAME = "cohere.command-r-08-2024"
REGION = "sa-saopaulo-1"

def main():
    print("\n=== Secure vs Insecure (OCI GenAI) ===\n")
    pergunta = input("Digite sua pergunta: ").strip()

    # 1) Primeiro decidimos se o modo seguro bloquearia (sem chamar o modelo ainda)
    suspeito, motivo = detectar_prompt_injection(pergunta)

    # Log do modo seguro (decisão)
    if suspeito:
        log_event({
            "mode": "secure",
            "action": "block",
            "reason": motivo,
            "prompt_preview": pergunta[:160],
            "model": MODEL_NAME,
            "region": REGION
        })
    else:
        log_event({
            "mode": "secure",
            "action": "allow",
            "reason": None,
            "prompt_preview": pergunta[:160],
            "model": MODEL_NAME,
            "region": REGION
        })

    # Log do modo inseguro (sempre allow)
    log_event({
        "mode": "insecure",
        "action": "allow",
        "reason": None,
        "prompt_preview": pergunta[:160],
        "model": MODEL_NAME,
        "region": REGION
    })

    # 2) Chama o modelo uma única vez (para comparação justa)
    resposta_modelo = perguntar_modelo(pergunta)

    print("\n--- MODO INSEGURO (sem guardrails) ---")
    print(resposta_modelo)

    print("\n--- MODO SEGURO (com guardrails) ---")
    if suspeito:
        print(f"🚫 Bloqueado por política de segurança.\nMotivo: {motivo}")
    else:
        print(mascarar_pii(resposta_modelo))

    print("\n(Log gravado em logs.jsonl)")

if __name__ == "__main__":
    main()
