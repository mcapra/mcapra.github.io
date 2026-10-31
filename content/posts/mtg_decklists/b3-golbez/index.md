+++
title = '[Bracket 3] Golbez, Crystal Collector'
bracket = 3
commanders = ['Golbez, Crystal Collector (FIN) 540']
archetypes = ['Artifacts', 'Control']
decklist_url = 'https://moxfield.com/decks/ylbbVf2_rUWIt4clcbvqfA'
deck_authors = [{ name = 'birkoss', url = 'https://moxfield.com/users/birkoss' }]
primer_url = 'https://moxfield.com/decks/96NfxqKiG0ypzWusGhWwzQ/primer'
date = 2025-09-13T00:00:00-05:00
draft = false



[overview]
summary = "Esper artifact value. Golbez surveils as artifacts enter, returns a creature from your graveyard each end step once you control four artifacts, and drains each opponent for its power at eight."
strengths = [
  "A strong, steady value engine with lots of Draw (25).",
  "Counterspells (6) protect the artifact board from hate.",
  "Damage arrives without attacking, through Golbez's end-step drain.",
]
weaknesses = [
  "Artifact hate hits the whole deck at once.",
  "A midrange deck rather than a combo deck; wins can take a while.",
]
gameplan = [
  "Early: always cast Golbez on turn two, then ramp and start filling the graveyard. Hold a 0-mana artifact or artifact land to surveil the turn he lands.",
  "Mid: build card advantage and control the board, and save Counterspells for artifact or graveyard hate rather than policing the table.",
  "Late: grow to eight artifacts and drain the table each end step.",
]
mulligan = [
  "A blue source and a black source on turn two for Golbez; blue is the main color. Artifact lands count toward his artifact thresholds.",
  "A 0-mana artifact or artifact land held back to surveil the turn Golbez lands, and a 3-mana artifact engine for turn three.",
]

[[overview.combos]]
cards = ["Golbez, Crystal Collector", "Troll of Khazad-dûm"]
result = "With eight or more artifacts, Golbez returns the Troll every end step and each opponent loses 6 life."

[[overview.combos]]
cards = ["Aetherflux Reservoir", "Cyberdrive Awakener"]
result = "Infinite damage, infinite lifegain triggers."
kind = "infinite"
steps = [
  "Cast Cyberdrive Awakener by paying {5}{U}.",
  "Aetherflux Reservoir triggers, causing you to gain 1 life for each spell you've cast this turn.",
  "When Cyberdrive Awakener enters the battlefield, it triggers, causing Aetherflux Reservoir to become a 4/4 artifact creature until end of turn.",
  "Give Aetherflux Reservoir lifelink.",
  "Activate Aetherflux Reservoir by paying 50 life, dealing 50 damage to any target and causing you to gain 50 life.",
  "Repeat step 5.",
]
source = "https://commanderspellbook.com/combo/2734-4740/"

[[overview.combos]]
cards = ["Sensei's Divining Top", "Foundry Inspector", "Mystic Forge"]
result = "Infinite card draw, near-infinite storm count, infinite draw triggers."
kind = "infinite"
steps = [
  "Activate Sensei's Divining Top by tapping it, causing you to draw a card and put Sensei's Divining Top on top of your library.",
  "Cast Sensei's Divining Top from the top of your library by paying {0}.",
  "Repeat",
]
source = "https://commanderspellbook.com/combo/777-985-5078/"

[[overview.combos]]
cards = ["Sensei's Divining Top", "Mystic Forge", "Etherium Sculptor"]
result = "Infinite card draw, near-infinite storm count, infinite draw triggers."
kind = "infinite"
steps = [
  "Activate Sensei's Divining Top by tapping it, causing you to draw a card and put Sensei's Divining Top on top of your library.",
  "Cast Sensei's Divining Top from the top of your library by paying {0}.",
  "Repeat",
]
source = "https://commanderspellbook.com/combo/985-1976-5078/"
+++
