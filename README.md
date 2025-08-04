📄 Description:

    load_notes() is a helper function that loads existing notes from a local JSON file.

        If the file does not exist or is empty, it returns an empty list.

        If the file contains valid JSON data, it parses and returns it as a Python list of note objects.

        In case of any read or decode error, it catches the exception and returns an empty list with a printed error message.

    This function ensures robust handling of data loading to prevent crashes due to missing or malformed files.
