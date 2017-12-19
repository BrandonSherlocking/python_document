earthw=input('please input you weight:')
nu=eval(earthw)
for i in range(1,11):
    nu+=0.5
moonthw=nu*0.165
print('you weight in earth is {}Kg \nin moonth is {:.3f}Kg'.format(nu, moonthw))
