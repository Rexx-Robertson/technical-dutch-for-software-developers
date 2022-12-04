#!/usr/bin/env python

import uuid


SCHEIDINGSTEKEN = '\t'


# TE DOEN: Vertaal alles
def main():
    iterate_file("../contents/01_ADJECTIVES_ADVERBS.txt", "../anki/01_ADJECTIVES_ADVERBS_DECK.txt", proces_regel_adjectives)
    iterate_file("../contents/02_NOUNS.txt", "../anki/02_NOUNS_DECK.txt", proces_regel_nouns)
    iterate_file("../contents/03_VERBS.txt", "../anki/03_VERBS_DECK.txt", proces_regel_verbs)


def iterate_file(van_bestandsnaam, naar_bestandsnaam, bewerkin):
    eerst = True

    with open(van_bestandsnaam, 'r') as in_file:
        with open(naar_bestandsnaam, 'w') as out_file:
            for in_regel in in_file.readlines()[3:]:
                if eerst:
                    eerst = False
                else:
                    out_file.write('\n')

                out_file.write(bewerkin(in_regel))


def proces_regel_adjectives(regel):
    uitvoer = [x.strip() for x in regel.split("  ") if x != '']
    uitvoer.append(str(uuid.uuid4()))
    return SCHEIDINGSTEKEN.join(uitvoer)


def proces_regel_nouns(regel):
    componenten = [x.strip() for x in regel.split(" ") if x != '']
    uitvoer = []
    uitvoer.append(' '.join(componenten[:2]))
    uitvoer.append(' '.join(componenten[2:]))
    uitvoer.append(str(uuid.uuid4()))
    return SCHEIDINGSTEKEN.join(uitvoer)


def proces_regel_verbs(regel):
    componenten = []
    for x in regel.split("  "):
        componenten += x.split("\t")
    componenten = [y.strip() for y in componenten if y != '']
    uitvoer = []
    uitvoer.append(componenten[0])

    # TE DOEN Ik begrijp deze kolommen niet, bezoek ze opnieuw na verdere studies

    uitvoer.append("; ".join(componenten[4:]))

    uitvoer.append(str(uuid.uuid4()))

    return SCHEIDINGSTEKEN.join(uitvoer)


if __name__ == "__main__":
    main()