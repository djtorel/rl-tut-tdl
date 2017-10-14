import sys

import tdl


def main():
    # Set screen dimensions
    screen_width = 80
    screen_height = 50

    tdl.set_font("font/arial12x12.png", greyscale=True, altLayout=True)

    root_console = tdl.init(screen_width, screen_height,
                            title='Roguelike Tutorial')

    while not tdl.event.is_window_closed():
        root_console.draw_char(40, 25, '@', bg=None, fg=(255, 255, 255))
        tdl.flush()

        root_console.draw_char(1, 1, ' ', bg=None)

        for event in tdl.event.get():
            if event.type == 'KEYDOWN':
                user_input = event
                break
        else:
            user_input = None

        if not user_input:
            continue

        if user_input.key == 'ESCAPE':
            sys.exit()


if __name__ == '__main__':
    main()
