for opposite in range(1, 21):
    for adjacent in range(opposite, 21):   
        for hypotenuse in range(adjacent, 21):  
            if opposite**2 + adjacent**2 == hypotenuse**2:
                print(f"({opposite}, {adjacent}, {hypotenuse})")
