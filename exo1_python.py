from itertools import product

def tableDeVerite(e):
    vars = sorted(set(j for j in e if j.isalpha()))
    negated_vars = ['¬' + var for var in vars]
    all_vars = vars + negated_vars
    table = []    
    for combination in product([0, 1], repeat=len(vars)):
        non_negated_values = dict(zip(vars, combination))
        negated_values = {var: 1 - non_negated_values[var] for var in vars}
        i = {**non_negated_values, **negated_values}
        i['Result'] = eval(e, i)
        table.append(i)    
    return table

def algebreDeBool(v):
    return '1' if v else '0'

def formCanoniques1_2(e):
    vars = sorted(set(j for j in e if j.isalpha()))
    mins = []  
    maxs = []
    for i in tableDeVerite(e):
        if i['Result']:
            min = ''.join([algebreDeBool(i[var]) for var in vars])
            mins.append(min)
        else:
            max = ''.join([algebreDeBool(1 - i[var]) if i[var] != None else '-' for var in vars])
            maxs.append(max)    
    mins = [''.join([vars[i] if min[i] == '1' else f'¬{vars[i]}' for i in range(len(vars))]) for min in mins]
    maxs = [''.join([vars[i] if max[i] == '0' else f'¬{vars[i]}' for i in range(len(vars))]) for max in maxs]    
    return mins, maxs

def main():
    e = input("f(X) : ")
    all_vars = sorted({j for j in e if j.isalpha() or j == '~'})
    negated_vars = ['¬' + var for var in all_vars if '¬' + var in e]
    header = ' | '.join(all_vars + negated_vars + [e])
    print(header)
    print('-' * len(header))
    for i in tableDeVerite(e):
        vals = []
        for var in all_vars:
            if var == '~':
                vals.append('')
            else:
                vals.append(algebreDeBool(i[var]))
        if negated_vars:
            for var in negated_vars:
                non_negated_var = var[1:]
                vals.append(algebreDeBool(1 - i[non_negated_var]))
        vals.append(algebreDeBool(i['Result']))
        print(' | '.join(vals))
    mins, maxs = formCanoniques1_2(e)
    print("Deuxième forme canonique :", ' * '.join(maxs))
    print("Première forme canonique :", ' + '.join(mins))

if __name__ == "__main__":
    main()
