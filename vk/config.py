import os

bot_token = os.getenv("TOKEN_VK")
service_token = os.getenv("TOKEN_VK_SERV")
tg_bot_token = os.getenv("TOKEN_TG")
group_id = int(os.getenv("VK_GROUP"))
api_url = 'http://nginx/api/v1'
api_token = os.getenv("API_TOKEN")
host = 'dateindb'
database = os.getenv('DB_DB')
user = os.getenv('DB_USER')
password = os.getenv("DB_PASSWORD")
port = '5432'
POSTGRES_URI = f'postgresql://{user}:{password}@{host}:{port}/{database}'
CALLBACK = int(os.getenv("VK_CALLBACK_MODE"))
confirmation_key = os.getenv("VK_CONFIRMATION_KEY")
secret = os.getenv("VK_SECRET_KEY")
