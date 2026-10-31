+++
title = '[Bracket 3] The Wise Mothman'
bracket = 3
commanders = ['The Wise Mothman (PIP) 1067']
archetypes = ['Mill', 'Counters']
decklist_url = 'https://moxfield.com/decks/DoU6se0q_EW7CgF-jELNvA'
deck_authors = [{ name = 'JollyCasual', url = 'https://moxfield.com/users/JollyCasual' }]
primer_url = 'https://moxfield.com/decks/iud_U_X_gEuWC64866SeMQ/primer'
date = 2025-09-13T00:00:00-05:00
draft = false



[overview]
summary = "Sultai mill-and-counters. The Wise Mothman turns every mill into +1/+1 counters, so many small mill effects work better than one big one; it wins through combat or by milling opponents out."
strengths = [
  "Two ways to win: combat with countered-up creatures, or mill.",
  "Repeating mill effects keep Mothman's counters flowing.",
  "Plenty of Draw (15) and Counterspells (7).",
]
weaknesses = [
  "Milling everyone can hand an opposing graveyard deck the win; knock out graveyard players first.",
  "Mothman gives every player rad counters, not just opponents.",
]
gameplan = [
  "Prefer many small mill effects over a few big ones; each triggers Mothman separately.",
  "Mill only yourself until you have graveyard hate down if an opponent is a graveyard deck.",
]
mulligan = [
  "Green first, then blue and black for Mothman on turn four; 4 cheap Land Ramp spells help.",
  "A repeatable mill effect or Mothman himself, plus creatures for the counters.",
]

[[overview.combos]]
cards = ["Zellix, Sanity Flayer", "Altar of the Brood"]
result = "Opponents' milled creatures make Horror tokens, each of which mills everyone again; it's rarely truly infinite but often huge."

[[overview.combos]]
cards = ["The Wise Mothman", "Psychic Corrosion"]
result = "Every card you draw mills each opponent two, putting counters on your creatures each time."

[[overview.combos]]
cards = ["Walking Ballista", "Mindcrank", "The Wise Mothman"]
result = "Remove a Ballista counter to ping a player: Mindcrank mills them, and each nonland card milled lets Mothman put a counter back. Hardened Scales makes it net-positive."

[[overview.combos]]
cards = ["Bloodchief Ascension", "Mindcrank"]
result = "Infinite mill, near-infinite lifegain, near-infinite lifegain triggers."
kind = "infinite"
steps = [
  "Cause one or more opponents to lose life.",
  "Mindcrank triggers once for each life loss event, causing that player to mill cards equal to the amount of life lost.",
  "Bloodchief Ascension triggers once for each card milled, causing that player to lose 2 life and you to gain 2 life for each trigger.",
  "Repeat from step 2.",
]
source = "https://commanderspellbook.com/combo/936-1290/"

[[overview.combos]]
cards = ["Altar of Dementia", "The Great Henge"]
result = "Infinite self-mill, infinite creature ETB, infinite creature LTB."
kind = "infinite"
steps = [
  "Activate Altar of Dementia by sacrificing the persist creature.",
  "The sacrificed creature's persist ability triggers, returning it from your graveyard to the battlefield with a -1/-1 counter on it.",
  "The Great Henge triggers, putting a +1/+1 counter on the persist creature and causing you to draw a card.",
  "The -1/-1 and +1/+1 counters are removed as a state-based action.",
  "Resolve the ability from step 1.",
  "Repeat.",
]
source = "https://commanderspellbook.com/combo/3139-5256--5/"

[[overview.rulings]]
cards = ["The Wise Mothman"]
note = "One mill event gives each targeted creature at most one +1/+1 counter, even when it mills several players or several cards. Many small mill effects beat one big one."
+++
