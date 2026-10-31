+++
title = '[Bracket 5] Krrik, Son of Yawgmoth'
bracket = 5
commanders = ["K'rrik, Son of Yawgmoth (MH3) 274"]
archetypes = ['Combo', 'Reanimator']
decklist_url = 'https://moxfield.com/decks/FGBgV9txgEWEql9NQaOPtQ'
deck_authors = [{ name = 'KntrellCL', url = 'https://moxfield.com/users/KntrellCL' }]
primer_url = 'https://moxfield.com/decks/6NkrPdOXGkeIM0KSyNborw/primer'
date = 2025-09-13T00:00:00-05:00
draft = false



[overview]
summary = "Mono-black midrange combo. K'rrik lets you pay life for black mana, and resilient creature-based combo lines win through common counterspells and stax."
strengths = [
  "Still capable of winning on turns one to three.",
  "Creature-based lines win through stax like Rule of Law and Null Rod.",
  "Win conditions dodge most common cEDH counterspells.",
]
weaknesses = [
  "Gives up some speed compared to storm builds.",
  "Life as a resource leaves you exposed to burn and aggression.",
]
gameplan = [
  "Step 1: cast K'rrik.",
  "Step 2: keep him alive for a turn cycle (recast if he's removed).",
  "Step 3: pick the combo line that suits the board and the opponents' interaction.",
]
mulligan = [
  "1–2 lands plus 11 cheap Rocks and 3 Rituals: fast mana covers K'rrik's {4}, and his three {B/P} can be paid with life, so he can land on turn one or two.",
  "A Tutor or a combo piece; black-heavy hands are explosive because K'rrik turns life into black mana.",
]

[[overview.combos]]
cards = ["K'rrik, Son of Yawgmoth", "Razaketh, the Foulblooded", "Gray Merchant of Asphodel"]
result = "Sacrifice creatures to Razaketh to tutor, paying black with life through K'rrik, and loop Gray Merchant for lethal drains."
steps = [
  "With K'rrik, Razaketh and any creature out (at least 20 life): sacrifice a creature to tutor Blood Celebrant and cast it, then use it to make black mana.",
  "Sacrifice Blood Celebrant to tutor Gray Merchant of Asphodel and cast it: drain for your devotion.",
  "Sacrifice Merchant to tutor Reanimate and return Blood Celebrant, then tutor and cast Animate Dead to return Merchant for another drain.",
  "Keep sacrificing and tutoring recursion (Dance of the Dead, and so on) until every opponent is drained out.",
]

[[overview.combos]]
cards = ["K'rrik, Son of Yawgmoth", "Vilis, Broker of Blood", "Sheoldred, the Apocalypse", "Pestilence"]
result = "Vilis draws a card for each life lost and Sheoldred gains 2 for each draw; Pestilence turns the surplus life into a table-wide drain."
kind = "infinite"
source = "https://commanderspellbook.com/combo/2498-3260-4691/"

[[overview.combos]]
cards = ["Fleshwrither", "Necrotic Ooze"]
result = "A creature-only tutor chain (transfigure into Necrotic Ooze, then Balthor) that assembles a Razaketh or Asmodeus finish through counterspells."

[[overview.combos]]
cards = ["Sheoldred, the Apocalypse", "Peer into the Abyss"]
result = "Near-infinite card draw for target opponent, near-infinite draw triggers for target opponent, near-infinite lifeloss for target opponent."
kind = "infinite"
steps = [
  "Cast Peer into the Abyss by paying {4}{B}{B}{B}, causing an opponent to draw cards equal to half their library size and lose half their life total, rounded up.",
  "Sheoldred's second ability triggers for each card drawn this way.",
  "Resolve the first Sheoldred trigger, causing the opponent to lose 2 life.",
  "Repeat step 3 until the opponent loses the game due to having zero or less life.",
]
source = "https://commanderspellbook.com/combo/1561-2498/"

[[overview.combos]]
cards = ["Orcish Bowmasters", "Peer into the Abyss"]
result = "Infinite +1/+1 counters on a creature, near-infinite card draw for target opponent, near-infinite damage."
kind = "infinite"
steps = [
  "Cast Peer into the Abyss by paying {4}{B}{B}{B}, targeting an opponent whose library size is larger than or equal to their life total.",
  "Resolve Peer into the Abyss, causing that opponent to draw cards equal to half their library size and causing them to lose half their life total, rounded up.",
  "Orcish Bowmasters triggers for each card drawn, dealing 1 damage to the opponent for each card drawn this way and putting that many +1/+1 counters on an Army you control.",
  "The opponent loses the game due to having zero or less life.",
]
source = "https://commanderspellbook.com/combo/1561-3862/"
+++
