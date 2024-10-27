

Жадібний алгоритм (find_coins_greedy) працює значно швидше, оскільки має часову складність O(m), де m — кількість номіналів монет, і підходить для задач з добре структурованими наборами монет. Наприклад, для суми 113113 він виконався за 0.000010 секунд. Однак, він не завжди дає оптимальне рішення, особливо для нестандартних наборів монет.

Алгоритм динамічного програмування (find_min_coins) має часову складність O(n \* m) і завжди знаходить мінімальну кількість монет. Але для великих сум він значно повільніший — для суми 113113 виконався за 0.189056 секунд. Це робить його більш вимогливим до ресурсів, але він забезпечує оптимальність для будь-якого набору монет.

The greedy algorithm (find_coins_greedy) works significantly faster, with a time complexity of O(m), where m is the number of coin denominations, and is suitable for problems with well-structured coin sets. For example, for the amount of 113113, it executed in 0.000010 seconds. However, it does not always provide an optimal solution, especially for non-standard coin sets.

The dynamic programming algorithm (find_min_coins) has a time complexity of O(n \* m) and always finds the minimal number of coins. However, it is much slower for large sums — for the amount of 113113, it took 0.189056 seconds. This makes it more resource-intensive, but it guarantees an optimal solution for any coin set.
