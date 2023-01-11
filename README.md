# Anki Card Creator

Utility to create Anki cards with my personal needs in mind (German)

## Valid Grammar Markings
- nom (Nominative case)
- acc (Accusative case)
- dat (Dative case)
- gen (Genitive case)
- masc (Masculine)
- fem (Feminine)
- neut (Neuter)

## Usage Syntax
-text content to be grammatically marked-<\grammatical information here> unmarked text here
unmarked text here -text content to be grammatically marked-<\grammatical information here>

## How to Use
Create a txt file with card content, the front content and back content are to be separated with the "|" character (do not put a space between the end of the front content and "|" and the front of the back content and "|"). Each individual card will be separated by a new line.

Example:
    -Inside example.txt-
        This is my -front-<\grammatical marking here> of the first card|This is the back of my first -card-<\grammatical content here>
        -This-<\grammatical marking here> is my front of the second card|This -is-<\grammatical marking here> the back of my second card
        This is my front of the third -card-<\grammatical marking here>|This is the back of my third card
        This is my front of the fourth card|This is the back of my fourth card

In order to process the text in this file, you will cd to the directory where card_gen.py is and move the text file to that directory, then type the command:
```
$ python card_gen.py <name of txt>
```
When entering the name of the txt file, DO NOT include the extension.