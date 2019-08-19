import journal
import string_formating

def main():
    print_header()
    run_event_loop()


def print_header():
    print("-------------------------")
    print("      Journal App")
    print("-------------------------\n")

def run_event_loop():
    print("What do you want to do with your journal?")
    cmd = 'EMPTY'
    journal_name = "default"
    journal_data = journal.load(journal_name)

    while cmd != 'X' and cmd:
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.upper().strip() 
        if cmd == 'L':
            list_entries(journal_data)
        elif cmd == 'A':
            add_entry(journal_data)
        elif cmd != 'X' and cmd:
            print("Sorry, we don't understand {}.".format(cmd))  
    print("\nGoodbye.")
    journal.save(journal_name, journal_data)

def list_entries(data):
    entries = reversed(data)
    if len(data) == 0:
        print("Your journal is empty.")
    else:
        print("---------------------")
        print("Your Journal Entries:")
        print("---------------------")
        for idx, entry in enumerate(entries):
            print("\n[{}.]\n{}\n".format(idx + 1, string_formating.wrap_text(entry)))
        print("---------------------\n")
        

def add_entry(data):
    text = input("Type your entry, <ENTER> to exit : ")
    journal.add_entry(text, data)
    # data.append(text)

if __name__ == "__main__":
    main()

