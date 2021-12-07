# •	Първи ред – цена на скумрията на килограм. Реално число в интервала [0.00…40.00]
# •	Втори ред – цена на цацата на килограм. Реално число в интервала [0.00…30.00]
# •	Трети ред – килограма паламуд. Реално число в интервала [0.00…50.00]
# •	Четвърти ред – килограма сафрид. Реално число в интервала [0.00… 70.00]
# •	Пети ред – килограма миди. Цяло число в интервала [0 ... 100]
price_of_mackerel_kg = float(input())
price_of_sprat_kg = float(input())
kg_bonito = float(input())
kg_scad = float(input())
kg_mussels = int(input())
# •	Паламуд – 60% по-скъп от скумрията
# •	Сафрид – 80% по-скъп от цацата
# •	Миди – 7.50 лв. за килограм
price_of_bonito_kg = price_of_mackerel_kg * 0.6 + price_of_mackerel_kg
price_of_scad_kg = price_of_sprat_kg * 0.8 + price_of_sprat_kg
price_of_mussels_kg = 7.5

cost_of_bonito = kg_bonito * price_of_bonito_kg
cost_of_scad = kg_scad * price_of_scad_kg
cost_of_mussels = kg_mussels * price_of_mussels_kg

total_cost = round (cost_of_bonito + cost_of_mussels + cost_of_scad, 2)
print (f"{total_cost:.2f}")

# # •	Първи ред – цена на скумрията на килограм. Реално число в интервала [0.00…40.00]
# # •	Втори ред – цена на цацата на килограм. Реално число в интервала [0.00…30.00]
# # •	Трети ред – килограма паламуд. Реално число в интервала [0.00…50.00]
# # •	Четвърти ред – килограма сафрид. Реално число в интервала [0.00… 70.00]
# # •	Пети ред – килограма миди. Цяло число в интервала [0 ... 100]
# price_of_mackerel_kg = float(input())
# price_of_sprat_kg = float(input())
# kg_bonito = float(input())
# kg_scad = float(input())
# kg_mussels = float(input())
# # •	Паламуд – 60% по-скъп от скумрията
# # •	Сафрид – 80% по-скъп от цацата
# •	Миди – 7.50 лв. за килограм
# price_of_bonito_kg = round (price_of_mackerel_kg * 0.6 + price_of_mackerel_kg, 2)
# price_of_scad_kg = round (price_of_sprat_kg * 0.8 + price_of_sprat_kg, 2)
# price_of_mussels_kg = 7.5
#
# cost_of_bonito = round (kg_bonito * price_of_bonito_kg, 2)
# cost_of_scad = round (kg_scad * price_of_scad_kg, 2)
# cost_of_mussels = round (kg_mussels * price_of_mussels_kg, 2)
#
# total_cost = round (cost_of_bonito + cost_of_mussels + cost_of_scad, 2)
# print(total_cost)

# # •	Първи ред – цена на скумрията на килограм. Реално число в интервала [0.00…40.00]
# # •	Втори ред – цена на цацата на килограм. Реално число в интервала [0.00…30.00]
# # •	Трети ред – килограма паламуд. Реално число в интервала [0.00…50.00]
# # •	Четвърти ред – килограма сафрид. Реално число в интервала [0.00… 70.00]
# # •	Пети ред – килограма миди. Цяло число в интервала [0 ... 100]
# price_of_mackerel_kg = float(input())
# price_of_sprat_kg = float(input())
# kg_bonito = float(input())
# kg_scad = float(input())
# kg_mussels = int(input())
# # •	Паламуд – 60% по-скъп от скумрията
# # •	Сафрид – 80% по-скъп от цацата
# # •	Миди – 7.50 лв. за килограм
# price_of_bonito_kg = price_of_mackerel_kg * 1.6
# price_of_scad_kg = price_of_sprat_kg * 1.8
# price_of_mussels_kg = 7.5
#
# cost_of_bonito = round (kg_bonito * price_of_bonito_kg, 2)
# cost_of_scad = round (kg_scad * price_of_scad_kg, 2)
# cost_of_mussels = round (kg_mussels * price_of_mussels_kg, 2)
#
# total_cost = round (cost_of_bonito + cost_of_mussels + cost_of_scad, 2)
# print (f"{total_cost:.2f}")
