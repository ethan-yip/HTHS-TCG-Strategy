import json, random, time, os
# Legendary Imports for Calc.

queenan = {
  "type" = "sci",
  "hp" = 300,
  "atk" = 60,
  "def" = 30,
  "base_dmg" = 100,
  "add_dmg_pt" = "15\s"
}

roche = {
  "type" = "lib",
  "hp" = 300,
  "atk" = 60,
  "def" = 30,
  "base_dmg" = 100,
  "add_dmg" = "50\la"
}

eng = {
  "type" = "math",
  "eff" = "pyz",
  "hp" = 300,
  "atk" = 40,
  "def" = 50,
  "base_dmg" = 100,
  "add_dmg_pt" = "10\pt",
}

hanas = {
  "type" = "eng",
  "hp" = 300, 
  "atk" = 50,
  "def" = 40,
  "base_dmg" = 100,
  "add_dmg" = "c\eng\20-a\eng\60"
}

l_cards = [queenan, roche, eng, hanas]
