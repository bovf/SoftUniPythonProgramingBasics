total_change = float(input()) * 100

change_left = total_change


def coin_2_lv(lv):
    amount_of_coins = lv // 200
    return amount_of_coins


def coin_1_lv(lv):
    amount_of_coins = lv // 100
    return amount_of_coins


def coin_50_st(st):
    amount_of_coins = st // 50
    return amount_of_coins


def coin_20_st(st):
    amount_of_coins = st // 20
    return amount_of_coins


def coin_10_st(st):
    amount_of_coins = st // 10
    return amount_of_coins


def coin_5_st(st):
    amount_of_coins = st // 5
    return amount_of_coins


def coin_2_st(st):
    amount_of_coins = st // 2
    return amount_of_coins


def coin_1_st(st):
    amount_of_coins = st // 1
    return amount_of_coins


coin_2_lv_counter = 0
coin_1_lv_counter = 0
coin_50_st_counter = 0
coin_20_st_counter = 0
coin_10_st_counter = 0
coin_5_st_counter = 0
coin_2_st_counter = 0
coin_1_st_counter = 0

while change_left > 0:
    if coin_2_lv(change_left) >= 1:
        coin_2_lv_counter += coin_2_lv(change_left)
        change_left -= coin_2_lv(change_left) * 200
    if coin_1_lv(change_left) >= 1:
        coin_1_lv_counter += coin_1_lv(change_left)
        change_left -= coin_1_lv(change_left) * 100
    if coin_50_st(change_left) >= 1:
        coin_50_st_counter += coin_50_st(change_left)
        change_left -= coin_50_st(change_left) * 50
    if coin_20_st(change_left) >= 1:
        coin_20_st_counter += coin_20_st(change_left)
        change_left -= coin_20_st(change_left) * 20
    if coin_10_st(change_left) >= 1:
        coin_10_st_counter += coin_10_st(change_left)
        change_left -= coin_10_st(change_left) * 10
    if coin_5_st(change_left) >= 1:
        coin_5_st_counter += coin_5_st(change_left)
        change_left -= coin_5_st(change_left) * 5
    if coin_2_st(change_left) >= 1:
        coin_2_st_counter += coin_2_st(change_left)
        change_left -= coin_2_st(change_left) * 2
    if coin_1_st(change_left) >= 1:
        coin_1_st_counter += coin_1_st(change_left)
        change_left -= coin_1_st(change_left) * 1


coin_total = int(coin_2_lv_counter +
                 coin_1_lv_counter +
                 coin_50_st_counter +
                 coin_20_st_counter +
                 coin_10_st_counter +
                 coin_5_st_counter +
                 coin_2_st_counter +
                 coin_1_st_counter)

print(coin_total)