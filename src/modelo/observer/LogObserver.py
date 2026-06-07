from src.modelo.dao.LogDaoJDBC import LogDaoJDBC
from src.modelo.observer.Observador import Observador


class LogObserver(Observador):
    def __init__(self):
        self.__log_dao = LogDaoJDBC()

    def actualizar(self, log_vo):
        self.__log_dao.insert(log_vo)
