+++
title = '[Bracket 5] Yuriko, the Tigers Shadow'
bracket = 5
commanders = ["Yuriko, the Tiger's Shadow (CMM) 364"]
archetypes = ['Combo', 'Aggro']
decklist_url = 'https://moxfield.com/decks/OtUIXzPys02sA7YCD680sg'
deck_authors = [{ name = 'R0bot0', url = 'https://moxfield.com/users/R0bot0' }]
primer_url = 'https://moxfield.com/decks/8CkGkfcOfkGNkYf0WnwzVg/primer'
date = 2025-09-13T00:00:00-05:00
draft = false



[overview]
summary = "Dimir ninja combo. Evasive creatures connect so Yuriko ninjutsus in and drains for revealed cards; the main win is Thassa's Oracle with Demonic Consultation, backed by Ad Nauseam."
strengths = [
  "Adaptive: as explosive as top combo decks, but can grind long games.",
  "Hard to shut down with stax: card advantage is creature-based and ninjutsu ignores Cursed Totem and Null Rod.",
  "Commander tax is irrelevant thanks to ninjutsu.",
]
weaknesses = [
  "Slower than the fastest cEDH commanders.",
  "Tax effects like Trinisphere, Rule of Law and Deafening Silence hit hard.",
]
mulligan = [
  "1–2 of the 29 lands plus fast mana (10 cheap Rocks, 5 Rituals).",
  "A cheap evasive creature to ninjutsu Yuriko in on turn two, plus a combo piece or Tutor; keep faster hands against faster tables.",
]

[[overview.combos]]
cards = ["Thassa's Oracle", "Demonic Consultation"]
result = "Exile your library, then win with Oracle's trigger."
kind = "win"
steps = [
  "Cast Thassa's Oracle.",
  "With its enter trigger on the stack, cast Demonic Consultation naming a card not in your library.",
  "The Oracle trigger resolves with an empty library, and you win.",
]
source = "https://commanderspellbook.com/combo/742-1295/"

[[overview.combos]]
cards = ["Thassa's Oracle", "Tainted Pact"]
result = "The same line with Tainted Pact."
kind = "win"
source = "https://commanderspellbook.com/combo/1295-3093/"

[[overview.combos]]
cards = ["Ad Nauseam", "Aetherflux Reservoir"]
result = "Ad Nauseam draws a huge hand; chain the cheap spells and let Aetherflux finish a player."

[[overview.combos]]
cards = ["Sensei's Divining Top", "Aetherflux Reservoir", "Bolas's Citadel"]
result = "Infinite card draw, infinite draw triggers, near-infinite damage."
kind = "infinite"
steps = [
  "Setup: Your life total is at least 2.",
  "Activate Sensei's Divining Top by tapping it, drawing a card and then putting Sensei's Divining Top on top of your library.",
  "Cast Sensei's Divining Top from the top of your library by paying 1 life.",
  "Aetherflux Reservoir triggers, gaining you 1 life for each spell you have cast this turn.",
  "Repeat until your life total is 52 or greater.",
  "Activate Aetherflux Reservoir by paying 50 life, dealing 50 damage to any target.",
  "Repeat.",
]
source = "https://commanderspellbook.com/combo/2173-4740-5078/"
+++
