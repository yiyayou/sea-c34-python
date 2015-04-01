# taks10 safe_input.py


def safe_input():
    """This function catch excepition from raw_input function and return None"""
    try:
        raw_input()
    except (EOFError, KeyboardInterrupt):
        return None
