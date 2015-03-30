def safe_input():
    try:
        user_input = raw_input("Type your input: ")
        print user_input
    except (EOFError, KeyboardInterrupt):
        return "None"

safe_input()
