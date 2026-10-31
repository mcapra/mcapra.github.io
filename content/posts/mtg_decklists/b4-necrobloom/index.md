+++
title = '[Bracket 4] The Necrobloom'
bracket = 4
commanders = ['The Necrobloom (MH3) 378']
archetypes = ['Lands Matter', 'Combo']
decklist_url = 'https://moxfield.com/decks/jCCfATMlUnGMrWfaHJAVMA'
deck_authors = [{ name = 'mcapra', url = 'https://moxfield.com/users/mcapra' }]
date = 2026-03-27T16:44:02+00:00
draft = false



[overview]
summary = "Abzan layered lands combo. Rather than A+B combos, many interchangeable pieces return, sacrifice and replay lands for infinite mana, mill and land triggers, aiming to win on turns three to five."
strengths = [
  "Redundant pieces make it easy to route around removal.",
  "Several deterministic infinite loops.",
  "The Necrobloom itself turns land drops into an army.",
]
weaknesses = [
  "Graveyard hate shuts down the loops.",
  "Complex lines with lots of sequencing.",
]
mulligan = [
  "Green first (57 green mana symbols), with 3–4 lands plus Land Ramp (8 cheap pieces).",
  "An engine piece or two and a reasonable curve; per the primer, don't look for a full combo in hand.",
]

[[overview.combos]]
cards = ["Aftermath Analyst", "Shifting Woodland", "Squandered Resources"]
result = "Infinite mana and infinite land enter and leave triggers."
kind = "infinite"
steps = [
  "Have Aftermath Analyst in your graveyard, at least four card types there, and eight other mana-producing lands (three that make {G}).",
  "Sacrifice every land except Shifting Woodland to Squandered Resources for mana.",
  "Pay {2}{G}{G}: Shifting Woodland becomes a copy of Aftermath Analyst.",
  "Pay {3}{G} and sacrifice it: return it and every land from your graveyard. Repeat.",
]
source = "https://commanderspellbook.com/combo/2167-5720-5721/"

[[overview.combos]]
cards = ["Shigeki, Jukai Visionary", "Tyvar, Jubilant Brawler", "Eerie Ultimatum"]
result = "A second deterministic land loop: Tyvar lets Shigeki keep returning Eerie Ultimatum, which returns everything."

[[overview.combos]]
cards = ["Sunscorched Desert"]
result = "The finisher: with an infinite land loop, replay Sunscorched Desert to ping each opponent to death."

[[overview.rulings]]
cards = ["Cultivator Colossus"]
note = "Lands it puts onto the battlefield enter tapped, and their landfall triggers wait until Colossus finishes resolving. It keeps drawing as it goes, so if you can't win, stop with cards left in your library rather than decking yourself."

[[overview.rulings]]
cards = ["Lumra, Bellow of the Woods"]
note = "Copies of Lumra die to the legend rule (CR 704.5j) as a state-based action, but the copy's enter trigger has already triggered and still resolves."
+++
