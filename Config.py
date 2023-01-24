import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "29102410"))
    API_HASH = os.environ.get("API_HASH", "53df200130dc74af318c900882aa0f11")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5863933862:AAFuPkTdl8bbsKXwxb4y_Rly5Pu4igaaZ4Y")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOJUBuxj8tkMhnfTEZPDW15pq7yc0d7LUTTAQRwP7Q99v9saBpTtzNtiNZwn06MXLhsr3sWtsw0qPEuQXp23THEQ-ZE9Na2DdY8fDVoZXF8w6X8eo-Wefu7nnGE4tZuve4EoE2YnW57KCewvYcqzOFo4gByvLOdqzmhU_Tx2bcBXZeWyA5ydYaA10ySckF8fHnwarzVF7L5qOeXp1eEX0oFer3jRV6JZYzWjhXmRDzHswcnb5z0MZQx4uPHPcdT3339fJLUU4_xTmTn0WEMd7EfVOvV989VrqeuXwdkbT28Uc65JfW_d0Ajs1-w3QSkDNbp_o1dvFa-YHPOHu4xI2mg4YD1o=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@MT_GROUPMUSIC_BOT")
    SUPPORT = os.environ.get("SUPPORT", "-1001872352449") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "@AASHIYANA_MERA") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5408061904")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', "True") # Change it to "True"
