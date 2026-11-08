+++
title = "[Bracket 3] Teval, the Balanced Scale"
bracket = 3
commanders = ['Teval, the Balanced Scale (TDC) 8']
archetypes = ["Lands Matter", "Graveyard", "Reanimator"]
decklist_url = "https://moxfield.com/decks/PCJ2fiiIE0WpLJ6zJ8_Alg"
deck_authors = [{ name = "monarchtempest", url = "https://moxfield.com/users/monarchtempest" }]
date = 2026-10-28T18:32:17+00:00
draft = false

[overview]
summary = "Sultai self-mill. Teval mills three each attack and returns a land from the graveyard, and every time cards leave your graveyard it makes a 2/2 Zombie. monarchtempest calls it a \"turbo battlecruiser\": it takes some hits early, then snowballs lands, mana and reanimated threats into a win around turn 7."
strengths = [
  "Hard to put down: removal and graveyard play only feed the engine, and the deck rebuilds from its graveyard after wipes.",
  "Lands do the heavy lifting. Field of the Dead, Gaea's Cradle and Lotus Field turn recursion into Zombies and huge mana, and Teval brings a land back on every attack.",
  "Several ways to win: Laboratory Maniac, drain from Polluted Cistern, Syr Konrad and The Scarab God, mill with Hedron Crab, or plain combat with an evasive commander and a Zombie army.",
  "Real interaction, with 11 Removal cards, 5 counterspells and sweepers for every permanent type, plus Glacial Chasm to stop all damage to you.",
]
weaknesses = [
  "Graveyard hate is the main threat. Endurance can save your graveyard from a Bojuka Bog in response, but Rest in Peace needs enchantment removal like Tear Asunder or Season of Gathering.",
  "It shows its plan openly. monarchtempest notes that tables tend to team up on Teval, with several removal spells a turn cycle.",
  "Farewell and other mass exile effects are a setback, even though the deck can recover.",
  "The mana is pip-heavy for three colors, and several utility lands only make colorless, so a hand short on colors stalls before Teval.",
]
gameplan = [
  "Early: turn 1, play a support or ramp piece like Hedron Crab, Birds of Paradise or Ripples of Undeath. Turn 2, ramp. Turn 3, cast Teval if you've ramped, or set up otherwise.",
  "Mid: attack with Teval every turn to mill three and return a land, and keep milling yourself for options. Build toward a big recursion turn while staying alive.",
  "Late: by turn 7, win with a mass recursion turn like Lumra or Living Death, a Laboratory Maniac finish or the drain cards. If you've been stopped, defend with Glacial Chasm, and Marwyn or Icetill Explorer to keep it.",
]
mulligan = [
  "At least 3 of the 35 lands, as few tapped as possible, with green first (47 colored mana symbols to black's 30 and blue's 22). Teval needs all three, and several utility lands only make colorless.",
  "A ramp piece to put Teval out on turn 3, like Birds of Paradise, Great Divide Guide or Nature's Lore. monarchtempest compares the keep to any four-mana commander you want out fast.",
  "Ideally an early mill engine such as Ripples of Undeath or Hedron Crab. Protection for Teval helps but isn't required, because the deck recovers from removal.",
]

[[overview.combos]]
cards = ["Shifting Woodland", "Aftermath Analyst", "Zuran Orb", "Amulet of Vigor"]
result = "Infinite landfall and lifegain. With delirium and enough mana, Hedron Crab mills the table and Field of the Dead makes endless Zombies."
kind = "infinite"
steps = [
  "With Aftermath Analyst in your graveyard, pay {2}{G}{G} to make Shifting Woodland a copy of it.",
  "Tap your other lands for mana, then sacrifice them to Zuran Orb for life.",
  "Pay {3}{G} and sacrifice the Woodland-Analyst to return every land, Woodland included.",
  "Amulet of Vigor untaps them all. Repeat.",
]
source = "https://commanderspellbook.com/combo/654-1315-5720-5721/"

[[overview.combos]]
cards = ["Shifting Woodland", "Aftermath Analyst", "Amulet of Vigor", "Sylvan Safekeeper"]
result = "The same loop, using Sylvan Safekeeper to sacrifice the lands instead of Zuran Orb."
kind = "infinite"
source = "https://commanderspellbook.com/combo/654-5720-5721-6620/"

[[overview.combos]]
cards = ["Shifting Woodland", "Laboratory Maniac"]
result = "With your library empty and Laboratory Maniac in the graveyard, make Woodland a copy of it at instant speed, then draw a card to win."
kind = "win"

[[overview.combos]]
cards = ["Lotuslight Dancers", "Dread Return", "Colossal Grave-Reaver"]
result = "Dancers puts Dread Return, Colossal Grave-Reaver and a blue card like Malevolent Hermit into your graveyard. Flash back Dread Return by sacrificing three creatures to reanimate the dragon, often by turn 5."

[[overview.combos]]
cards = ["Colossal Grave-Reaver", "Altar of Dementia", "Teval, the Balanced Scale"]
result = "Sacrifice Zombies to the Altar to mill yourself. Each creature card milled comes back through the Grave-Reaver, and Teval makes more Zombies to feed it. Liliana the Repentant does the same job."

[[overview.combos]]
cards = ["Glacial Chasm", "Icetill Explorer"]
result = "Let the Chasm go each upkeep instead of paying more life, then replay it from your graveyard. You never take damage outside your own choices."

[[overview.combos]]
cards = ["Lumra, Bellow of the Woods", "Amulet of Vigor"]
result = "Lumra returns every land from your graveyard, and the Amulet untaps them all for one huge turn. Aftermath Analyst does the same at instant speed."

[[overview.combos]]
cards = ["Irma, Part-Time Mutant", "Teval, the Balanced Scale"]
result = "Irma becomes a copy of Teval each combat but keeps her own name, so the legend rule doesn't apply and you get two attack triggers."

[[overview.rulings]]
cards = ["Teval, the Balanced Scale"]
note = "The Zombie trigger fires once per event, so returning several cards at once makes one token. Separate events, such as two different spells, each make one."

[[overview.rulings]]
cards = ["Glacial Chasm"]
note = "Your own creatures can't attack while it's out, so attack with Teval first and return the Chasm with the trigger. If you control no other land when it enters, you must sacrifice the Chasm itself."

[[overview.rulings]]
cards = ["Shifting Woodland"]
note = "It copies only the printed card and gets no enter abilities, but static abilities like Laboratory Maniac's work. You need four card types in your graveyard to activate it."

[[overview.rulings]]
cards = ["Colossal Grave-Reaver"]
note = "Cards milled together arrive at once, so it returns only one creature per mill, however many creatures hit the graveyard."

[[overview.rulings]]
cards = ["Amulet of Vigor"]
note = "It only untaps permanents that enter tapped. A land that enters untapped and is tapped later won't trigger it."

[[overview.rulings]]
cards = ["Field of the Dead"]
note = "It counts itself and the entering land, but only one land of each name counts toward seven."

[[overview.rulings]]
cards = ["Dread Return"]
note = "You choose the target before paying the flashback cost, so you can't reanimate a creature you sacrifice for it. Flashback is sorcery-speed."

[[overview.rulings]]
cards = ["Lotus Vale"]
note = "It needs two untapped lands to sacrifice as it enters. If you can't, it goes straight to your graveyard. The same applies when Teval or Lumra tries to return it."

[[overview.rulings]]
cards = ["Living Death"]
note = "Every player's creatures are swapped at once, so check opponents' graveyards before casting it."
+++
