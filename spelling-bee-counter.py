#!/opt/homebrew/bin/python

# jna@retina.net
# John Adams
# 
# count the number of starting two letter combinations in a file of words
# useful for solving spelling bee

import sys

def main():
    # open and read the file line by line
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    # count the number of words starting with each two letter combination
    counts = {}
    for line in lines:
        line = line.strip()
        if len(line) < 2:
            continue
        key = line[0:2]
        if key in counts:
            counts[key] += 1
        else:
            counts[key] = 1

    # sort the keys
    keys = list(counts.keys())
    keys.sort()
    
    sorted_dict = {i: counts[i] for i in keys}
    # print the counts
    for key in sorted_dict:
        print(key.upper(), counts[key])

if __name__ == "__main__":
    # make sure there is one and only one argument
    if len(sys.argv) != 2:
        print("Usage: python3 spelling-bee-counter.py <file>")
        sys.exit(1)

    main()
