
class Settings:
    key_words = ["technology", "science"]
    api_keys = {"NewsApi.org": "7f7dca4824124b3a8bfc499ee1ac427d",
                "NewsData.io": "pub_14335257c88334563a6d6035196c3c7d8e917"}

    @classmethod
    def set_default(cls):
        Settings.key_words = ["technology", "science"]
        Settings.api_keys = {
            "NewsApi.org": "7f7dca4824124b3a8bfc499ee1ac427d",
            "NewsData.io": "pub_14335257c88334563a6d6035196c3c7d8e917"
        }
