import os

bot_token = str(os.getenv("TOKEN_TG"))
vk_token = str(os.getenv("TOKEN_VK"))
api_url = 'http://nginx/api/v1'
api_token = str(os.getenv("API_TOKEN"))
group_id = int(os.getenv("VK_GROUP"))
host = 'dateindb'
database = str(os.getenv("DB_DB"))
user = str(os.getenv("DB_USER"))
password = str(os.getenv("DB_PASSWORD"))
port = '5432'
POSTGRES_URI = f'postgresql://{user}:{password}@{host}:{port}/{database}'
WEBHOOK_DOMAIN = str(os.getenv("TG_WEBHOOK_DOMAIN"))
WEBAPP_HOST = '127.0.0.1'
WEBAPP_PORT = '3001'
WEBHOOK = int(os.getenv("TG_WEBHOOK_MODE"))
