# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening.append(Bracket(next, i + 1))
            pass

        elif next in ")]}":
           if len(opening) == 0:
            return i + 1
            pass
        
recent_bracket = open.pop()

if !matching(recent_beacket.char, next):
    return i + 1

if len(opening) > 0:
    return opening[0].position

return "Success"

def main():
    text = input()
    mismatch = find_mismatch(text)
    if mismatch == "Success":
        print("Success")
    else:
        print(mismatch)


if __name__ == "__main__":
    main()
