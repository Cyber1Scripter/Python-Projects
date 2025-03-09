import curses
import time

def animate_cat(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(1)  # Make getch non-blocking
    stdscr.timeout(100)  # Set delay for animation

    cat_frames = [
        [
            "   ,     ,",
            "   |\\_,-~/",
            "   \\_  _/",
            "  (  @ @  )",
            "   |   \"   |",
            "   |  -^-  |",
            "    \__|__/",
            "  /        \\",
            " /          \\",
            "/            \\",
            "\  ||  ||  ||  || /",
            " \_oo__oo__oo__o_/"
        ],
        [
            "   ,     ,",
            "   |\\_,-~/",
            "   \\_  _/",
            "  (  @.@  )",
            "   |   \"   |",
            "   |  -^-  |",
            "    \__|__/",
            "  /        \\",
            " /          \\",
            "/            \\",
            "\  ||  ||  ||  || /",
            " \_oo__oo__oo__o_/"
        ]
    ]

    frame_index = 0
    y, x = 5, 10  # Starting position
    direction = 1  # Movement direction

    while True:
        stdscr.clear()
        for i, line in enumerate(cat_frames[frame_index]):
            stdscr.addstr(y + i, x, line)
        stdscr.refresh()
        
        frame_index = (frame_index + 1) % len(cat_frames)
        y += direction

        if y >= 10 or y <= 5:  # Bounce between two heights
            direction *= -1

        time.sleep(0.2)
        key = stdscr.getch()
        if key == ord('q'):  # Press 'q' to exit
            break

curses.wrapper(animate_cat)

