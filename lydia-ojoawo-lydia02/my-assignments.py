import os
from datetime import datetime

class DuplicateVisitorError(Exception):
    pass

def get_last_visitor(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            if lines:
                last_line = lines[-1].strip()
                if last_line:
                    return last_line.split(',')[0]
        return None
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def add_visitor(filename, name):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        with open(filename, 'a') as f:
            f.write(f"{name},{timestamp}\n")
    except Exception as e:
        print(f"Error writing to file: {e}")


def main():
    filename = "visitors.txt"
    try:
        name = input("Enter visitor's name: ").strip()
        last_visitor = get_last_visitor(filename)
        if last_visitor and last_visitor.lower() == name.lower():
            raise DuplicateVisitorError(f"Duplicate visitor: {name}")
        add_visitor(filename, name)
        print(f"Welcome, {name}! Your visit has been recorded.")
    except DuplicateVisitorError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()