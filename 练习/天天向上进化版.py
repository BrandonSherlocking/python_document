#向上5天，向下2天
dayup,dayfactor = 1.0, 0.01
for i in range(365):
    if i%7 in [6,0]:
        dayup = dayup*(1-dayfactor)
    else :
        dayup = dayup*(1+dayfactor)
print('向上五天，向下两天的力量：{:.2f}'.format(dayup))

#优化，需要多努力才能比的上每天都努力的人
def dayUp(df):
    dayup=1
    for i in range(365):
        if i % 7 in [6,0]:
            dayup = dayup*(1-0.01)
        else:
            dayup = dayup*(1+df)
    return dayup
dayfactor = 0.01
while (dayUp(dayfactor)<37.78):
    dayfactor+=0.001
print('每天努力的程度是：{:.3f}'.format(dayfactor))
