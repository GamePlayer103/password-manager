import sys

def print_help():
    msg = (
        'usage:\n'
        '\tnew - add new password\n'
        '\tlist - print saved passwords\n'
        '\tedit - edit saved password\n'
    )
    print(msg)

if __name__ == '__main__':
    try:
        arg = sys.argv[1].lower()
    except IndexError:
        print_help()
        sys.exit()

    if arg == 'new':
        pass
    elif arg == 'list':
        pass
    elif arg == 'edit':
        pass
    else:
        print_help()