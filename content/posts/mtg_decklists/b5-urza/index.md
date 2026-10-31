+++
title = '[Bracket 5] Urza, Lord High Artificer'
bracket = 5
commanders = ['Urza, Lord High Artificer (H1R) 11']
archetypes = ['Stax', 'Combo']
decklist_url = 'https://moxfield.com/decks/yaOqN-AwS0avOa6QMyMcLA'
deck_authors = [{ name = 'Hauntz', url = 'https://moxfield.com/users/Hauntz' }]
primer_url = 'https://moxfield.com/decks/mNapLrgSiUaA17cl9XNCpw/primer'
date = 2025-09-13T00:00:00-05:00
draft = false



[overview]
summary = "Mono-blue artifact midrange with stax. Urza turns artifacts into blue mana and casts free cards from your library; fast mana and stax buy a window to assemble infinite mana and loop the deck."
strengths = [
  "Fast artifact mana and stax give a strong early window.",
  "Several infinite-mana lines, and wins without dedicated \"I win\" cards.",
  "Heavy interaction: 16 Counterspells.",
]
weaknesses = [
  "Usually not the grindiest deck late in the game.",
  "Turbo Ad Nauseam decks can be faster, often using your own artifacts against you.",
]
gameplan = [
  "Early: the best window to win; others are slowed by stax and you're ahead on mana. Tutor for Proteus Staff or another combo.",
  "Late: focus on card advantage and stax pieces, and let others absorb interaction with failed win attempts.",
]
mulligan = [
  "1–2 lands plus fast artifact mana (9 cheap Rocks) so Urza lands on turn two or earlier.",
  "Mulligan harder the later you are in turn order; slow hands get punished.",
]

[[overview.combos]]
cards = ["Tidespout Tyrant", "Urza, Lord High Artificer"]
result = "With two cheap artifacts, alternate tapping and recasting them while Tyrant bounces the tapped one: infinite mana."
steps = [
  "Have Tidespout Tyrant and Urza out, plus two cheap artifacts (with Urza, 0-cost artifacts are mana-positive).",
  "Tap one artifact for mana and cast the other artifact; Tyrant's trigger returns the tapped artifact to your hand.",
  "Tap the newly cast artifact and recast the first, returning the other. Repeat for infinite mana and casts.",
]

[[overview.combos]]
cards = ["Isochron Scepter", "Dramatic Reversal"]
result = "With rocks producing 3+ mana, imprint Dramatic Reversal on Scepter for infinite mana; then use Urza's ability to cast the whole deck."
kind = "infinite"
source = "https://commanderspellbook.com/combo/4821-5261/"

[[overview.combos]]
cards = ["Proteus Staff", "Tidespout Tyrant"]
result = "Staff Urza's Construct token: with only two other creatures in the deck, you hit Tidespout Tyrant or Hullbreaker Horror."

[[overview.combos]]
cards = ["Windfall", "Tormod's Crypt", "Timetwister"]
result = "With infinite mana, loop Timetwister and repeatedly Windfall opponents out, exiling their graveyards with Tormod's Crypt each time."

[[overview.combos]]
cards = ["Hullbreaker Horror"]
result = "Infinite creature LTB, infinite creature ETB, infinite storm count."
kind = "infinite"
steps = [
  "Cast one of the permanents from your hand by paying {0}.",
  "Hullbreaker Horror triggers; choose to return nothing.",
  "That permanent enters the battlefield.",
  "Cast one of the permanents from your hand by paying {0}.",
  "Hullbreaker Horror triggers, returning the other permanent from the battlefield to your hand.",
  "The permanent you cast enters the battlefield.",
  "Repeat from step 4.",
]
source = "https://commanderspellbook.com/combo/513--62/"

[[overview.combos]]
cards = ["Rings of Brighthearth", "Basalt Monolith"]
result = "Infinite colorless mana."
kind = "infinite"
steps = [
  "Activate Basalt Monolith's first ability by tapping it, adding {C}{C}{C}.",
  "Activate Basalt Monolith's last ability by paying {3}.",
  "Rings of Brighthearth triggers, causing you to pay {2} to copy Basalt Monolith's last ability.",
  "Resolve the copy of Basalt Monolith's last ability, untapping it.",
  "Activate Basalt Monolith's first ability by tapping it, adding {C}{C}{C}.",
  "Resolve the Basalt Monolith ability from step 2, untapping it.",
  "Repeat.",
]
source = "https://commanderspellbook.com/combo/4131-4235/"
+++
