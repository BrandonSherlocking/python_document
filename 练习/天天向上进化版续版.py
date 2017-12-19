def dayup(df):
    dayup=1
    for i in range(365):
        if i % 7 in [5, 6, 0]:
            dayup = dayup*(1+df)
    return dayup
dayfactor = 0.01
least = dayup(dayfactor)
print('一年后的能力值是：{:.3f}'.format(least))