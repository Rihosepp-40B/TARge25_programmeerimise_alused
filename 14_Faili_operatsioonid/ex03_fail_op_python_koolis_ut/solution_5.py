"""Ülesanne 5
Palindroomiks nimetatakse sõna (ka sõnaühendit), mis on nii vasakult paremale kui paremalt vasakule lugedes
täpselt ühesugunem (näit. "kook", "kuulilennuteetunneliluuk" jne). Loo programm, mis trükib ekraanile välja
kõik tekstifailis olevad sõnad, mis on palindroomid. Alustekstiks võid kasutada suvalist teksti, kuid katsetada
tasuks ka sõnaloenditega, kus iga sõna asub eraldi real (näit. eesti keele sõnade algvormid e. lemmad veebilehelt
http://www.eki.ee/tarkvara/wordlist/)."""


def create_file(filename: str, content):
    with open(filename, "w", encoding="UTF-8") as f:
        f.write(content)


# def read_text_to_list(filename: str):
#     with open(filename, "r", encoding="UTF-8") as f:
#         words = f.read().lower().split()
#     return words
#
#
# def find_palindrome_words(word_list: list):
#     for word in word_list:
#         if word[::-1] == word:
#             print(word)
#         else:
#             pass


def is_palindrome(word: str) -> bool:
    return word[::-1] == word


def find_palindrome_in_file(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as f:
        for line in f:
            word = line.lower().strip()
            if len(word) > 1 and is_palindrome(word):
                print(word)


if __name__ == '__main__':
    filename = "palindrome.txt"
    content = """Kook panni peal Kuulilennuteetunneliluuk on paras pähkel"""
    #create_file(filename, content)
    # word_list = read_text_to_list(filename)
    print(f"failis {filename} on järgnevad sõnad palindroomid")
    # find_palindrome_words(word_list)
    find_palindrome_in_file(filename)