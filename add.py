# adds file to staging area
# put the current staging area file in index file have various parameter
# creates blob node or tree node depending on item being staged

# so there is one top level tree node for each subdirs and blobs at that level
# commit node is just pointer to tree node
# when we make changes to file currently in the tree we update the pointer in its parent tree node
# to change in next commit
# for every commit we make a new tree node if the tree node exists we copy its pinters and make a new
# hash value for new tree node

# index file contains all the files and their path

# my idea to make tree node will be to hash the path of file in tree substructure
# in this way we can easily make new tree node if changes happen by finding all nodes at same level
# directory structure and are not affected
# index file will contain only one entry per file


# index file will have format as
# staging_type sha1_hash file_path


# TODO if already in index and file hash is same then do not to index
import os
import hash
import path


def to_index(sha1_hash, file):
    staging_type = b'S'
    line = staging_type + b' ' + bytes(sha1_hash, encoding="utf-8") + b' ' + bytes(file, encoding="utf-8")
    with open(path.INDEX_PATH, "ab") as fp:
        fp.write(line)
        fp.write(b"/n")


def add_files(file_paths):
    n = len(file_paths)

    all_files = set()
    # extract files from given list
    for i in range(n):
        if os.path.exists(file_paths[i]) and os.path.isdir(file_paths[i]):
            for root, dirs, files in os.walk(file_paths[i]):
                for file in files:
                    all_files.add(os.path.join(root, file))
        else:
            all_files.add(file_paths[i])

    # add all files
    for file in all_files:
        if os.path.exists(file):
            fp = open(file, "rb")
            content = fp.read()
            fp.close()
            sha1_hash = hash.hash_create(content, b'blob')
            to_index(sha1_hash, file)


def add(files):
    if isinstance(files, str):
        files = [files]

    add_files(files)


if __name__ == '__main__':
    add(['add.py', 'hash.py'])
