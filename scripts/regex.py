import re


def remove_newlines(filename):
    """Removes all newlines from a file"""
    with open(filename + ".txt", 'r') as f:
        text = f.read()

    n = re.compile('[\n]')
    m = n.finditer(text)

    for line in m:
        new_text = text.replace(text[line.start()], " ")

    with open(filename + "_NoNL" + ".txt", 'w') as f:
        f.write(new_text)


def make_start_end(filename):
    """Inputs start ('[S]') and end ('[E]') tokens in a file"""
    with open(filename + ".txt", 'r') as f:
        text = f.read()

    start = re.compile('[.?!”] +[A-Z“]')

    m = start.search(text)
    print(m)
    while m is not None:
        text = text[:m.end() - 1] + "[S]" + text[m.end() - 1:]
        text = text[:m.start() + 1] + "[E]" + text[m.start() + 1:]
        m = start.search(text)
        # print("Loading...")

    with open(filename + "_S&E.txt", 'w') as f:
        f.write(text)


if __name__ == '__main__':
    remove_newlines('text/ksbd')
    make_start_end('text/ksbd_NoNL')
    # make_start_end('scripts/text_Wheel_of_Time_NoNL')
