"""Väljasta ekraanile kõikvõimalikud kombinatsioonid kujul "x - y - z", kus x, y ja z on mistahes täisarvud 1-st 20-ni
(20 kaasaarvatud). Samuti loenda, mitu sellist kombinatsiooni leiti. Tulemus:

1 - 1 - 1
1 - 1 - 2
​1 - 1 - 3
[...]
​15 - 12 - 2
​15 - 12 - 3
[...]
20 - 20 - 19
20 - 20 - 20
Kokku leiti 8000 kombinatsiooni."""

range_list = range(20)
count = 0
for x in range_list:
    for y  in range_list:
        for z in range_list:
            count += 1
            print(f"{x + 1} - {y + 1} - {z + 1}")
print(f"Kokku leiti {count} kombinatsiooni.")