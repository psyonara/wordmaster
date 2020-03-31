import curses


VALID_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def start_game(screen: curses.initscr()):
    curses.curs_set(0)
    curses.noecho()
    curses.cbreak()

    screen.clear()

    screen.addstr(0, 0, "Secret Word: ")

    screen.refresh()
    word_chars = ""
    while True:
        c = screen.getch()
        ch = chr(c).upper()
        if len(word_chars) < 4 and ch in VALID_LETTERS:
            word_chars += ch
            screen.addstr(ch.upper())
            screen.refresh()

        if len(word_chars) == 4:
            break

    screen.getkey()

def main():
    print("Starting Wordmaster...")
    curses.wrapper(start_game)


if __name__ == "__main__":
    main()
