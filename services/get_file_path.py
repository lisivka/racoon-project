import os
import uuid


def get_path_with_unique_filename(instance, file_name: str, file_path: str) -> str:
    """
    Method to generate unique file path and name using UUID
        :param file_name: name of the file
        :param file_path: path where file should be saved
        :return: file path with unique file name
    """
    # get input file extension
    ext = file_name.strip().split('.')[-1]
    return os.path.join(f'{file_path}', f'{uuid.uuid4()}.{ext}')
