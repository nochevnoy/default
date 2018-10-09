import re

def count_smileys(arr):
    num = 0
    for x in arr:
        if re.match('[;:][-~]?[)D]', x):
            num += 1
    return num