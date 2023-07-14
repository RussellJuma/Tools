class File:

    @classmethod
    def open(cls, file_path: str, method: str = 'r') -> str or bytes:
        """

        :param file_path: (str) file_path
        :param method: (str) r or rb
        :return: file_contents
        """
        try:
            with open(file_path, method) as file:
                file_contents = file.read()
            return file_contents
        except UnicodeDecodeError:
            print('File mode changing to rb')
            return cls.open(file_path, 'rb')
