import os
from . import StoreInterface, cached


class Store(StoreInterface):
    def __init__(self, name, infos):
        self.name = name

    def gen_parser(self, parser):
        parser.add_argument("secret")

    @cached
    def read_secret(self, secret):
        if res := os.getenv(secret):
            return res
        else:
            raise Exception(f"Secret '{secret}' not found in store '{self.name}'")
