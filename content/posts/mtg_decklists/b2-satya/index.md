+++
title = '[Bracket 2] Satya, Aetherflux Genius'
bracket = 2
commanders = ['Satya, Aetherflux Genius (M3C) 3']
archetypes = ['Blink', 'Artifacts']
decklist_url = 'https://moxfield.com/decks/zebdKhU2ZUyteK2RujSmrA'
precon = 'Creative Energy'
date = 2025-09-13T00:00:00-05:00
draft = false




[overview]
summary = "Jeskai energy precon. Satya makes an attacking token copy of another creature whenever she attacks, keeping it if you pay energy equal to its mana value."
strengths = [
  "Copies of creatures with enter triggers give repeated value every attack.",
  "Lots of artifact ramp (11 Rocks).",
  "Big artifact creatures make powerful copies.",
]
weaknesses = [
  "Needs good creatures on the battlefield to copy.",
  "Keeping expensive copies drains energy fast.",
]
gameplan = [
  "Build a board of creatures with enter triggers, then attack with Satya to copy the best one.",
  "Bank energy to keep the most valuable copies.",
]
mulligan = [
  "All three colors by turn four, plus one of the 6 cheap Rocks; the top end is heavy (13 cards at 6+ mana value).",
  "A creature with a strong enter trigger for Satya to copy on her first attack.",
]

[[overview.combos]]
cards = ["Satya, Aetherflux Genius", "Myr Battlesphere"]
result = "Satya's attacking copy of Battlesphere makes four more Myr as it enters."

[[overview.combos]]
cards = ["Satya, Aetherflux Genius", "Lightning Runner"]
result = "Infinite creature LTB, infinite creature ETB, infinite creature sacrifice triggers."
kind = "infinite"
steps = [
  "Declare Lightning Runner and Satya as attackers, triggering their abilities.",
  "Resolve the Satya trigger, causing you to get {E}{E} and create a token copy of Lighting Runner that's tapped and attacking.",
  "Resolve the Lightning Runner trigger, causing you to get {E}{E} and then pay eight {E} to untap all creatures you control and to get an additional combat phase after this one.",
  "Move to your next combat phase, and declare Satya and each Lightning Runner you control as attackers.",
  "Resolve the Satya trigger, causing you to get {E}{E} and create a token copy of Lighting Runner that's tapped and attacking.",
  "Resolve the first Lightning Runner trigger, causing you to get {E}{E} and choosing not to pay.",
  "Repeat step 6 until there is only one Lightning Runner trigger remaining.",
  "Resolve the final Lightning Runner trigger, causing you to get {E}{E} and then pay eight {E} to untap all creatures you control and to get an additional combat phase after this one.",
  "Repeat from step 4.",
]
source = "https://commanderspellbook.com/combo/4918-5658/"

[[overview.combos]]
cards = ["Lightning Runner", "Stone Idol Generator"]
result = "Infinite combat phases, infinite energy counters, infinite mana creatures you control can produce."
kind = "infinite"
steps = [
  "Declare Lightning Runner and at least five other creatures as attackers.",
  "Lightning Runner triggers once, and Stone Idol Generator triggers for each attacking creature.",
  "Resolve all Stone Idol Generator triggers, causing you to get that much {E}.",
  "Resolve the Lightning Runner trigger, causing you to get {E}{E}, and then pay eight {E} to untap all creatures you control and to get an additional combat phase after this one.",
  "Repeat.",
  "You may attack with additional creatures to net additional {E} each loop.",
]
source = "https://commanderspellbook.com/combo/4918-5723/"

[[overview.combos]]
cards = ["Gonti's Aether Heart", "Decoction Module", "Whirler Virtuoso"]
result = "Infinite creature tokens, infinite creature ETB."
kind = "infinite"
steps = [
  "Activate Whirler Virtuoso by paying {E}{E}{E}, creating a 1/1 Thopter artifact creature token.",
  "Thopter token enters the battlefield, triggering Gonti's Aether Heart and Decoction Module trigger.",
  "Resolve the Gonti's Aether Heart's trigger, adding {E}{E}.",
  "Resolve the Decoction Module trigger, adding {E}.",
  "Repeat.",
]
source = "https://commanderspellbook.com/combo/2583-3484-4636/"
+++
