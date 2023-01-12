class AnkiExportParser:
    def __init__(self, path):
        self.contents: list[str] = self.read_from_export_txt(f"{path}.txt")

    def read_from_export_txt(self, path):
        with open(path, "r", encoding="utf-8") as org:
            lines = org.readlines()
            return lines[3:len(lines)]

if __name__ == "__main__":
    parser = AnkiExportParser("AllDecksTesting")
    print(parser.contents)