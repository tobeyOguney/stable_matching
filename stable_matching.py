#A pythonic implementation of the Gale-Shapley algorithm
def generate_stable_matching(group1, group2):
    match_1 = dict()
    match_2 = dict()
    single1 = list(group1.keys())
    while single1:
        for choice in group1[single1[0]]:
            if choice not in list(match_2.keys()):
                match_1[single1[0]] = choice
                match_2[choice] = single1[0]
                break
            else:
                if group2[choice].index(single1[0]) < group2[choice].index(match_2[choice]):
                    del match_1[match_2[choice]]
                    single1.append(match_2[choice])
                    match_1[single1[0]] = choice
                    match_2[choice] = single1[0]
                    break
        single1 = single1[1:]
    return match_1.items()

if __name__ == '__main__':
    print(
        generate_stable_matching(
            {
                'Simi': ['Wizkid', 'Adekunle Gold'],
                'Tiwa Savage': ['Wizkid', 'Adekunle Gold']
            },
            {
                'Wizkid': ['Simi', 'Tiwa Savage'],
                'Adekunle Gold': ['Simi', 'Tiwa Savage']
            },
        )
    )
