current_population = 8.1
growth_rate = 0.0088

double_population = current_population * 2
quadruple_population = current_population * 4
year_of_double = None
year_of_quadruple = None

print("Year\tPopulation (billions)\tIncrease (billions)")

for year in range(1, 101):
    increase = current_population * growth_rate
    new_population = current_population + increase
    print(f"{year}\t{new_population:.2f}\t\t\t{increase:.2f}")
    
    if not year_of_double and new_population >= double_population:
        year_of_double = year
    if not year_of_quadruple and new_population >= quadruple_population:
        year_of_quadruple = year

    current_population = new_population

print("\nPopulation will double in year:", year_of_double)
print("Population will quadruple in year:", year_of_quadruple)
