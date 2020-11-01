"""
Get notes (Meal, Diaper etc)
"""
import json

from lg.lib.auth import Session
from lg.lib.entities.enrollments import Enrollments
from lg.lib.entities.notes import Notes


def main(email, password):
    session = Session(email, password)
    enrollments = Enrollments(session).get()

    select = {}
    for i, enrollment in enumerate(enrollments, 1):
        select[i] = enrollment["id"]
        print("{}: {}".format(i, enrollment["display_name"]))

    choice = input("Pick one: ")

    notes = Notes(session).get(select[int(choice)])

    print(json.dumps(notes, indent=4, sort_keys=True))


if __name__ == "__main__":
    import argparse
    import getpass

    parser = argparse.ArgumentParser()
    parser.add_argument("email", help="Email")
    args = parser.parse_args()

    password = getpass.getpass("Password: ")

    main(args.email, password)
