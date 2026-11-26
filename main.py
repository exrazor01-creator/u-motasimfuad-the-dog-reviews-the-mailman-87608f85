"""The Dog Reviews the Mailman -- make.fun one-liner entry.

The line is a one-star review written by the dog itself, in first person,
about the one visitor who shows up every single day and never stays.
The joke turns on the dog's two obsessions colliding: the mailman smells
of every other dog on the street -- the most exciting smell in the world
-- and yet he always leaves before the dog can properly sniff his bag.
The grievance is pure dog logic (a stranger who smells that interesting
should stay and be sniffed), and the closing "The audacity" is the dog
filing its formal complaint in the voice of an outraged customer.
"""

import os

# The entry: a dog's one-star review of the mailman.
# He arrives daily smelling of every dog on the street, then leaves
# without letting the reviewer sniff his bag -- the ultimate insult
# from a dog's point of view, delivered with customer-review outrage.
LINE = "One star. He comes every day smelling of every dog on the street, then leaves without letting me sniff his bag. The audacity."


def validate(text):
    """Check that a candidate entry line meets the competition rules.

    Raises ValueError unless ``text`` is a non-blank single-line ASCII
    string of 1 to 200 characters, with no leading or trailing space and
    no double spaces.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1 to 200 characters")
    if not text.isascii():
        raise ValueError("entry must be ASCII only")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be blank")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing space")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")


def main():
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="ascii") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
