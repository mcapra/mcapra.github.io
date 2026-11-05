+++
title = "[Bracket 3] Sephiroth, Fabled SOLDIER"
bracket = 3
commanders = ['Sephiroth, Fabled SOLDIER // Sephiroth, One-Winged Angel (FIN) 382']
archetypes = ["Aristocrats", "Combo", "Graveyard"]
decklist_url = "https://moxfield.com/decks/N3DTSu6qHU-M2q24sfqiEw"
deck_authors = [{ name = "Panzer_MTG", url = "https://moxfield.com/users/Panzer_MTG" }]
date = 2026-11-02T11:30:24+00:00
draft = false

[overview]
summary = "Mono-black sacrifice. Sephiroth costs 3, trades creatures for cards and drains on every death. Four drains in a turn flip him into a 5/5 flyer and give you a permanent Blood Artist emblem, and flipping him again adds another. Panzer calls it a grindy deck, but it also holds several infinite loops."
strengths = [
  "The flip is easy to force: with one creature on each side, Accursed Marauder, Plaguecrafter, Fleshbag Marauder and similar effects kill four creatures at once. Flare of Malice can do it for free at instant speed.",
  "Emblems can't be removed and they stack, so even a board wipe from an opponent drains the table once one is out.",
  "Fodder keeps coming back: Gravecrawler, Bloodghast, Reassembling Skeleton and Nether Traitor all return cheaply, and Forsaken Miner returns for {B} whenever a drain targets an opponent.",
  "Black's best interaction, with 19 Removal and 4 Board Wipes. Wipes like The Meathook Massacre and Toxic Deluge double as drain once you have an emblem.",
]
weaknesses = [
  "Graveyard hate cuts off the recursive creatures that fuel both the grind and the loops. Exile effects also stop creatures dying, so nothing drains.",
  "Mono-black can't answer artifacts here, and enchantments only fall to Feed the Swarm, Withering Torment and Gaius van Baelsar.",
  "Grave Pact and Dictate of Erebos can lock opponents out of the game, and Panzer warns they may not be welcome at your table. Expect to become the target.",
  "Ramp is thin: Sol Ring and rituals early, then mana from sacrificing creatures. Culling the Weak and the altars do nothing on an empty board.",
]
gameplan = [
  "Early: play one or two cheap creatures first, so Sephiroth has something to sacrifice as he enters. He can land on turn 2 off Sol Ring, or turn 1 off Dark Ritual.",
  "Mid: flip him as soon as each opponent has a creature, using an each-player sacrifice effect. Then sacrifice on opponents' turns too, so once-per-turn cards like Morbid Opportunist, Ghoulish Procession and Gisa work every turn.",
  "Late: stack emblems by returning Sephiroth to his front face, attack as the Angel to turn tokens into cards, and assemble a loop. Without one, drain the table down, then finish with Torment of Hailfire, Gray Merchant or Bolas's Citadel.",
]
mulligan = [
  "3–4 land drops from the 30 lands and 4 spells that double as lands. Every spell is black, so colors aren't a concern, but Cabal Coffers and Urborg are bonuses rather than keeps on their own.",
  "Two cheap bodies to feed Sephiroth: Gravecrawler, Forsaken Miner, Nested Shambler or Bitterblossom. He's always available in the command zone, so you're mulliganing for fodder, not for him.",
  "A sacrifice outlet or payoff, such as Viscera Seer, Carrion Feeder, Blood Artist or Zulaport Cutthroat. Rituals and Village Rites need creatures on the board, so don't count them as plays.",
]

[[overview.combos]]
cards = ["Warren Soultrader", "Gravecrawler", "Sephiroth, Fabled SOLDIER"]
result = "Infinite drain with no mana needed, which kills the table. You need at least 2 life to start."
kind = "infinite"
steps = [
  "Pay 1 life and sacrifice Gravecrawler to Warren Soultrader.",
  "Sephiroth (or an emblem) drains an opponent, gaining the life back.",
  "Soultrader makes a Treasure. Sacrifice it for {B} and cast Gravecrawler from your graveyard.",
  "Repeat.",
]
source = "https://commanderspellbook.com/combo/2577-5670-6578/"

[[overview.combos]]
cards = ["Gravecrawler", "Phyrexian Altar"]
result = "Infinite deaths and enters. It needs another Zombie to recast Gravecrawler, and Sephiroth, an emblem or Blood Artist to win."
kind = "infinite"
steps = [
  "Sacrifice Gravecrawler to Phyrexian Altar for {B}.",
  "Cast Gravecrawler from your graveyard with that {B}.",
  "Repeat.",
]
source = "https://commanderspellbook.com/combo/2577-4050/"

[[overview.combos]]
cards = ["Pitiless Plunderer", "Ashnod's Altar", "Reassembling Skeleton"]
result = "Infinite colorless mana and infinite deaths. Spend the mana on a huge Torment of Hailfire, or let your drain finish the table."
kind = "infinite"
steps = [
  "Sacrifice Reassembling Skeleton to Ashnod's Altar for {C}{C}.",
  "Pitiless Plunderer makes a Treasure. Sacrifice it for {B}.",
  "Pay {1}{B} to return the Skeleton, leaving you {C} ahead.",
  "Repeat.",
]
source = "https://commanderspellbook.com/combo/1580-2034-4871/"

[[overview.combos]]
cards = ["Forsaken Miner", "Phyrexian Altar", "Sephiroth, Fabled SOLDIER"]
result = "Infinite drain, because targeting an opponent with the drain is a crime that lets the Miner return."
kind = "infinite"
steps = [
  "Sacrifice Forsaken Miner to Phyrexian Altar for {B}.",
  "Sephiroth's trigger targets an opponent, which commits a crime.",
  "Pay {B} to return the Miner as its trigger resolves.",
  "Repeat.",
]
source = "https://commanderspellbook.com/combo/4050-5544-6578/"

[[overview.combos]]
cards = ["Ayara, First of Locthwain", "Plague of Vermin"]
result = "Pay all but 1 of your life. Each black Rat that enters drains every opponent and gains you 1, so it wins if you have more life than each of them."
kind = "win"
source = "https://commanderspellbook.com/combo/884-5035/"

[[overview.combos]]
cards = ["Tombstone Stairwell", "Blood Artist"]
result = "Every player makes a 2/2 for each creature card in their graveyard at each upkeep, and they're all destroyed at each end step. Every one of those deaths drains, and Sephiroth or an emblem adds more."
source = "https://commanderspellbook.com/combo/2842-6215/"

[[overview.combos]]
cards = ["Grave Pact", "Sephiroth, Fabled SOLDIER"]
result = "One of your creatures dying makes each opponent sacrifice one too. In a four-player game with creatures on every side, that's four deaths and a flip from one sacrifice."

[[overview.combos]]
cards = ["Accursed Marauder", "Sephiroth, Fabled SOLDIER"]
result = "Two mana for four deaths and an instant flip, if each opponent has a nontoken creature. You can sacrifice the Marauder itself, and it often takes a lone commander."

[[overview.combos]]
cards = ["Undying Malice", "Sephiroth, Fabled SOLDIER"]
result = "Cast it on the flipped Angel, then sacrifice him. He returns on his front face, so four more drains give you a second emblem. Not Dead After All and Malakir Rebirth do the same."

[[overview.combos]]
cards = ["Starscape Cleric", "Sephiroth, Fabled SOLDIER"]
result = "Each life you gain makes every opponent lose 1. So each drain costs the target 2 life and the other two opponents 1 each."

[[overview.rulings]]
cards = ["Sephiroth, Fabled SOLDIER"]
note = "He flips on the fourth time his own ability resolves in a turn. If he dies along with other creatures, it still triggers for them, but he won't transform. Emblem triggers are a different ability, so they don't count."

[[overview.rulings]]
cards = ["Sephiroth, Fabled SOLDIER"]
note = "To re-flip through Undying Malice or Unearth, leave him in the graveyard rather than moving him to the command zone. A double-faced card always returns with its front face up, and only transforming gives you an emblem."

[[overview.rulings]]
cards = ["Forsaken Miner"]
note = "It must already be in your graveyard when the crime happens, and each spell or ability is only one crime however many things it targets."

[[overview.rulings]]
cards = ["Gravecrawler"]
note = "It doesn't change when you can cast it, so Gravecrawler loops need your main phase with an empty stack. Once it's on the stack, losing your other Zombie doesn't matter."

[[overview.rulings]]
cards = ["Grave Pact"]
note = "It doesn't target, so hexproof doesn't help. It triggers once for each of your creatures that dies, and those sacrifices happen at the same time."

[[overview.rulings]]
cards = ["Plague of Vermin"]
note = "Paying continues until every player in a row declines, so a player who passed can pay again if someone else keeps going. All the Rats enter at once."

[[overview.rulings]]
cards = ["Tombstone Stairwell"]
note = "Each player controls the tokens they make, so opponents can attack with them. The tokens are also destroyed if the Stairwell leaves, which still counts as deaths."

[[overview.rulings]]
cards = ["Bolas's Citadel"]
note = "Normal timing still applies from the top of your library, and you need a land play for lands. X is 0, so Torment of Hailfire does nothing cast this way."

[[overview.rulings]]
cards = ["Sengir Autocrat"]
note = "When it leaves the battlefield, the Serf tokens are exiled and don't die, so sacrifice them first."
+++
