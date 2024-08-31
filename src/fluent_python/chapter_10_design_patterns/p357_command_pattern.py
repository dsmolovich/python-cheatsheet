class Document:
    def __init__(self, name) -> None:
        self._name = name
        self._text = ''
    
    def open(self):
        print(f'Opens document \'{self._name}\'')
    
    def close(self):
        print(f'Closes document \'{self._name}\'')
    
    def save(self) -> bool:
        print(f'Saves document \'{self._name}\'')
        return True

    def copy(self, position: int, length: int):
        return_value = self._text[position:position+length]
        print(f'Copies \'{return_value}\' from the document ({position}-{length}). Text is now: \'{self._text}\'')
        return return_value

    def cut(self, position: int, length: int):
        return_value = self._text[position:position+length]
        new_text = self._text[:position] + self._text[position+length:]
        self._text = new_text
        print(f'Cuts \'{return_value}\' from the document ({position}-{length}). Text is now: \'{self._text}\'')
        return return_value

    def paste(self, text: str, position: int):
        new_text = self._text[:position] + text + self._text[position:]
        self._text = new_text
        print(f'Pastes \'{text}\' into the the document at position {position}. Text is now: \'{self._text}\'')
        return True

class Application:
    def add_document(self, document: Document):
        self._document = document

    def get_document(self):
        return self._document

application = Application()

def open_command(name: str) -> bool:
    document = Document(name=name)
    application.add_document(document=document)
    document.open()
    return True

def save_command() -> bool:
    document = application.get_document()
    return document.save()

def close_command() -> None:
    document = application.get_document()
    return document.close()

def paste_command(text: str, position: int):
    document = application.get_document()
    return document.paste(text=text,
                          position=position)

def copy_command(position: int, length: int):
    document = application.get_document()
    return document.copy(position=position,
                         length=length)

def cut_command(position: int, length: int):
    document = application.get_document()
    return document.cut(position=position,
                         length=length)

class MacroCommand:
    """A command that executes a list of commands"""
    def __init__(self, commands) -> None:
        self._commands = list(commands)

    def __call__(self):
        for command in self._commands:
            command()

open_paste_save_close_command = MacroCommand([lambda: open_command(name="New Document"),
                                        lambda: paste_command(position=0, text="The quick brown fox jumps over the lazy dog."),
                                        lambda: save_command(),
                                        lambda: close_command()])

def _doctest_it():
    """
    >>> open_command(name="Some Document")
    Opens document 'Some Document'
    True

    >>> paste_command(position=0, text="The quick brown fox jumps over the lazy dog.")
    Pastes 'The quick brown fox jumps over the lazy dog.' into the the document at position 0. Text is now: 'The quick brown fox jumps over the lazy dog.'
    True

    >>> cut_command(position=4, length=15)
    Cuts 'quick brown fox' from the document (4-15). Text is now: 'The  jumps over the lazy dog.'
    'quick brown fox'

    >>> paste_command(text="blue slow elephant", position=4)
    Pastes 'blue slow elephant' into the the document at position 4. Text is now: 'The blue slow elephant jumps over the lazy dog.'
    True

    >>> save_command()
    Saves document 'Some Document'
    True

    >>> close_command()
    Closes document 'Some Document'

    >>> open_paste_save_close_command()
    Opens document 'New Document'
    Pastes 'The quick brown fox jumps over the lazy dog.' into the the document at position 0. Text is now: 'The quick brown fox jumps over the lazy dog.'
    Saves document 'New Document'
    Closes document 'New Document'
    """
