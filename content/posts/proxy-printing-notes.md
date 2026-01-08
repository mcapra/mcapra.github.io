+++
title = 'Proxy Printing Notes'
date = 2026-01-06T12:23:00-05:00
draft = false
+++
## Proxy Printing Notes

My hardware:
* Cricut Maker 3
* Canon PIXMA G7020

My software:
* https://github.com/luziferius/MTGProxyPrinter

Fancy-fancy paper is Red River Paper, specifically their [UltraPro Satin 270](https://www.redrivercatalog.com/browse/68lb-ultrapro-satin.html) (formerly sold as 68lb. UltraPro Satin 4.0). I've also found the [Polar Gloss Metallic 255](https://www.redrivercatalog.com/browse/66lb-polar-pearl-metallic-inkjet-photo-paper.html) to be a good stock if you want something foil-like. For dual-faced cards, I use their [60lb. Polar Matte Double-Sided](https://www.redrivercatalog.com/browse/60lb-polar-matte-double-sided.html). I find it's important for dual-faced cards to use a stock that has the same finish on both sides, else one face of the card may look washed out compared to the other. Not all inkjet papers necessarily have the same finish on both sides.

Less-fancy, but still good paper I use is either [Neenah's 110lb 94 Bright](https://www.amazon.com/dp/B006P1EQXA) or [Accent's 120lb Opaque White](https://www.amazon.com/dp/B0114MUOOO?th=1). The Accent stock is a bit chonky, but less floppy compared to the Neenah stock. It's a preference/taste thing IMO. Both the Accent and the Neenah stocks tend to have more washed-out dark tones and don't look as nice, but produce perfectly legible and playable cards IMO. I don't find the differences in print quality to be significantly different between the two stocks, just weight/handling differences.

Cost-wise, for a 100-card deck printed on 8.5x11 sheets, with 9 cards per sheet, fancy-fancy paper averages ~$6 per deck, less-fancy averages ~$0.60 for the Neenah stock and ~$2.53 for the heavier Accent stock. The Neenah stock is really great for starting out, and I use it for loads of other applications beyond MTG proxies. Crazy value, I usually keep ~2-3 reams of it on-hand. I find the cost of ink is negligible if you have an eco-tank printer -- of 15x total 100 card decks I made recently for a work playgroup I used maybe $20 worth of ink total.

Print settings, both on the printer itself and the device sending the print job (laptop/desktop typically) are equally as important as the paperstock used. Most fancy papers will provide recommended print settings based on the type of printer you have. May need to tweak and tune these to avoid bleeding, smearing, or washed out tones. The Neenah/Accent papers aren't too finnicky in my experience, but YMMV.

MTGProxyPrinter accepts decklists from most of the major providers -- I use Moxfield because their API exposes scryfall IDs which make capturing specific art easier. MTGProxyPrint doesn't easily handle dual-faced cards, and I usually remove those and stage them by hand in MTGProxyPrinter so a double-sided print lines up correctly. If you have a fancier printer that can handle dual-side printing without reloading the stock, this may not be an issue. MTGProxyPrinter also offers adjustments for the spacing, overlap, bleed, etc which can make dialing in the Cricut (or whatever cutting machine) template easier.

MTGProxyPrinter importing out of services other than Moxfield, which ***don't*** use scryfall IDs, can sometimes pull weird art -- Japanese text, phyrexian text, other versions of a card which are not necessarily desirable if you want people to be able to read the cards you're playing.

I typically play with the proxy cards sleeved, since most commercial cardstocks you can buy aren't really designed to be handled regularly like one might handle a playing card. Again, more of a preference/taste thing.

Cricut stuff, if you want a cutting machine, is its own rabbit hole to fall down. There's tons of good YouTube content out there to learn the basics. Cricut is a CNC cutting machine, not a die-cutting machine, so the cuts won't look quite as crisp compared to legit MTG cards. You could probably find a conventional, manual, die-cutting machine that's big enough to fit 8.5x11 sheets of paperstock, but you'd be on your own for creating the die. I did a lot of trial-and-error before working out a reusable Cricut project, and set of indexing jigs for the cutting sheets, that lined up nicely with the 9 cards on a single printed sheet. You could use Cricut's "Print Then Cut" functionality to avoid all that mess, but you'll only be able to squeeze 5 cards on a sheet of 8.5x11 instead of 9, and all of your cuts will take longer because the Cricut needs to index every cut first by the score marks.