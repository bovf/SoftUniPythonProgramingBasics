cat_breed = str(input())
cat_sex = str(input())


if cat_breed == "British Shorthair":
    if cat_sex == "m":
        human_years = 13
        human_months = human_years * 12
        cat_months = human_months / 6
        print(f"{cat_months:.0f} cat months")
    elif cat_sex == "f":
        human_years = 14
        human_months = human_years * 12
        cat_months = human_months / 6
        print(f"{cat_months:.0f} cat months")
elif cat_breed == "Siamese":
    if cat_sex == "m":
        human_years = 15
        human_months = human_years * 12
        cat_months = human_months / 6
        print(f"{cat_months:.0f} cat months")
    elif cat_sex == "f":
        human_years = 16
        human_months = human_years * 12
        cat_months = human_months / 6
        print(f"{cat_months:.0f} cat months")
elif cat_breed == "Persian":
    if cat_sex == "m":
        human_years = 14
        human_months = human_years * 12
        cat_months = human_months / 6
        print(f"{cat_months:.0f} cat months")
    elif cat_sex == "f":
        human_years = 15
        human_months = human_years * 12
        cat_months = human_months / 6
        print(f"{cat_months:.0f} cat months")
elif cat_breed == "Ragdoll":
    if cat_sex == "m":
        human_years = 16
        human_months = human_years * 12
        cat_months = human_months / 6
        print(f"{cat_months:.0f} cat months")
    elif cat_sex == "f":
        human_years = 17
        human_months = human_years * 12
        cat_months = human_months / 6
        print(f"{cat_months:.0f} cat months")
elif cat_breed == "American Shorthair":
    if cat_sex == "m":
        human_years = 12
        human_months = human_years * 12
        cat_months = human_months / 6
        print(f"{cat_months:.0f} cat months")
    elif cat_sex == "f":
        human_years = 13
        human_months = human_years * 12
        cat_months = human_months / 6
        print(f"{cat_months:.0f} cat months")
elif cat_breed == "Siberian":
    if cat_sex == "m":
        human_years = 11
        human_months = human_years * 12
        cat_months = human_months / 6
        print(f"{cat_months:.0f} cat months")
    elif cat_sex == "f":
        human_years = 12
        human_months = human_years * 12
        cat_months = human_months / 6
        print(f"{cat_months:.0f} cat months")
else:
    print(f"{cat_breed} is invalid cat!")