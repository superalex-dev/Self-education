amount = float(input())
From = input()
To = input()

resultinBGN= amount

if From == 'USD':
    resultinBGN *= 1.79549
elif From == 'EUR':
    resultinBGN *= 1.95583

elif From == 'GBP':
    resultinBGN *= 2.53405

output = resultinBGN

if To == 'USD':
    output /= 1.79549

elif To == 'EUR':
    output /= 1.95583

elif To == 'GBP':
    output /= 2.53405


print(round(output,2), To)