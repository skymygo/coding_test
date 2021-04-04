import re
def solution(new_id):
    new_id = new_id.lower()
    new_id = new_id.replace("-", "A",).replace("_", "B").replace(".", "C")
    new_id =  re.sub('[^a-zA-Z0-9]','',new_id).strip()
    before_len = 0
    while before_len != len(new_id):
        before_len = len(new_id)
        new_id = new_id.replace("CC", "C")
    while new_id.startswith("C"):
        new_id = new_id[1:]
    new_id = new_id[:15]
    while new_id.endswith("C"):
        new_id = new_id[:-1]
    if new_id == '':
        new_id = 'aaa'

    while len(new_id) <3:
        new_id += new_id[-1]
    new_id = new_id.replace("A", "-").replace("B","_").replace("C", ".")

    return new_id


if __name__ == '__main__':
    input = ["...!@BaT#*..y.abcdefghijklm", "z-+.^.", "=.=", "123_.def", "abcdefghijklmn.p"]
    output = ["bat.y.abcdefghi", "z--", "aaa", "123_.def", "abcdefghijklmn"]

    for _input, _output in zip(input, output):
        res = solution(_input)
        print('{}, input: {}, output: {}, predict: {}'.format(res==_output, _input, _output, res))

