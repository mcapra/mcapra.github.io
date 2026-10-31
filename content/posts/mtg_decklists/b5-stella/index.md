+++
title = '[Bracket 5] Stella Lee, Wild Card'
bracket = 5
commanders = ['Stella Lee, Wild Card (OTC) 3']
archetypes = ['Combo', 'Storm']
decklist_url = 'https://moxfield.com/decks/g5kk9go2HEWXoSgLAfIU-w'
deck_authors = [{ name = 'FreedomWaffle', url = 'https://moxfield.com/users/FreedomWaffle' }]
primer_url = 'https://moxfield.com/decks/x5iDbb-n9UCrYAh5PIdtbg/primer'
date = 2025-09-13T00:00:00-05:00
draft = false



[overview]
summary = "Izzet combo with storm backup. Stella copies an instant or sorcery once you've cast three spells in a turn; redundant one-card win conditions present early, instant-speed wins."
strengths = [
  "Multiple one-card win conditions present early wins.",
  "Most combos work at instant speed, so you can wait for the right window.",
  "Very interactive: 14 Counterspells.",
]
weaknesses = [
  "Commander-centric: Stella is a removal magnet.",
  "Weak to stax and removal, and limited to two colors.",
]
gameplan = [
  "Mulligan aggressively for a turn-one or turn-two Stella or a card advantage engine.",
  "Save interaction to protect Stella, and have Spellskite or a counterspell up before casting her if needed.",
  "Wait for a window, then present an instant-speed win.",
]
mulligan = [
  "1–2 of the 24 lands plus Rocks (10 cheap ones); blue is the main color.",
  "Stella on turn one or two, or a draw engine (Rhystic Study, Mystic Remora).",
]

[[overview.combos]]
cards = ["Stella Lee, Wild Card", "Twisted Fealty"]
result = "Infinite life loss that doesn't target, so it wins even through The One Ring's protection."
kind = "infinite"
steps = [
  "With Stella untapped and two other spells cast this turn, cast Twisted Fealty.",
  "Tap Stella to copy it; each copy creates a new Wicked Role, replacing the last one and draining opponents.",
  "Keep copying until the table is dead.",
]
source = "https://commanderspellbook.com/combo/5534--28/"

[[overview.combos]]
cards = ["Stella Lee, Wild Card", "Cerulean Wisps"]
result = "Copy Wisps to untap Stella each time and draw your whole deck (Refocus or Twitch also work)."
kind = "infinite"
source = "https://commanderspellbook.com/combo/5534--28/"

[[overview.combos]]
cards = ["Underworld Breach", "Lion's Eye Diamond", "Brain Freeze"]
result = "Mill your deck, then mill opponents out or wheel into another win."
kind = "infinite"
steps = [
  "Cast Underworld Breach (6+ other cards in hand or graveyard).",
  "Cast Lion's Eye Diamond and sacrifice it for {R}{R}{R}, discarding your hand.",
  "Escape Wheel of Fortune, then escape Lion's Eye Diamond again; repeat to dig for Brain Freeze or Thassa's Oracle.",
  "Escape Brain Freeze repeatedly to mill opponents out. A silence effect first is strongly advised.",
]
source = "https://commanderspellbook.com/combo/1368-3518-4856/"

[[overview.combos]]
cards = ["Underworld Breach", "Lotus Petal", "Brain Freeze"]
result = "Infinite self-mill, near-infinite magecraft triggers, near-infinite mill."
kind = "infinite"
steps = [
  "Activate Lotus Petal by tapping and sacrificing it, adding {U}.",
  "Cast Lotus Petal from your graveyard for its escape cost by exiling three cards besides Brain Freeze from your graveyard.",
  "Repeat from step 1 one additional time.",
  "Cast Brain Freeze either from your hand by paying {1}{U}, or from your graveyard for its escape cost by paying {1}{U} and exiling three cards from your graveyard.",
  "Brain Freeze's storm ability triggers, creating at least two copies of Brain Freeze targeting yourself, and any remaining copies targeting an opponent.",
  "Resolve each Brain Freeze, causing yourself to mill nine cards and, if applicable, an opponent to mill three cards for each Brain Freeze remaining.",
  "Repeat.",
]
source = "https://commanderspellbook.com/combo/1368-1414-4856/"

[[overview.combos]]
cards = ["Underworld Breach", "Wheel of Fortune", "Jeska's Will"]
result = "Infinite draw triggers for all players, infinite looting for all players, near-infinite magecraft triggers."
kind = "infinite"
steps = [
  "Cast Jeska's Will from your graveyard for its escape cost by paying {2}{R} and exiling three other cards from your graveyard, adding at least six {R}.",
  "Cast Wheel of Fortune from your graveyard for its escape cost by paying {2}{R} and exiling three other cards from your graveyard, causing each player to discard their hand and draw seven cards.",
  "Repeat.",
]
source = "https://commanderspellbook.com/combo/1368-1878-2706/"
+++
