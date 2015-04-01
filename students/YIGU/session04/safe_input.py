# taks10 safe_input.py


def safe_input(i):
    """This function catch excepition from raw_input function and return None"""
    try:
        raw_input(i)
    except (EOFError, KeyboardInterrupt):
        return None
