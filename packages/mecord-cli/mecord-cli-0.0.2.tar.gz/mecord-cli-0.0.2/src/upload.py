
import sftp_upload
from pathlib import Path

def upload(src):
    file_name = Path(src).name
    oss_path = f"ftp://192.168.3.220/1TB01/data/mecord/{file_name}"
    sftp_upload.upload(src, file_name)
    return oss_path