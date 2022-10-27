<p align="center">
  <img width="200" align="center" src="https://github.com/ropoko/dictionary-cli/blob/main/assets/logo.png">
</p>

<h1 align="center">
  Dictionary-cli
</h1>
<p align="center">
Dictionary for command line, re-written for various educational purposes.
</p>

<p align="center">
   <a style="text-decoration:none" href="https://github.com/ropoko/dictionary-cli/stargazers/">
    <img src="https://img.shields.io/github/stars/ropoko/dictionary-cli?style=flat&color=yellow" alt="stars" />
  </a>
  <a style="text-decoration:none" href="https://gitHub.com/ropoko/dictionary-cli/tags/">
    <img src="https://img.shields.io/github/tag/ropoko/dictionary-cli?style=flat" alt="tags" />
  </a>
  <a href="https://lgtm.com/projects/g/ropoko/dictionary-cli/context:python"><img alt="Language grade: Python" src="https://img.shields.io/lgtm/grade/python/g/ropoko/dictionary-cli.svg?logo=lgtm&logoWidth=18"/>
  </a>
</p>

## Languages
| Language | Abbreviation |
| -------- | ------------ |
| English | en |
| Portuguese_BR | pt |
| Hindi | hi |
| Spanish | es |
| French | fr |
| Japanese | ja |
| Russian | ru |
| German | de |
| Italian | it |
| Korean | ko |
| Chinese (simplified) | zh |
| Arabic | ar |
| Turkish | tr |

## Features
### Setting default language
`$ dictionary-cli --lang-default <lang>`

after that, you don't need to type the language to search a word, example:
`$ dictionary-cli <word>`

note: in all the examples below, the `<lang>` can be omitted.

### Synonyms
`$ dictionary-cli <word> <lang> -s` or `$ dictionary-cli <word> <lang> --synonyms`

### Examples
`$ dictionary-cli <word> <lang> -e` or `$ dictionary-cli <word> <lang> --examples`

### Anki - Flashcards
- card-types: basic, basic-reverse and cloze.
- if your profile name have spaces, like: "User name", you need to use quote marks.

note: you don't need to create the deck and subdecks, the app does it itself.

#### Creating card
`$ dictionary-cli <word> <lang> --card <type>`

#### Changing profile before creating the card
`$ dictionary-cli <word> <lang> --profile "User name" --card <type>`

## :zap: Installing
try versions in devmode from:

[![](https://snapcraft.io/static/images/badges/en/snap-store-black.svg)](https://snapcraft.io/dictionary-cli)

or simply: `$ sudo snap install dictionary-cli`

### Using Anki Features

Just follow the steps in the [documentation](https://github.com/FooSoft/anki-connect#installation) (is pretty simple ;D)

note: while you're using the dictionary to create cards, the anki app must be open, otherwise some weird errors will appear :P
## :rocket: Running

command: `$ dictionary-cli <word> <lang>`

![](https://github.com/ropoko/dictionary-cli/blob/main/assets/demo-new.gif)

## :coffee: Contributing
- [Buy me a coffee](https://picpay.me/ropoko)
- Pull Requests and issues are welcome


## Dependencies
- Snapd Package
- [Google Api Dictionary](https://github.com/meetDeveloper/googleDictionaryAPI)
- For more informations about Snap Packages  [click here](https://snapcraft.io/docs).

## Special Thanks
- Rafael Ferrari whom made the logo | [mailto](mailto:rafaelferrari.job@gmail.com), number: +55 14 988045194

