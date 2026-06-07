import bcrypt


class PasswordService:
    def hash_password(self, password):
        texto = password.encode("utf-8")
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(texto, salt).decode("utf-8")

    def verificar_password(self, password, pass_hash):
        if password is None or pass_hash is None:
            return False
        try:
            return bcrypt.checkpw(password.encode("utf-8"), pass_hash.encode("utf-8"))
        except Exception:
            return False
