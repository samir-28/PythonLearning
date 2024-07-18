from countryinfo import CountryInfo

country=CountryInfo(input("Enter the country name:"))

print("Country name:",country.name())
print("Capital:",country.capital())
print("Population:",country.population())
print("Area(in kms):",country.area())
print("Region:",country.region())
print("Subregion:",country.subregion())
print("Currency:",country.currencies())
print("Languages:",country.languages())
print("Borders:",country.borders())
print("Demonym:",country.demonym())

