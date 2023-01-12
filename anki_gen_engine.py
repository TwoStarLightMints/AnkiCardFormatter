from sys import argv

from card_gen import CardGenerator
from write_anki_txt import AnkiTxtWriter

class Engine:
    IMPORT_FROM_EXT = ".txt"
    def __init__(self, path, separator:str="\t", html:str="false", deck_column:str="1", deck:str="German Vocab::General"):
        self.generator = CardGenerator(f"{path}{self.IMPORT_FROM_EXT}")
        self.writer = AnkiTxtWriter(self.generator.processed, separator, html, deck_column, deck)

if __name__ == "__main__":
    eng = Engine(argv[1], deck="TESTING_PY")