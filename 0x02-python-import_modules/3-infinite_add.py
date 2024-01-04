#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    cnt = len(sys.argv) -1

    if cnt == 0:
        print("0")
    else:
        nm = 0
        for c in range(1, cnt + 1):
            nm += int(sys.argv[c])
        print("{}".format(int(nm)))
