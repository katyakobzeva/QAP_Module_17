money = float(input("Сумма, которую вы хотите положить под процент = " ))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

tkb_bank = per_cent['ТКБ'] * money / 100
skb_bank = per_cent['СКБ'] * money / 100
vtb_bank = per_cent['ВТБ'] * money / 100
sber_bank = per_cent['СБЕР'] * money / 100

deposit = [tkb_bank, skb_bank, vtb_bank, sber_bank]
print(deposit)

max_deposit = max(deposit)
print("Максимальная сумма, которую вы можете заработать =  ", max_deposit)


