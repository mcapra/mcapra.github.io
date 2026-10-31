+++
title = '[Bracket 2] Auntie Ool, Cursewretch'
bracket = 2
commanders = ['Auntie Ool, Cursewretch (ECC) 2']
archetypes = ['Counters', 'Control']
decklist_url = 'https://moxfield.com/decks/5KKSY_eOiEqzitTX_CXU4g'
precon = 'Blight Curse'
date = 2025-09-13T00:00:00-05:00
draft = false




[overview]
summary = "Jund -1/-1 counters precon. Auntie Ool draws a card whenever your creatures get -1/-1 counters and drains 1 life whenever an opponent's creature does."
strengths = [
  "Ool turns every -1/-1 counter into a card or a point of drain: incremental, but left unchecked she's often the only engine the deck needs.",
  "Lots of interaction: 19 Removal and 7 Board Wipes.",
  "Ward—Blight 2 makes Ool costly to target.",
]
weaknesses = [
  "Slow and grindy. Light on ramp (2 Land Ramp, 4 Rocks).",
  "Few fast finishers; games are won by attrition and big threats like Grave Titan.",
  "Reviewers flag Ferrafor, Young Yew and Aberrant Return as underperformers worth swapping.",
]
gameplan = [
  "Land Ool early and put -1/-1 counters everywhere: your creatures draw cards, opponents' creatures cost them life.",
  "Grind with removal and wipes, then close with big threats like Grave Titan.",
]
mulligan = [
  "Black-heavy lands: black is about two-thirds of the deck's colored symbols, and Ool needs a red and a green source too.",
  "Something that puts -1/-1 counters on creatures (yours or theirs) early, so Ool draws or drains from the turn she lands.",
]

[[overview.combos]]
cards = ["Auntie Ool, Cursewretch", "Midnight Banshee"]
result = "Every upkeep, each nonblack creature gets a -1/-1 counter: opponents lose 1 life per creature they control, and you draw for each of yours."

[[overview.combos]]
cards = ["Auntie Ool, Cursewretch", "Carnifex Demon"]
result = "Each activation puts a counter on every other creature: a card for each of yours, a life point for each of theirs."

[[overview.combos]]
cards = ["Blowfly Infestation", "Flourishing Defenses"]
result = "Infinite creature ETB, infinite creature LTB, infinite death triggers."
kind = "infinite"
steps = [
  "Put a -1/-1 counter on any creature you control with toughness equal to one.",
  "The creatue dies as a state-based action due to having zero toughness.",
  "Flourishing Defenses and Blowfly Infestation trigger.",
  "Resolve the Flourishing Defenses trigger, creating a creature token.",
  "Resolve the Blowfly Infestation trigger, putting a -1/-1 counter on any creature you control with toughness equal to 1.",
  "Repeat from step 2.",
]
source = "https://commanderspellbook.com/combo/1084-4994/"

[[overview.combos]]
cards = ["Blowfly Infestation", "Hapatra, Vizier of Poisons"]
result = "Infinite death triggers, infinite creature ETB, infinite creature LTB."
kind = "infinite"
steps = [
  "Put a -1/-1 counter on any creature you control with toughness equal to one.",
  "The creatue dies as a state-based action due to having zero toughness.",
  "Hapatra and Blowfly Infestation trigger.",
  "Resolve the Hapatra trigger, creating a 1/1 Snake creature token.",
  "Resolve the Blowfly Infestation trigger, putting a -1/-1 counter on any creature you control with toughness equal to one.",
  "Repeat from step 2.",
]
source = "https://commanderspellbook.com/combo/2228-4994/"
+++
