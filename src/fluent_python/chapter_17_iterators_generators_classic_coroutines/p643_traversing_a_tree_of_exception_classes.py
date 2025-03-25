def tree(cls, level: int = 0):
    yield cls.__name__, level
    for sub_cls in cls.__subclasses__():
        yield from tree(cls=sub_cls,
                        level=level+1)

def display(cls):
    for cls_name, level in tree(cls=cls):
        indent = ' ' * 4 * level
        print(f'{indent}{cls_name}')


def doctest():
    """
    >>> display(Exception)
    Exception
        ArithmeticError
            FloatingPointError
            OverflowError
            ZeroDivisionError
        AssertionError
        AttributeError
            FrozenInstanceError
        BufferError
        EOFError
        ImportError
            ModuleNotFoundError
            ZipImportError
        LookupError
            IndexError
            KeyError
            CodecRegistryError
        MemoryError
        NameError
            UnboundLocalError
        OSError
            BlockingIOError
            ChildProcessError
            ConnectionError
                BrokenPipeError
                ConnectionAbortedError
                ConnectionRefusedError
                ConnectionResetError
            FileExistsError
            FileNotFoundError
            InterruptedError
            IsADirectoryError
            NotADirectoryError
            PermissionError
            ProcessLookupError
            TimeoutError
            UnsupportedOperation
            itimer_error
            Error
                SameFileError
            SpecialFileError
            ExecError
            ReadError
        ReferenceError
        RuntimeError
            NotImplementedError
            RecursionError
            _DeadlockError
        StopAsyncIteration
        StopIteration
        SyntaxError
            IndentationError
                TabError
        SystemError
            CodecRegistryError
        TypeError
        ValueError
            UnicodeError
                UnicodeDecodeError
                UnicodeEncodeError
                UnicodeTranslateError
            UnsupportedOperation
        Warning
            BytesWarning
            DeprecationWarning
            EncodingWarning
            FutureWarning
            ImportWarning
            PendingDeprecationWarning
            ResourceWarning
            RuntimeWarning
            SyntaxWarning
            UnicodeWarning
            UserWarning
        ExceptionGroup
        error
        _OptionError
        _Error
        TokenError
        StopTokenizing
        ClassFoundException
        EndOfBlock
        BdbQuit
        Error
        Restart
        SkipTest
        _ShouldStop
        _UnexpectedSuccess
        ArgumentError
        ArgumentTypeError
        DocTestFailure
        UnexpectedException
        Error
        error
        LZMAError
        RegistryError
        _GiveupOnFastCopy
    """