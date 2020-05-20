# Civilization VI Drafter

This is my take on a quick-and-dirty Civ VI drafter in Python

(an updated version of https://github.com/wggodfrey/civ6-drafter)

## How to Use

### Setup

Make sure you install [pandas](https://github.com/pandas-dev/pandas), on which this package depends.

Install using:
`pip3 install pandas`

### Configuration (editing `draft_civs.py`)

1) Enter the names of the players you want to draft into the `PLAYERS` list (on line 4)

2) Edit `NUMBER_OF_DRAFT_OPTIONS_PER_PLAYER` if desired from the default of 4 (on line 16)

## Running

Run `python3 draft_civs.py` after configuring and you're good :).

## About the Data
The data used to draft (in `data/leaders.csv`) should be accurate as of the 19th of May, 2020.

Make sure to validate this data for accuracy in the Civilization Wiki ([Leaders](https://civilization.fandom.com/wiki/Leaders_(Civ6)), [Civilizations](https://civilization.fandom.com/wiki/Civilizations_(Civ6))) if too much time has passed past this point.
