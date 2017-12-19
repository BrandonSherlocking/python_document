width = eval(input('Please enter width:'))

priceWidth = 10
itemWidth = width - priceWidth

headerFormat = '%-*s%*s'
Format = '%-*s%*.2f'

print('='*width)

print(headerFormat % (itemWidth, 'Item', priceWidth, 'Price'))

print('-'*width)

print(Format % (itemWidth, 'Apples', priceWidth, 0.4))
print(Format % (itemWidth, 'Pears', priceWidth, 0.5))
print(Format % (itemWidth, 'Cantaloupes', priceWidth, 1.92))
print(Format % (itemWidth, 'Dried Apriocts (16 oz.)', priceWidth, 8))
print(Format % (itemWidth, 'Prunes (4 lbs.)', priceWidth, 12))

print('='*width)