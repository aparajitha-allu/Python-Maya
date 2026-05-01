cp, sp = map(int, input().split())

loss = cp - sp
loss_percent = (loss / cp) * 100

print("{:.2f}".format(loss_percent))