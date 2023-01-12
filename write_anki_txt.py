class AnkiTxtWriter:
    def __init__(self, cards: str, separator:str="\t", html:str="false", deck_column:str="1", tags_column:str="4", deck:str="German Vocab::General"):
        self.card_contents = cards
        self.create_anki_txt_file(separator, html, deck_column, tags_column, deck)
    
    def create_anki_txt_file(self, sep: str, html: str, deck_col: str, tag_col: str, deck: str):
        with open("to_import.txt", "w") as anki:
            anki.write(f"#separator:{sep}\n")
            anki.write(f"html:{html}\n")
            anki.write(f"#deck column:{deck_col}\n")
            anki.write(f"tags column:{tag_col}\n")

            # From here on, write the different cards
            for card in self. card_contents:
                anki.write(f"{deck}\t{card}\n")

if __name__ == "__main__":
    AnkiTxtWriter("anki.txt")