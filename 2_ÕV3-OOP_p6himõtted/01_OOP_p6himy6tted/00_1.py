class Doorbell:
    click_count = 0

    def __init__(self):
        self.click_count = 0

    def ring(self):
        print("Ringing..")
        self.click_count += 1
        Doorbell.click_count += 1

d1 = Doorbell()
d2 = Doorbell()

for _ in range(10): d1.ring()
for _ in range(4): d2.ring()
print(d1.click_count)         # 10
print(d2.click_count)         # 4
print(Doorbell.click_count)   # 14