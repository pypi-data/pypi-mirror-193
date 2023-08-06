import sys

from .data import COMMON_VERBS
from .verb_conjugator import VerbConjugator


def main():
    vc = VerbConjugator()

    while True:
        user_selection = vc.display_menu()
        if user_selection == "1":
            vc.setup()
            vc.display_verb_conjugation()
        elif user_selection == "2":
            vc.setup()
            vc.drill_and_practice()
        elif user_selection == "3":
            vc.common_verbs_quiz(COMMON_VERBS)
        else:
            print("\nGoodbye!")
            sys.exit(0)


if __name__ == "__main__":
    main()
