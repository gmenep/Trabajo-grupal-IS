import bcrypt


class PasswordLogica:
    @staticmethod
    def hash_password(password):
        password_bytes = password.encode("utf-8")
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password_bytes, salt)
        return hashed_password.decode("utf-8")

    @staticmethod
    def verify_password(password, stored_hash):
        if password is None or stored_hash is None:
            return False

        try:
            password_bytes = password.encode("utf-8")
            stored_hash_bytes = stored_hash.encode("utf-8")
            return bcrypt.checkpw(password_bytes, stored_hash_bytes)

        except ValueError:
            return False


if __name__ == "__main__":
    password_plana = "changeme"
    password_hash = PasswordLogica.hash_password(password_plana)

    print("Hash generado:", password_hash)
    print("Password correcta:", PasswordLogica.verify_password("changeme", password_hash))
    print("Password incorrecta:", PasswordLogica.verify_password("otra", password_hash))
