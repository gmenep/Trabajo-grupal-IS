import bcrypt


class PasswordLogica:

    def hash_password(self, password):
        password_bytes = password.encode("utf-8")
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password_bytes, salt)
        return hashed_password.decode("utf-8")

    def verificar_password(self, password, stored_hash):
        if password is None or stored_hash is None:
            return False

        try:
            password_bytes = password.encode("utf-8")
            stored_hash_bytes = stored_hash.encode("utf-8")
            return bcrypt.checkpw(password_bytes, stored_hash_bytes)

        except ValueError:
            return False


if __name__ == "__main__":
    password_logica = PasswordLogica()
    password_plana = "changeme"
    password_hash = password_logica.hash_password(password_plana)

    print("Hash generado:", password_hash)
    print("Password correcta:", password_logica.verificar_password("changeme", password_hash))
    print("Password incorrecta:", password_logica.verificar_password("otra", password_hash))
