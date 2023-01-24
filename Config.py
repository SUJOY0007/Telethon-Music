import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "29102410"))
    API_HASH = os.environ.get("API_HASH", "53df200130dc74af318c900882aa0f11")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5863933862:AAFuPkTdl8bbsKXwxb4y_Rly5Pu4igaaZ4Y")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOJUBuzeCWraOlH03p9UCcyYFGldzU0TkB9BWt7VN5M1yXKSJuT-J-_6mHsffNsbbcC71vDGHSisn0aRROlegDWr7nTyUvGiKpQy6tj9jeIv_eD7SFrsCfzZkUJ2xpu9o8blfK21_-C8tr74KRl3N2jdb6Xp0DLg8cDTiHXYWqxpn_2Iv-gtPXzKKSI0Kcvvg4nGQFy-1sPrq29-kY98bo8ZvkX0nHfg-gmwp4P3yBSWWne2PH3oB2GXk5Enyw-W2jYXH7wgesg-5D9SdWxhXH0YgU2o_aOunHJnZvvFduhpguRCo_T7c5780ePuUt3pHo3rCibcToYVfvR4YUv-2m2AkdHk=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@MT_GROUPMUSIC_BOT")
    SUPPORT = os.environ.get("SUPPORT", "-1001872352449") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "@AASHIYANA_MERA") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5408061904")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
