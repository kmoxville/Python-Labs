# -*- coding: utf-8 -*-
shopsList = [];
goodsList = [];
numberOfShops = int(input("Введите количество магазинов\n"));
i = 1;
while i <= numberOfShops:
  shopsList.append(input(f"Введите название магазина №{i}: "));
  i += 1;

numberOfGoods = int(input("Введите количество товаров\n"));
shopsAndGoods = {};
i = 1;
while i <= numberOfGoods:
  goodsName = input(f"Введите название товара №{i}: ");

  goodsPrices = {};
  for shop in shopsList:
    goodsPrices[shop] = int(input(f"Введите цену товара №{goodsName} Для магазина {shop}: "));

  shopsAndGoods[goodsName] = goodsPrices;
  i += 1;

requiredGoods = input("Введите требуемые товары через запятую без пробелов: ").split(",");
shopsAndPrices = dict.fromkeys(shopsList, 0);
print(shopsAndPrices);
for good in requiredGoods:
  for shop in shopsAndGoods[good]:
    shopsAndPrices[shop] += shopsAndGoods[good][shop];


minPriceAndShop = (100000000, "no_shop");
for shop in shopsAndPrices:
  price = shopsAndPrices[shop];
  if price < minPriceAndShop[0]:
    minPriceAndShop = (price, shop);

print(f"The shop with the lowest price is {minPriceAndShop[1]} : {minPriceAndShop[0]}");
