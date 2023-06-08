import hidden_4
if __name__ == "__main__":
    names = dir(hidden_4)
    for name in names:
        if not name.startwith("_"):
            print(name)
