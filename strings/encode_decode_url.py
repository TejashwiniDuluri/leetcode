import base64


class Codec:
    def __init__(self) -> None:
        self.hash = {}

    def encode(self, longUrl: str) -> str:
        encoded_msg = base64.b64encode(
            longUrl.encode()).decode().replace("/", ".")
        total_url = encoded_msg
        self.hash[encoded_msg] = longUrl

        return total_url

    def decode(self, shortUrl: str) -> str:
        return self.hash[shortUrl.split("/")[-1]]


# Your Codec object will be instantiated and called as such:
url = "http://badge.example.net/beginner.aspx?aftermath=achiever&actor=air"
codec = Codec()
print(codec.decode(codec.encode(url)))
