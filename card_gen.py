from enum import Enum

# Class should be given a front and back plain text as to be able to create proper cards

# Delimiting character is |

# Front:
#   {Front content}
# Back:
#   {Back content}

# Types of text encountered
#   Unformatted
#   Grammar Indicator

class TextType (Enum):
    fem = 0,
    masc = 1,
    neut = 2,
    nom = 3,
    acc = 4,
    dat = 5,
    gen = 6,


test_str1 = "-You-<nominative> have seen -the first person-<accusative>"
test_str2 = "-I-<nominative> want to see -you-<accusative> on tuesday. -You-<nominative> do not want to see -me-<accusative>."

class CardGenerator:
    def __init__(self, content: str="Example Front|Example Back"):
        # contents: list[str] = self.split_into_sides(content)
        pass

    def split_into_sides(self, combined: str):
        contents: list[str] = combined.split("|")
        front: str = contents[0]
        back: str = contents[1]

    def parse_content(self, content: str):
        results: list[str] = list()

        no_grammar, grammar, ind = self.find_chunk(content)

        if no_grammar != "":
            results.append(no_grammar)
        results.append(grammar)

        while ind != -1:
            print(ind)
            n_g, g, ind = self.find_chunk(content, ind)

            if n_g != "":
                results.append(n_g)
            if g != ("", ""):
                results.append(g)

        return results

    def find_chunk(self, content: str, start_ind=0) -> list[str, tuple[str], int]:
        # Find the content that is marked for gramaticalization
        ind1 = content.find("-", start_ind)

        if ind1 == -1:
            return [content[start_ind:len(content)], ("", ""), -1]

        ind2 = content.find("-", ind1 + 1)
        # Find the grammaticalization rules
        g_ind1 = content.find("<", ind1)
        g_ind2 = content.find(">", g_ind1 + 1)

        return [content[start_ind:ind1], (content[ind1+1:ind2], content[g_ind1+1:g_ind2]), g_ind2+1] # The plus one in the first part of the slice is to remove the delimiting marker from the resulting chunk

if __name__ == "__main__":
    gen = CardGenerator()
    print(gen.parse_content(test_str2))