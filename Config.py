import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "29102410"))
    API_HASH = os.environ.get("API_HASH", "53df200130dc74af318c900882aa0f11")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5964726300:AAE5zfJECTgvE6xVBy1ptaX0i8Dawri6IiQ")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOJUBu2uBX1giSIENBlF95kwKu9FhbRsGRmXV0OrlOinpGk6p9pDtdU88QMzP2WNaNgHfg3OG1dqBLvCaLsgP3eNDXLqlx1S4w8J45zNnxIcCrMZ0W2928f5oK6HEtVnOCb9jfqpmAJcJIV90DRzSf3sq-QKQ7_U6WleGW0QpRiw7Jh-PRg-vWk7wz4WXw9UtdsT9izsV0tjdqMUvFYmVlMF9U7ZKyCZ8QfgTI4tsRlsbpfmY2STeKK0IP6QMk-cTo6gBOm8Jj6fRKM54yTZRQhiKrdh0wEdOr3vuwf0HBgWE12eDlYkUNKF9ZvyCEM1q3MREWiISheZ8II0wmjNc6wJdJFk=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@MT_MUSICX_BOT")
    SUPPORT = os.environ.get("SUPPORT", "-1001872352449") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "@sujoy_man") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5408061904")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
