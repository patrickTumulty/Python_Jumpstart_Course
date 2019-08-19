import os

def load(name):
    '''
    This method creates and loads a new journal.

    : param name: This base name of journal to load.
    : return: A new journal data structure populated with the file data.
    '''
    data = []
    filename = get_full_pathname(name)
    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())
    return data


def save(name, journal_data):
    filename = get_full_pathname(name)
    print("....... saving to: {}".format(filename))
    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')


def add_entry(data, journal_data):
    journal_data.append(data)


def get_full_pathname(name):
    filename = os.path.abspath(os.path.join('.','Daily Journal/journals/' + name + '.jrl'))
    return filename


