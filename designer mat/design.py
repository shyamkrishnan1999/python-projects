def mid_pat(x):
    for i in range(0, x):
        print(".|.", end="")


def side_pat(x):
    for i in range(0, x):
        print("-", end="")


data = input().split()
n = int(data[0])
m = int(data[1])
val = (m - 3) // 2
mid = 1

for i in range(0, n // 2):
    side_pat(val)
    mid_pat(mid)
    side_pat(val)
    val = val - 3
    mid = mid + 2
    print("")

cent = (m - 7) // 2
side_pat(cent)
print("WELCOME", end="")
side_pat(cent)
print("")

for i in range(0, n // 2):
    val = val + 3
    mid = mid - 2
    side_pat(val)
    mid_pat(mid)
    side_pat(val)
    print("")
