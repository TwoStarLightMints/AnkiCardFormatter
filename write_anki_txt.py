class AnkiTxtWriter:
    def __init__(self, origin_file: str, separator:str="\t", html:str="false", deck_column:str="1", tags_column:str="4", deck:str="German Vocab::General"):
        self.card_contents = self.get_card_contents(origin_file)

    def get_card_contents(self, path):
        contents = list()
        
        with open(path, "r") as org:
            contents = org.readlines()
        
        return contents
    
    def create_anki_txt_file(self, sep: str, html: str, deck_col: str, tag_col: str, deck: str):
        with open("to_import.txt", "w") as anki:
            anki.write(f"#separator:{sep}")
            anki.write(f"html:{html}")
            anki.write(f"#deck column:{deck_col}")
            anki.write(f"tags column:{tag_col}")
            # From here on, write the different cards