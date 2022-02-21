from langdetect import detect, detect_langs
print(detect("War doesn't show who's right, just who's left."))
print(detect_langs("Ein, zwei, drei, vier, five, one two, yksi, kaksi."))
print(detect_langs("Otec matka syn."))
print(detect_langs("Jag heter Peter. Jag är tjugofyra år."))
print(detect_langs("Hej, jag heter Saga Torstensson. Jag är tjugofyra år och bor i Halmstad. Det är första gången jag är här, så jag tänkte inte orda så mycket utan mest lyssna. Jag vill bara säga att jag är glad att ni har välkomnat mig här i er lilla skrivarcirkel."))
