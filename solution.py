# T1
text = 'Berlin is a world city of culture, politics, media and science.'

print(len(text))


# T2
print(text[0], text[-1])


# T3
print(text[0:3].upper())


# T4
text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital"
print('B appears:', text.count('B'), 'times.')


# T5
text = "Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau."

print('Last ten characters:', text[-10:])


# T6
text = "---Python programming---"
text = text.replace('-', '')

print(text)


# T7
firstname = "Johannes"
lastname = "Gohl"
list = firstname, lastname

print(f'Firstname: {list[0]} \nLastname: {list[1]}')
