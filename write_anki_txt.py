from os.path import isfile

class AnkiTxtWriter:
    # Cards is a list of strings received from the CardGenerator
    # Separator determines the character used to separate fields in the txt document
    # If html is true, then the html inside of the front and back is parsed as a real html document, otherwise it is treated as plain text
    # Deck column tells Anki where to look for the decks
    # Deck is used to set a default deck for all the produced cards
    def __init__(self, cards: list[str], separator:str="\t", html:str="true", deck_column:str="1", deck:str="German Vocab::General"):
        self.card_contents = cards
        self.create_anki_txt_file(separator, html, deck_column, deck)
    
    def create_anki_txt_file(self, sep: str, html: str, deck_col: str, deck: str):
        file_name = "to_import"
        count = 1
        file_ext = "txt"

        file = ""

        if isfile(f"{file_name}.{file_ext}"):
            while isfile(f"{file_name}{count}.{file_ext}"):
                count += 1
            file = f"{file_name}{count}.{file_ext}"
        else:
            file = f"{file_name}.{file_ext}"
        
        with open(file, "w") as anki:
            anki.write(f"#separator:{sep}\n")
            anki.write(f"#html:{html}\n")
            anki.write(f"#deck column:{deck_col}\n")

            # From here on, write the different cards
            for card in self. card_contents:
                anki.write(f"{deck}\t{card}\n")

if __name__ == "__main__":
    pass