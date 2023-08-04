import sys

DB_PHONES = {}


def input_error(func):
    def wrapped(*args):
        try:
            return func(args[0])
        except IndexError:
            return "This command 'add', you must write - 'add' 'name' 'number'"
        except KeyError:
            return "This command 'phone', you must write - 'phone' 'name'"
        except ValueError:
            return "This command 'change', you must write - 'change' 'name' 'number'"
    return wrapped


@input_error
def add_phone(*args):
    if len(args[0]) != 3:
        raise IndexError
    DB_PHONES.update({args[0][1]: args[0][2]})
    return "You add new contact"


@input_error
def change_phone(*args):
    if len(args[0]) != 3:
        raise ValueError
    for k in DB_PHONES.keys():
        if k == args[0][1]:
            DB_PHONES[k] = args[0][2]
    return f"Contact {args[0][1].title()} was changed"


@input_error
def get_phone(*args):
    if len(args[0]) != 2:
        raise KeyError
    result = DB_PHONES.get(args[0][1])
    return f'Contact {args[0][1].title()} find:\n {result}'


def greeting(*args):
    return "How can I help you?"


def get_contacts(*args):
    list = []
    for k, v in DB_PHONES.items():
        _ = k.title() + ' ' + str(v)
        list.append(_)
        contact_list = ('\n').join(list)
    return f'Contacts list:\n{contact_list}'


COMMANDS = {
    "add": add_phone,
    "change": change_phone,
    "show all": get_contacts,
    "hello": greeting,
    "hi": greeting,
    "phone": get_phone,
}


def main():
    while True:
        user_input = input(">>> ")
        user_input_lower = user_input.lower()
        list = user_input_lower.split(' ')
        for k, v in COMMANDS.items():
            if user_input_lower.startswith(k):
                print(v(list))
            elif user_input_lower in ['good bye', 'exit', 'close']:
                print("Good bye!")
                sys.exit()
            
            
if __name__ == "__main__":
    main()