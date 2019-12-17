# generates hash of the file passed to it using sha-1 and zlib and stores it in directory
import os
import zlib
import hashlib
import path


def save_content(hash_content, content_hash):
    dir_name = content_hash[:2]
    file_name = content_hash[2:]
    dir_path = os.path.join(path.OBJECT_PATH, dir_name)
    file_path = os.path.join(dir_path, file_name)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

    with open(file_path, "wb") as fp:
        fp.write(hash_content)


def hash_create(content, content_type):
    header = content_type + b' ' + bytes(str(len(content_type)), encoding="utf-8")  # bytes header
    store = header + b' ' + content
    content_hash = hashlib.sha1(store).hexdigest()
    hash_content = zlib.compress(store)
    save_content(hash_content, content_hash)
    return content_hash


def hash_decode(content):
    uncompress = zlib.decompress(content)
    uncompress = uncompress.split(b' ')[2]
    return uncompress


if __name__ == "__main__":
    hash_create(b"hfww nwbdbdw bwbdwbdw wdhwdwbdw", b"blob")
