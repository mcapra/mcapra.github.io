+++
title = '[Bracket 2] {{ replace (replaceRE `^b\d-` "" .File.ContentBaseName) "-" " " | title }}'
bracket = 2
# Commander(s) with their printing, e.g. "Hashaton, Scarab's Fist (DRC) 1"; import_decks.py fills these in
commanders = ['Commander Name']
# Primary archetype first; names must exist in data/archetypes.yaml
archetypes = ['Combo']
# Where import_decks.py fetches the list from (Moxfield or Archidekt); not shown on the page
decklist_url = 'https://moxfield.com/decks/XXXXXXXX'
# Original list author(s), linked to their profile
deck_authors = [{ name = 'mcapra', url = 'https://moxfield.com/users/mcapra' }]
# For a preconstructed deck, name the product instead of deck_authors
# precon = 'Animated Army'
date = {{ .Date }}
draft = true

# The Overview tab. See "Writing an overview" in README.md.
[overview]
summary = "Colors, engine and win route in one or two sentences."
strengths = [
  "Something specific to this list.",
]
weaknesses = [
  "Something specific to this list.",
]
gameplan = [
  "Early: ...",
]
mulligan = [
  "Lands: how many, and which colors carry the deck.",
  "Pieces: what the first turns need for this strategy.",
]

# One block per combo; every card must be in the deck.
# kind = "infinite" or "win" adds a badge; source links to Commander Spellbook.
# [[overview.combos]]
# cards = ["Card A", "Card B"]
# result = "What it does."
# kind = "infinite"
# steps = ["Step one.", "Step two."]
# source = "https://commanderspellbook.com/combo/0000-0000/"

# [[overview.rulings]]
# cards = ["Card A"]
# note = "A non-obvious rules interaction (cite a CR number only if certain)."
+++
