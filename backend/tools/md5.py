import hashlib
from fastapi import UploadFile


async def get_file_md5(file: bytes):
    md5 = hashlib.md5()
    md5.update(file)
    return md5.hexdigest()
