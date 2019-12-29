from base64 import b64encode,b64decode

cookie = 'p0AHKFY4ZazN2iPT0OfjxKBdo9XeP0MpVQXyfodZqRY0kDxq4coWRLhxMW+nZw3shqk4FmTSizeTayEoXYZp6f8YI/aneFp/g8jbsQrXMqE='
user_cookie = "{'admin': 0, 'username': '123', 'password': '123'}"
user_cookie_with_iv = ("X" * 16) + user_cookie # 16 is block size in bytes
byte_offset = user_cookie_with_iv.find("0") # that is value of admin 
byte_to_flip = byte_offset - 16
token = b64decode(cookie)

cookie_chars = bytearray(token)
cookie_chars[byte_to_flip] = cookie_chars[byte_to_flip] ^ ord("0") ^ ord("1")
encode_cookie_admin = b64encode(cookie_chars).decode("utf-8")

print(encode_cookie_admin)
