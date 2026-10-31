+++
title = '[Bracket 2] Shiko and Narset, Unified'
bracket = 2
commanders = ['Shiko and Narset, Unified (TDC) 7']
archetypes = ['Spellslinger']
decklist_url = 'https://moxfield.com/decks/YtK35kRVFkiRPWm30rv8yw'
precon = 'Jeskai Striker'
date = 2025-09-13T00:00:00-05:00
draft = false




[overview]
summary = "Jeskai spellslinger precon. Shiko and Narset copy your second spell each turn if it targets, and draw you a card if it doesn't."
strengths = [
  "Every turn's second spell is either doubled or replaced.",
  "Plenty of Draw (17) and Removal (12).",
  "Strong top end in Velomachus Lorehold and Magma Opus.",
]
weaknesses = [
  "Needs two spells every turn to get value.",
  "Creature-light, so it relies on a few big threats to close.",
]
gameplan = [
  "Cast two spells every turn; target permanents or players with the second to copy it.",
  "Close with big spells and the deck's few large threats.",
]
mulligan = [
  "Blue-heavy lands with red; white is the lightest color. One of the 7 cheap Rocks helps cast two spells a turn.",
  "Two or more cheap spells per turn, ideally targeted ones, since only the second spell each turn gets copied.",
]

[[overview.combos]]
cards = ["Narset's Reversal", "Expansion // Explosion"]
result = "Infinite magecraft triggers."
kind = "infinite"
steps = [
  "Setup: You have an additional instant or sorcery card in hand with mana value 4 or less and valid targets as applicable.",
  "Cast any instant or sorcery by paying its mana cost.",
  "Holding priority, cast Expansion by paying its mana cost, targeting the instant or sorcery cast in step 1.",
  "Cast Narset's Reversal by paying {U}{U}, copying Expansion targeting the spell cast in step 1 and returning the original Expansion to your hand.",
  "Cast Expansion by paying its mana cost, copying the copy of Expansion, targeting the copy of Expansion.",
  "Resolve the copy of Expansion, creating a copy of Expansion targeting the copy of Expansion.",
  "Repeat step 5.",
]
source = "https://commanderspellbook.com/combo/11-60/"

[[overview.combos]]
cards = ["Adaptive Training Post", "Expansion // Explosion"]
result = "Infinite magecraft triggers."
kind = "infinite"
steps = [
  "Cast the additional instant or sorcery by paying its mana cost.",
  "If Adaptive Training Post had two charge counters on it, it triggers, putting a charge counter on it.",
  "Holding priority, activate Adaptive Training Post by removing three charge counters from it, copying the next instant or sorcery spell you cast this turn.",
  "Cast Expansion by paying its mana cost, targeting the spell cast in step 1.",
  "Adaptive Training Post triggers, copying Expansion, with the copy targeting the original Expansion.",
  "Resolve the copy of Expansion, copying the original Expansion, with the copy targeting the original Expansion.",
  "Repeat step 5.",
]
source = "https://commanderspellbook.com/combo/60-6452/"
+++
