import sys
import getopt
import random
from spammer import Spammer


def main(argv):
    delay = 5
    text = "Sample"
    is_splitted = False
    count = 1
    suffix = "\n"
    single_delay = 0
    try:
        opts, args = getopt.getopt(argv, "hd:t:s:c:l", [
                                   "delay=", "text=", "is-splitted=", "count=", "line-ending=", "single-delay="])
    except getopt.GetoptError as err:
        print("Wrong format")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("spammer -d <delay: seconds> -t <text_to_spam: string> -c <repetition_count: int> -s <is_text_splitted: boolean> -l <line_ending: string>")
            sys.exit()
        elif opt in ("-d", "--delay"):
            delay = float(arg)
        elif opt in ("-t", "--text"):
            text = arg
        elif opt in ("-s", "--is-splitted"):
            is_splitted = arg.lower()[0] == "t"
        elif opt in ("-c", "--count"):
            count = int(arg)
        elif opt in ("-l", "--line-ending"):
            suffix = arg
        elif opt == "--single-delay":
            single_delay = float(arg)
    spammer = Spammer(text = text, spamc = count, init_delay = delay, is_splitted = is_splitted, suffix = suffix)
    spammer.run()


if __name__ == "__main__":
    main(sys.argv[1:])
