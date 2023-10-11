{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNg6DO3n0GA7R1Wn0i1LuNJ"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 16,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5BqjLTnfXNK4",
        "outputId": "79c2dc2c-2557-4e41-9338-0da453432c32"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Введите количество магазинов\n",
            "1\n",
            "Введите название магазина №1: 111\n",
            "Введите количество товаров\n",
            "1\n",
            "Введите название товара №1: 1111\n",
            "Введите цену товара №1111 Для магазина 111: 100\n",
            "Введите требуемые товары через запятую без пробелов: 1111\n",
            "{'111': 0}\n",
            "The shop with the lowest price is 111 : 100\n"
          ]
        }
      ],
      "source": [
        "shopsList = [];\n",
        "goodsList = [];\n",
        "numberOfShops = int(input(\"Введите количество магазинов\\n\"));\n",
        "i = 1;\n",
        "while i <= numberOfShops:\n",
        "  shopsList.append(input(f\"Введите название магазина №{i}: \"));\n",
        "  i += 1;\n",
        "\n",
        "numberOfGoods = int(input(\"Введите количество товаров\\n\"));\n",
        "shopsAndGoods = {};\n",
        "i = 1;\n",
        "while i <= numberOfGoods:\n",
        "  goodsName = input(f\"Введите название товара №{i}: \");\n",
        "\n",
        "  goodsPrices = {};\n",
        "  for shop in shopsList:\n",
        "    goodsPrices[shop] = int(input(f\"Введите цену товара №{goodsName} Для магазина {shop}: \"));\n",
        "\n",
        "  shopsAndGoods[goodsName] = goodsPrices;\n",
        "  i += 1;\n",
        "\n",
        "requiredGoods = input(\"Введите требуемые товары через запятую без пробелов: \").split(\",\");\n",
        "shopsAndPrices = dict.fromkeys(shopsList, 0);\n",
        "print(shopsAndPrices);\n",
        "for good in requiredGoods:\n",
        "  for shop in shopsAndGoods[good]:\n",
        "    shopsAndPrices[shop] += shopsAndGoods[good][shop];\n",
        "\n",
        "\n",
        "minPriceAndShop = (100000000, \"no_shop\");\n",
        "for shop in shopsAndPrices:\n",
        "  price = shopsAndPrices[shop];\n",
        "  if price < minPriceAndShop[0]:\n",
        "    minPriceAndShop = (price, shop);\n",
        "\n",
        "print(f\"The shop with the lowest price is {minPriceAndShop[1]} : {minPriceAndShop[0]}\");"
      ]
    }
  ]
}