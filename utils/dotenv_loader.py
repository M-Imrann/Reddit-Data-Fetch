import os
from dotenv import load_dotenv


def load_env():
    load_dotenv()
    client_id = os.getenv("REDDIT_CLIENT_ID")
    client_secret = os.getenv("REDDIT_CLIENT_SECRET")
    user_agent = os.getenv("USER_AGENT")

    if not all([client_id, client_secret, user_agent]):
        raise EnvironmentError("Missing Reddit credentials in dotenv")

    return client_id, client_secret, user_agent
