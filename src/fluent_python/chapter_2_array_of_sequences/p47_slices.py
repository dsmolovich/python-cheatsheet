
address_book = """
0...........12..............28..................48................
John        Doe             +1(416)567.3456     john.doe@gmail.com
Steven      Pearce          +1(905)212.5678     spearce@yahoo.com
Frank       Frakhofost      +1(219)345.4412     franky@gmail.com
"""

FIRST_NAME = slice(0, 12)
LAST_NAME = slice(12, 28)
PHONE_NUMBER = slice(28, 48)
EMAIL = slice(48, None)

line_items = address_book.split("\n")[2:]

def populate_people():
    """
    >>> populate_people()
    John Doe john.doe@gmail.com
    Steven Pearce spearce@yahoo.com
    Frank Frakhofost franky@gmail.com
    """
    for line_item in line_items:
        if line_item:
            print(line_item[FIRST_NAME].strip(),
                line_item[LAST_NAME].strip(),
                line_item[EMAIL].strip())
