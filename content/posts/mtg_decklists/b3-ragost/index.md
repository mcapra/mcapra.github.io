+++
title = "[Bracket 3] Ragost, Deft Gastronaut"
bracket = 3
commanders = ['Ragost, Deft Gastronaut (EOE) 300']
archetypes = ["Artifacts", "Lifegain", "Burn"]
decklist_url = "https://moxfield.com/decks/tWnSl-B_2U-BtNycRCZZKQ"
deck_authors = [{ name = "Tybalto", url = "https://moxfield.com/users/Tybalto" }]
date = 2026-05-13T06:13:34+00:00
draft = false

[overview]
summary = "Boros artifacts without aggro. Ragost makes every artifact a Food, then eats one for 3 damage to each opponent, and untaps at any end step after you've gained life. Cheap artifacts that draw when they die keep the engine fed, and Nuka-Cola Vending Machine provides the infinite finish."
strengths = [
  "Every artifact is ammunition: each one is 3 damage to every opponent, and eggs like Ichor Wellspring and the Implements draw a card as they go.",
  "Ragost untaps at every player's end step if you gained life, and Drumbellower and Sting add more untaps. That's up to three activations a turn, or 12 damage-dealing sacrifices per round.",
  "Lifegain is built in: every artifact can be eaten for 3 life, and lifelink from Basilisk Collar or Shadowspear turns each activation into 9. In one of Tybalto's games it reached 88 life.",
  "Real interaction for Boros, with 11 Removal cards plus free protection in Flawless Maneuver and Deflecting Swat.",
]
weaknesses = [
  "It depends on Ragost. Tybalto had to recast him several times in some games, and without him the artifacts are just artifacts.",
  "Slow before turn 5, and Tybalto's games show it struggling against Voltron commanders that win quickly. It won 5 of their 23 logged games.",
  "Artifact hate is crippling. Vandalblast, Bane of Progress and Haywire Mite each set it back a long way in their games.",
  "The plan is obvious once Ragost is out, so expect to become the archenemy early.",
]
gameplan = [
  "Early: play Rocks, eggs and cheap disruption like Esper Sentinel or Authority of the Consuls. Cast Ragost on turn 2 or 3, and use Urza's Saga or Tezzeret to fetch Basilisk Collar or Shadowspear.",
  "Mid: activate Ragost every turn, including opponents' turns, and gain life before each end step so he untaps. Add untappers like Drumbellower and Sting, and refill with eggs and The One Ring.",
  "Late: assemble Nuka-Cola Vending Machine with Krark-Clan Ironworks and Reckless Fireweaver or Weftstalker Ardent, or with Grinding Station to mill the table. Otherwise drain them down with repeated Ragost activations, or use Aetherflux Reservoir.",
]
mulligan = [
  "3–4 of the 33 lands with both colors (22 white mana symbols to red's 18). Ragost needs {R}{W} on turn 2, and the fetches can find Plateau, Sacred Foundry or Elegant Parlor for both.",
  "Two cheap artifacts to feed Ragost, ideally eggs that draw when they die. A hand of only lands and big spells has nothing to eat.",
  "A way to gain life each turn, so Ragost untaps: Basilisk Collar, Shadowspear, Spirit Loop, Scrapheap or Urza's Saga to fetch one.",
]

[[overview.combos]]
cards = ["Ragost, Deft Gastronaut", "Nuka-Cola Vending Machine", "Krark-Clan Ironworks", "Reckless Fireweaver"]
result = "Infinite colorless mana and infinite artifacts entering. With Reckless Fireweaver or Weftstalker Ardent out, each Treasure pings every opponent, so it wins on the spot."
kind = "infinite"
steps = [
  "Sacrifice a Treasure to Krark-Clan Ironworks for {C}{C}. Ragost makes it a Food.",
  "Nuka-Cola Vending Machine makes a tapped Treasure, which is also a Food.",
  "Repeat.",
]
source = "https://commanderspellbook.com/combo/1575-4659-6748/"

[[overview.combos]]
cards = ["Ragost, Deft Gastronaut", "Nuka-Cola Vending Machine", "Grinding Station"]
result = "Infinite mill. Tybalto won two of their logged games by milling the whole table this way."
kind = "infinite"
steps = [
  "Tap Grinding Station and sacrifice a Treasure to mill three cards from a player.",
  "Nuka-Cola Vending Machine makes a Treasure, and Grinding Station untaps as it enters.",
  "Repeat.",
]
source = "https://commanderspellbook.com/combo/1575-3698-6748/"

[[overview.combos]]
cards = ["Academy Manufactor", "Nuka-Cola Vending Machine", "Krark-Clan Ironworks"]
result = "The same loop without Ragost: Manufactor turns each Treasure into a Clue, a Food and a Treasure, so sacrificing the Food keeps it going."
kind = "infinite"
source = "https://commanderspellbook.com/combo/1575-4231-4659/"

[[overview.combos]]
cards = ["Ratchet, Field Medic // Ratchet, Rescue Racer", "Ragost, Deft Gastronaut", "Basilisk Collar"]
result = "Cast Ratchet converted for {1}{W}. A nontoken artifact eaten by a lifelinking Ragost converts him, and the 9 life converts him back to return that artifact. With a Rock, it can pay for its own sacrifice on each player's turn."

[[overview.combos]]
cards = ["Ragost, Deft Gastronaut", "Drumbellower", "Sting, the Glinting Dagger"]
result = "Drumbellower untaps him in each opponent's untap step, and Sting untaps him at each combat, for up to three activations a turn."

[[overview.combos]]
cards = ["Ragost, Deft Gastronaut", "Scrapheap"]
result = "Every artifact Ragost eats gains you 1 life, so he always untaps at the end step."

[[overview.combos]]
cards = ["Ragost, Deft Gastronaut", "Chandra's Incinerator"]
result = "Each activation also deals 3 damage to a creature or planeswalker of each opponent. In a four-player game, one activation alone brings the Incinerator's cost down to {R}."

[[overview.combos]]
cards = ["Osgir, the Reconstructor", "Sol Ring"]
result = "Tap Sol Ring for {C}{C}, spend one to eat it with Ragost and the other to have Osgir make two Sol Ring copies."

[[overview.combos]]
cards = ["Treasure Nabber", "Ragost, Deft Gastronaut"]
result = "Artifacts an opponent taps for mana become yours until your next turn ends, and Ragost can eat them before you have to give them back."

[[overview.rulings]]
cards = ["Ragost, Deft Gastronaut"]
note = "He untaps only if you gained life before the end step begins; gaining life during the end step is too late. He has {T} in his cost, so he can't activate the turn he arrives without haste."

[[overview.rulings]]
cards = ["Ragost, Deft Gastronaut"]
note = "One artifact can't pay two sacrifice costs, so you can't eat a Food for its own life ability and Ragost's damage at once."

[[overview.rulings]]
cards = ["Nuka-Cola Vending Machine"]
note = "It triggers whenever you sacrifice a Food for any reason, and Ragost makes every artifact a Food. That includes Treasures sacrificed for mana and artifacts sacrificed to Krark-Clan Ironworks or Grinding Station."

[[overview.rulings]]
cards = ["Academy Manufactor"]
note = "Ragost turning artifacts into Foods isn't creating Food tokens, so Manufactor only triples tokens you actually create."

[[overview.rulings]]
cards = ["Ratchet, Field Medic // Ratchet, Rescue Racer"]
note = "If several life gains happen at once, he converts only once. His mana value is always that of the front face."

[[overview.rulings]]
cards = ["Goblin Engineer"]
note = "It only returns artifacts with mana value 3 or less, so it can't bring back Krark-Clan Ironworks. Ratchet can, once you've gained 4 life that turn."

[[overview.rulings]]
cards = ["Chandra's Incinerator"]
note = "It counts all noncombat damage dealt to opponents this turn, even if they gained life back, but only reduces generic mana. It always costs at least {R}."

[[overview.rulings]]
cards = ["Treasure Nabber"]
note = "It only steals artifacts tapped for mana using {T}, not ones tapped for improvise. They stay tapped when you gain control."

[[overview.rulings]]
cards = ["Aetherflux Reservoir"]
note = "Paying 50 life at exactly 50 puts you at 0 and you lose, so you need 51."
+++
