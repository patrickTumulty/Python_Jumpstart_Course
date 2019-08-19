

def wrap_text(string):
    line_length = 50
    bp = int(len(string) / line_length)
    if bp == 0:
        return string
    else:
        num_loop = 0
        while num_loop < bp:
            num_loop += 1
            string = string[:line_length * num_loop] + "\n" + string[line_length * num_loop:]
        return string

