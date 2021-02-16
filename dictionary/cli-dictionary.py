#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
import requests
import argparse
import threading
from random import randint
# from dictionary.language import language
from language import language
import anki

WORD_MEANING = []


def get_parser():
    parser = argparse.ArgumentParser(
        prog='cli-dictionary', description='welcome to cli-dictionary, never use a browser again to get a word meaning ;)')
    parser.add_argument('word', type=str, help='the word to be searched.')
    parser.add_argument(
        'lang', type=str, help='the language of the requested word.')
    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s 2.3.1')
    parser.add_argument('-s', '--synonyms', action='store_true',
                        help='display the synonyms of the requested word.')
    parser.add_argument('-e', '--examples', action='store_true',
                        help='display a phrase using the requested word.')

    group_anki = parser.add_argument_group('Anki-Flashcards')
    group_anki.add_argument(
        '--profile', help='select the profile', type=str)
    group_anki.add_argument(
        '--card', help='select the type of card', choices=['basic', 'basic-reverse', 'cloze'])

    return parser


def main(word, lang, *args):
    word = word.encode('utf-8')

    sy = ''  # synonyms
    ex = ''  # examples
    Anki = {}

    for arg in args:
        sy = arg[0]['synonyms']
        ex = arg[0]['examples']

        Anki = {
            'profile': arg[0]['profile'],
            'card': arg[0]['card']
        }

    # upper() because in list of language.py all the abbreviation are uppercased.
    lang = lang.upper()

    if lang in language:
        url = language[lang] + word.decode('utf-8')
        meaning(url, synonyms=sy, examples=ex)
    else:
        print("""
           select a valid language:
           en <english> | pt <portuguese>
           hi <hindi>   | es <spanish>
           fr <french>  | ja <japanese>
           ru <russian> | de <german>
           it <italian> | ko <korean>
           zh <chinese> | ar <arabic>
           tr <turkish>
       """)

    if Anki['profile'] == None and Anki['card'] == None:
        pass
    else:
        get_anki(profile=Anki['profile'], card=Anki['card'],
                 lang=lang, word=word.decode('utf-8'), meaning=WORD_MEANING)


def meaning(url, **kwargs):
    header = {
        "Accept": "charset=utf-8"
    }

    response = requests.request('GET', url, headers=header)

    data = json.loads(response.text.encode('utf-8'))

    for obj in data:

        meanings = obj['meanings'][0]['definitions']

        # always show the definition - default
        get_meaning(meanings, 'definition')

        if kwargs.get('examples'):
            get_data('EXAMPLES', meanings, 'example')

        if kwargs.get('synonyms'):
            # j- get index of the synonym
            get_data('SYNONYMS', meanings, 'synonyms', j=0)


def get_meaning(array_meanings, key):
    print('DEFINITIONS ----------------------')

    i = 0

    for element in array_meanings:
        i = i + 1
        # print(f'{str(i)}. {element[key]}')
        WORD_MEANING.append(f'{str(i)}. {element[key]}')

    for m in WORD_MEANING:
        print(m)


def get_data(title, array, key, **kwargs):
    try:
        i = 0
        print(title + ' ----------------------')

        j = kwargs.get('j')

        if j != 0:
            for element in array:
                i = i + 1
                print(f'{str(i)}. {element[key]}')
        else:
            for element in array:
                i = i + 1
                j = j + 1
                print(f'{str(i)}. {element[key][j]}')

    except (IndexError, TypeError):
        print('sorry, we could not find the word you are looking for :(')
        return

    except KeyError:
        return


def get_anki(**kwargs):
    print('ANKI ----------------------')
    # anki
    profile = kwargs.get('profile')
    card = kwargs.get('card')

    # dictionary info
    lang = kwargs.get('lang')
    word = kwargs.get('word')
    meaning = kwargs.get('meaning')

    rand_number = randint(1, 5)

    create_anki(lang=lang)

    try:
        if profile == None:
            anki.createCard(card, lang, word, meaning[rand_number])
            return
        elif card == None:
            print('Oops! You should select a card type!')
            return
        else:
            thread = threading.Thread(target=anki.changeProfile(profile))

            thread.start()
            thread.join()

            # check if this new profile have the deck and subdecks
            create_anki(lang=lang)

            anki.createCard(card, lang, word, meaning[rand_number])
            print(
                f'changing profile to "{profile}" and adding card type: "{card}".')
            return
    except (IndexError):
        print('Oops!')
        return


def create_anki(**kwargs):
    if anki.IsDeckCreated() == False:
        anki.createDeck()

    elif anki.IsSubDeckCreated(kwargs.get('lang')) == False:
        anki.createSubDeck(kwargs.get('lang'))


if __name__ == '__main__':
    parser = get_parser()
    args = vars(parser.parse_args())
    main(sys.argv[1], sys.argv[2], [args])
