# -*- coding: utf-8 -*-
"""Roblox trend snapshot for the game cost calculator and the Roblox trends article.

Read by hand from roblox.com/charts (Top Playing Now = all devices and locations; Top Trending and
Up-and-Coming = computer, US and South Korea). Players = concurrent players shown on the chart.
Refresh with each weekly check; keep game names exactly as Roblox shows them, minus emoji/update tags.
"""
CHECKED = "2026-10-06"
SOURCE = "https://www.roblox.com/charts"

# key = calculator genre; games = (name, concurrent players)
TRENDS = [
    dict(key="steal", games=[("Steal An Egg", "1.1M"), ("Steal a Brainrot", "85K"), ("Break and Steal an Egg", "43K"), ("Steal Animal Egg", "18K"), ("Steal ASMR!", "16K")]),
    dict(key="coophorror", games=[("Dandy's World", "166K"), ("99 Nights in the Forest", "157K"), ("Forsaken", "56K"), ("DOORS", "48K")]),
    dict(key="duels", games=[("RIVALS", "137K"), ("Murderers VS Sheriffs Duels", "86K"), ("Ball VS Ball", "33K"), ("Sniper Arena", "15K")]),
    dict(key="plus1", games=[("+1 Speed Keyboard Escape", "81K"), ("+1 Loot To Forge", "32K"), ("+1 Stone Skipping", "24K"), ("+1 Tongue Escape", "18K")]),
    dict(key="rng", games=[("Fish It!", "70K"), ("Fisch", "67K"), ("Anime Dice", "62K"), ("Sol's RNG", "30K")]),
    dict(key="pet", games=[("Adopt Me!", "186K"), ("Ride A Pet", "78K"), ("Pet Simulator 99", "50K"), ("7 Days Cat-Sitting", "16K")]),
    dict(key="verbsim", games=[("Build the Pyramid!", "13K"), ("Pet Store Tycoon", "12K"), ("Drill for Eggs", "12K"), ("Peel THE Potato", "10K"), ("Melt All The Ice!", "5K")]),
    dict(key="coopobby", games=[("Flee the Facility", "30K"), ("Grapple Cart Obby", "9K"), ("Carry the Glass Together!", "4K"), ("Chained Together", "1K")]),
]
