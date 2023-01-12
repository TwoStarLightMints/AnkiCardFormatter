from card_gen import CardGenerator
from write_anki_txt import AnkiTxtWriter

class Engine:
    def __init__(self, path, separator:str="\t", html:str="false", deck_column:str="1", tags_column:str="4", deck:str="German Vocab::General"):
        self.generator = CardGenerator(path)
        self.writer = AnkiTxtWriter(self.generator.processed, separator, html, deck_column, tags_column, deck)

        self.writer.create_anki_txt_file(separator, html, deck_column, tags_column, deck)

if __name__ == "__main__":
    eng = Engine("anki.txt")