sentence = input('Sentence:')

screenWidth = 80
textWidth = len(sentence)
boxWidth = textWidth + 8
left = (screenWidth - boxWidth) // 2
left1 = left - 4

print()
print(' '*left1 + '+' + '-'*(boxWidth) + '+')
print(' '*left + '|' + ' '*textWidth + '|')
print(' '*left + '|' + sentence + '|')
print(' '*left + '|' + ' '*textWidth + '|')
print(' '*left1 + '+' + '-'*(boxWidth) + '+')
print()
