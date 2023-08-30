import math

ONE_TALENT_TO_POUND = 20
ONE_POUND_TO_LOT = 32
ONE_LOT_TO_GRAM = 13.3
ONE_KILOGRAM_TO_GRAM = 1000
talent = float(input("Enter talents:"))
pound = float(input("Enter pounds:"))
lot = float(input("Enter lots:"))

talentsTOGram = ONE_TALENT_TO_POUND * ONE_POUND_TO_LOT * ONE_LOT_TO_GRAM * talent
poundsTOGram = ONE_POUND_TO_LOT * ONE_LOT_TO_GRAM * pound
lotsTOGram = ONE_LOT_TO_GRAM * lot

talentsTOKilogram = (talentsTOGram / 1000)
poundsTOKilogram = (poundsTOGram / 1000)
lotsTOKilogram = (lotsTOGram / 1000)
totalWeightInKilos = talentsTOKilogram + poundsTOKilogram + lotsTOKilogram
weightKiloPart = int(totalWeightInKilos)
weightGramPart = format((totalWeightInKilos-int(totalWeightInKilos))*1000, ".2f")
print("The weight in modern units:")
print(str(weightKiloPart) + " kilograms and " + str(weightGramPart) + " grams.")

