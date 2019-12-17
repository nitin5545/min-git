import os


def init():
    try:
        os.mkdir(".min-git")
        os.mkdir(".min-git/branches")
        os.mkdir(".min-git/info")
        os.mkdir(".min-git/objects")
        os.mkdir(".min-git/refs")
        open(".min-git/HEAD").close()
        print("Initialized an empty min-git repository")

    except OSError as e:
        print(e)


if __name__ == '__main__':
    init()
