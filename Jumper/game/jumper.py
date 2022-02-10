class Jumper:

    def __init__ (self):
        pass
    def _print_jumper(self, score):
        print_list = [
        [" ____"],
        ["\____/"],
        [" \  /"],
        ["  \/"],
        ["  O"],
        [" /|\\"],
        [" /\\"]]

        for i in print_list[score:len(print_list)]:
            print(*i, sep="")