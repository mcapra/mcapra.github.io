+++
title = '[Bracket 5] Kenrith, the Returned King'
bracket = 5
commanders = ['Kenrith, the Returned King (PLST) ELD-303']
archetypes = ['Combo', 'Storm']
decklist_url = 'https://moxfield.com/decks/JqHn8EOJT0yNOXMojpIeBg'
deck_authors = [{ name = 'DrGiovanni', url = 'https://moxfield.com/users/DrGiovanni' }, { name = 'InSertS', url = 'https://moxfield.com/users/InSertS' }, { name = 'pradasfdez', url = 'https://moxfield.com/users/pradasfdez' }]
primer_url = 'https://moxfield.com/decks/mkIhm5thEUGpwANTr1-GJQ/primer'
date = 2025-09-13T00:00:00-05:00
draft = false



[overview]
summary = "Five-color turbo combo. Fast mana, rituals and tutors aim to win on turns one to three with compact one-card win conditions, falling back to a midrange plan built around draw engines."
strengths = [
  "Five colors give access to the best cards in the format.",
  "Many compact win lines make it easy to pivot and hard to predict.",
  "Several one-card win conditions: Ad Nauseam, Necropotence, Intuition.",
]
weaknesses = [
  "Kenrith doesn't draw cards, so mulligans decide whether you have an engine.",
  "Five-color mana: a bad fetch decision can cost the game.",
  "You will always be seen as the threat.",
]
gameplan = [
  "Main plan (turbo): with a hand that can win on turns one to three, go for it.",
  "Backup (midrange): land a draw engine like Mystic Remora or Rhystic Study, then high-impact cards like Smothering Tithe, Ad Nauseam, Necropotence or The One Ring.",
]
mulligan = [
  "1–2 lands plus fast mana (6 cheap Rocks, 3 Dorks, 4 Rituals): the deck runs only 28 lands. Blue and black are the main colors.",
  "A draw engine (Mystic Remora, Rhystic Study) or a Tutor into a win line; per the primer, mulligans make or break this deck.",
]

[[overview.combos]]
cards = ["Thassa's Oracle", "Demonic Consultation"]
result = "Exile your library, then win with Oracle's trigger."
kind = "win"
steps = [
  "Cast Thassa's Oracle.",
  "With its enter trigger on the stack, cast Demonic Consultation naming a card that isn't in your library: your whole library is exiled.",
  "The Oracle trigger resolves with no cards in your library, and you win.",
]
source = "https://commanderspellbook.com/combo/742-1295/"

[[overview.combos]]
cards = ["Thassa's Oracle", "Tainted Pact"]
result = "Same line with Tainted Pact: keep exiling until your library is empty (works in a singleton deck)."
kind = "win"
source = "https://commanderspellbook.com/combo/1295-3093/"

[[overview.combos]]
cards = ["Underworld Breach", "Lion's Eye Diamond", "Brain Freeze"]
result = "Loop Lion's Eye Diamond for mana and Brain Freeze for storm to mill every opponent."
kind = "infinite"
steps = [
  "Cast Underworld Breach.",
  "Cast Lion's Eye Diamond, then sacrifice it for three mana, discarding your hand.",
  "Escape Lion's Eye Diamond from your graveyard (exiling three other cards) and sacrifice it again: each loop nets three mana.",
  "Use the mana to escape Brain Freeze repeatedly; the storm count climbs each time, milling opponents (and you, to fuel more escapes).",
  "Mill them out, or switch to a Thassa's Oracle line.",
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

[[overview.rulings]]
cards = ["Necropotence"]
note = "Discarding to hand size with Necropotence creates an exile trigger for each card, so players get priority during the cleanup step (CR 514.3a). \"Until end of turn\" effects such as Silence have already ended by then, which opens an instant-speed win window."

[[overview.rulings]]
cards = ["Brain Freeze", "An Offer You Can't Refuse"]
note = "Let some Brain Freeze copies resolve, then counter the original with An Offer You Can't Refuse: you get two Treasures and the original goes back to your graveyard to escape again with Underworld Breach."
+++
