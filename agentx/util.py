import os


def get_headers(api_key: str = None):
    return {"accept": "*/*", "x-api-key": api_key or os.getenv("AGENTX_API_KEY")}
