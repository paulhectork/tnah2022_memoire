"""
calculate F1 score of named entity linking using machine learning, based
on results provided by :
Soudani, Meherzi, Bouhafs, Frontini, Brando et al.,
'Adaptation et évaluation de systèmes de
reconnaissance et de résolution des entités nommées
pour le cas de textes littéraires français du 19ème siècle',
https://hal.archives-ouvertes.fr/hal-01925816
"""

candidate_dbp = 2 * (1 * 0.816) / (1 + 0.816)
candidate_bnf = 2 * (0.760 * 0.630) / (0.760 + 0.630)
candidate_wdt = 2 * (0.912 * 0.830) / (0.912 + 0.830)
nil_dbp = 2 * (0.367 * 1) / (0.367 + 1)
nil_bnf = 2 * (0.580 * 0.972) / (0.580 + 0.972)
nil_wdt = 2 * (0.440 * 1) / (0.440 + 1)

print(f"""
	score dbp: {candidate_dbp} - {nil_dbp},
	score bnf: {candidate_bnf} - {nil_bnf},
	score wd: {candidate_wdt} - {nil_wdt}
""")
