kata = {
        'Python': 'Guido van Rossum',
        'Ruby': 'Yukihiro Matsumoto',
        'PHP': 'Rasmus Lerdof',
        }

for k, v in kata.items():
    print(k, "was created by", v)
print('\n'.join([k + " was created by " + kata[k] for k in kata]))
