def beregn_gjennomsnitt(liste):
    gjennomsnitt = sum(liste) / len(liste)
    print("Gjennomsnittet av tallene er:",  gjennomsnitt)


# Eksempel på bruk ved å kalle funksjonen
tall_liste = [2, 4, 6, 8, 12]
beregn_gjennomsnitt(tall_liste)