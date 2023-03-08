import vk_api

def init_session():
    TOKEN = open(f"access_token.txt").read().strip()
    session = vk_api.VkApi(token=TOKEN)
    return session.get_api()