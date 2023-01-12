# Class should be given a front and back plain text as to be able to create proper cards

# Delimiting character is "\t"

# Front:
#   {Front content}
# Back:
#   {Back content}

# Types of text encountered
#   Unformatted
#   Grammar Indicator

# Valid Grammar Indicators
#   nom
#   acc
#   dat
#   gen
#   masc
#   fem
#   neut



class CardGenerator:
    def __init__(self, path, deck_provided=False, options_included=False):
        if deck_provided and options_included:
            self.to_process = self.read_from_origin(path)
            self.processed = list()

            self.opts = [line.rstrip("\n") for line in self.to_process if "#" in line]

            for line in self.to_process[len(self.opts):len(self.to_process)]:
                print(f"Processing line: {line}")
                contents: list[str] = self.split_into_sides_and_process_decks(line)
                self.processed.append("\t".join(contents))
            
            self.opts_included_processed = [*self.opts, *self.processed]

        elif deck_provided:
            self.to_process = self.read_from_origin(path)
            self.processed = list()

            for line in self.to_process:
                print(f"Processing line: {line}")
                contents: list[str] = self.split_into_sides_and_process_decks(line)
                self.processed.append("\t".join(contents))

        elif options_included:
            self.to_process = self.read_from_origin(path)
            self.processed = list()

            self.opts = [line.rstrip("\n") for line in self.to_process if "#" in line]

            for line in self.to_process[len(self.opts):len(self.to_process)]:
                print(f"Processing line: {line}")
                contents: list[str] = self.split_into_sides_and_process(line)
                self.processed.append("\t".join(contents))
            
            self.opts_included_processed = [*self.opts, *self.processed]

        else:
            self.to_process = self.read_from_origin(path)
            self.processed = list()

            for line in self.to_process:
                print(f"Processing line: {line}")
                contents: list[str] = self.split_into_sides_and_process(line)

                self.processed.append("\t".join(contents))

    def split_into_sides_and_process(self, combined: str):
        contents: list[str] = combined.split("\t")
        front: str = contents[0]
        back: str = contents[1]
        
        return [self.process_card_content(front), self.process_card_content(back)]

    def split_into_sides_and_process_decks(self, combined_w_deck: str):
        contents: list[str] = combined_w_deck.split("\t")
        front = contents[1]
        back = contents[2]

        return [contents[0], self.process_card_content(front), self.process_card_content(back)]

    def parse_content(self, content: str) -> list[str | tuple[str, str]]:
        results: list[str | tuple[str, str]] = list()

        no_grammar, grammar, ind = self.find_chunk(content)

        if no_grammar != "":
            results.append(no_grammar)
        results.append(grammar)

        while ind != -1:
            n_g, g, ind = self.find_chunk(content, ind)

            if n_g != "":
                results.append(n_g)
            if g != ("", ""):
                results.append(g)

        return results

    def find_chunk(self, content: str, start_ind=0) -> list[str | tuple[str, str] | int]:
        # Find the content that is marked for gramaticalization
        ind1 = content.find("-", start_ind)

        if ind1 == -1:
            return [content[start_ind:len(content)], ("", ""), -1]

        ind2 = content.find("-", ind1 + 1)
        # Find the grammaticalization rules
        g_ind1, g_ind2 = self.find_grammar_info(content, ind1)

        return [content[start_ind:ind1], (content[ind1+1:ind2], content[g_ind1+1:g_ind2]), g_ind2+1] # The plus one in the first part of the slice is to remove the delimiting marker from the resulting chunk

    def find_grammar_info(self, content: str, start_ind: int):
        g_ind1 = content.find("<", start_ind)
        g_ind2 = content.find(">", g_ind1 + 1)

        return [g_ind1, g_ind2]

    def encode_content(self, parsed_list: list) -> str:
        result = ""

        for item in parsed_list:
            if type(item) == str:
                result += item
            else:
                if item[1] == "nom":
                    result += f'<span style="text-decoration: underline; text-decoration-color: green">{item[0]}</span>'
                if item[1] == "acc":
                    result += f'<span style="text-decoration: underline; text-decoration-color: red">{item[0]}</span>'
                if item[1] == "dat":
                    result += f'<span style="text-decoration: underline; text-decoration-color: blue">{item[0]}</span>'
                if item[1] == "gen":
                    result += f'<span style="text-decoration: underline; text-decoration-color: orange">{item[0]}</span>'
                if item[1] == "masc":
                    result += f'<span style="color: blue">{item[0]}</span>'
                if item[1] == "fem":
                    result += f'<span style="color: red">{item[0]}</span>'
                if item[1] == "neut":
                    result += f'<span style="color: green">{item[0]}</span>'
        
        return result

    def process_card_content(self, content: str) -> str:
        return self.encode_content(self.parse_content(content))

    def read_from_origin(self, path: str) -> list[str]:
        lines = list()

        with open(path, "r", encoding="utf-8") as origin:
            lines = origin.readlines()
        
        return lines

    def write_to_dest(self, path: str, contents: str):
        with open(path, "w", encoding="utf-8") as dest:
            for content in contents:
                dest.write(content)

from sys import argv

if __name__ == "__main__":
    gen = CardGenerator(f"{argv[1]}.txt", deck_provided=True, options_included=True)