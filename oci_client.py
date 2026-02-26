import oci

CONFIG_PROFILE = "SAOPAULO"
CONFIG_FILE = "~/.oci/config"
ENDPOINT = "https://inference.generativeai.sa-saopaulo-1.oci.oraclecloud.com"

MODEL_OCID = "ocid1.generativeaimodel.oc1.sa-saopaulo-1.amaaaaaask7dceya5jeqxpapicf3unmiktoes4bjnis4cnd6aeejhx2q5c2q"
COMPARTMENT_ID = "ocid1.compartment.oc1..aaaaaaaaglekaj4zn2kqjwcu6fvdgnjqmwrvmvb6z7znocaun2zron2nl3jq"

def perguntar_modelo(prompt_usuario):

    config = oci.config.from_file(CONFIG_FILE, CONFIG_PROFILE)

    client = oci.generative_ai_inference.GenerativeAiInferenceClient(
        config=config,
        service_endpoint=ENDPOINT,
        retry_strategy=oci.retry.NoneRetryStrategy(),
        timeout=(10, 240)
    )

    chat_detail = oci.generative_ai_inference.models.ChatDetails()

    chat_request = oci.generative_ai_inference.models.CohereChatRequest()
    chat_request.message = prompt_usuario
    chat_request.max_tokens = 300
    chat_request.temperature = 0.2
    chat_request.frequency_penalty = 0
    chat_request.top_p = 0.75
    chat_request.top_k = 0
    chat_request.safety_mode = "CONTEXTUAL"

    chat_detail.serving_mode = oci.generative_ai_inference.models.OnDemandServingMode(
        model_id=MODEL_OCID
    )
    chat_detail.chat_request = chat_request
    chat_detail.compartment_id = COMPARTMENT_ID

    response = client.chat(chat_detail)

    return response.data.chat_response.text
