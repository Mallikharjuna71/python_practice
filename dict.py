d = {}

d['name'] = 'Madara uchiha'
d['kills'] = 80000
d['nick_name'] = 'ghost of the uchiha'

l = ['pet', 'age', 'skills']
d1 = dict.fromkeys(l)

k = d1.pop('skills')
l = d1.popitem()
print(d1)

d.update(d1)
print(d, k, l)

d['pet'] = 'kurama'
d['skills'] = 'susano'
d['eyes'] = ['EMS', 'Rinnegan']

print(d)
del d['pet']
print(d)
print(len(d))

