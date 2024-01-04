#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    allnames = dir(hidden_4)
    for name in allnames:
        if name[:2] != "__":
            print(name)
