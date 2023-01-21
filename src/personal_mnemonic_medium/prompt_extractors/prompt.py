from typing import List


class Prompt:
    def __init__(self, tags: List[str], subdeck: str, uuid: str):
        self.tags = tags
        self.subdeck = subdeck
        self.uuid = uuid
