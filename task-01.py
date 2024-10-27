import time

class Coin:
    def __init__(self, value):
        self.value = value


def find_coins_greedy(amount, coins=None):
    # amount: сума, яку необхідно видати рештою
    # coins: набір монет
    # return: словник з номіналами монет та їх кількістю
    if coins is None:
        # Якщо набір монет не заданий, використовуємо стандартний набір монет.
        coins = [Coin(50), Coin(25), Coin(10), Coin(5), Coin(2), Coin(1)]
     # Сортуємо монети за спаданням номіналу, щоб використовувати найбільші номінали спочатку.
    coins.sort(key=lambda x: x.value, reverse=True)

    result = {}
    # Проходимося по кожній монеті в списку
    for coin in coins:
        # Визначаємо кількість монет даного номіналу, які можна використати для видачі решти
        count =  amount // coin.value
        if count > 0:
            # Додаємо монету до результату, якщо можна видати хоча б одну монету даного номіналу
            result[coin.value] = count
            # Зменшуємо залишкову суму, яку потрібно видати
            amount -= coin.value * count
    return result


def find_min_coins(amount, coins=None):
    if coins is None:
        # поки теж саме що і у попередній функції
        coins = [Coin(50), Coin(25), Coin(10), Coin(5), Coin(2), Coin(1)]
        coins.sort(key=lambda x: x.value, reverse=True)
        # Ініціалізація масиву для зберігання мінімальної кількості монет для кожної суми від 0 до amount.
    min_coins = [float('inf')] * (amount + 1)
    # Для суми 0 потрібно 0 монет
    min_coins[0] = 0
     # Масив для збереження останньої використаної монети
    coins_used = [0] * (amount + 1)

     # Проходимося по всіх можливих сумах від 1 до amount
    for i in range(1, amount + 1):
        for coin in coins:
             # Перевіряємо, чи можна використовувати цю монету для поточної суми
            if i >= coin.value and min_coins[i - coin.value] +1 < min_coins[i]:
                # Оновлюємо мінімальну кількість монет для поточної суми
                min_coins[i] = min_coins[i - coin.value] +1
                # Зберігаємо номінал монети, яка використовується для досягнення поточної суми
                coins_used[i] = coin.value
    
    result = {}
    current_amount = amount
    while current_amount > 0:
        coin_value  =  coins_used[current_amount]
        if coin_value in result:
            # Якщо монета вже є в результаті, збільшуємо її кількість
            result[coin_value] += 1
        else:
            # Інакше додаємо монету до результату
            result[coin_value] = 1
        # Зменшуємо поточну суму на номінал використаної монети
        current_amount -= coin_value
    return result




# use

coins = [Coin(50), Coin(25), Coin(10), Coin(5), Coin(2), Coin(1)]
amount = 113113

start_time = time.perf_counter()
greedy_result = find_coins_greedy(amount, coins)
greedy_time = time.perf_counter() - start_time
print("Greedy Algorithm Result:", greedy_result, f"Algorithm Time: {greedy_time:.6f} seconds")

start_time = time.perf_counter()
dp_result = find_min_coins(amount, coins)
dp_time = time.perf_counter() - start_time
print("Dynamic Programming Result:", dp_result, f"Algorithm Time: {dp_time:.6f} seconds")


