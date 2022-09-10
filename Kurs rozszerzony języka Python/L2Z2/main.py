from Formula import*

var = [('p', True), ('q', False), ('r', False)]

formula1 = Neg(Var('p'))
print(str(formula1))
print('Boolean value of: ' + str(formula1) + ' is: ' + str(formula1.evaluate(var)))

print('----------------')

formula2 = Con(Imp(Var('p'), Var('q')), Var('r'))
print(str(formula2))
print('Boolean value of: ' + str(formula2) + ' is: ' + str(formula2.evaluate(var)))

print('----------------')

formula3 = Bic(Dis(Var('q'), Var('r')), Con(Var('p'), Var('r')))
print(str(formula3))
print('Boolean value of: ' + str(formula3) + ' is: ' + str(formula3.evaluate(var)))

print('----------------')


def variables(formula):
    outcome = []
    if type(formula) == Var:
        outcome.append(formula.name)
        return outcome
    elif type(formula) == TConst or type(formula) == FConst:
        return []
    elif type(formula) == Neg:
        return variables(formula.content)
    elif (type(formula) == Con or type(formula) == Dis or
            type(formula) == Imp or type(formula) == Bic):
        return variables(formula.left) + variables(formula.right)


def tautology(formula):
    vars_list = list(dict.fromkeys(variables(formula)))
    length = len(vars_list)
    env_list = []

    def generate(prefix, k):

        if k == 0:
            env_list.append(prefix)
            return

        for i in range(2):
            new_prefix = prefix + ['0', '1'][i]

            generate(new_prefix, k - 1)

    generate("", length)
    for i in range(2**length):
        env = []
        for j in range(len(vars_list)):
            env.append([vars_list[j], int(env_list[i][j])])
        if not formula.evaluate(env):
            return False
    return True


print('Is formula ' + str(formula3) + ' tautology? ' + str(tautology(formula3)))
print('---')
print('Is formula ' + str(formula2) + ' tautology? ' + str(tautology(formula2)))
print('---')
print('Is formula ' + str(formula1) + ' tautology? ' + str(tautology(formula1)))
print('---')

formula4 = TConst()
formula5 = Bic(Neg(Con(Var('a'), Var('b'))), Dis(Neg(Var('a')), Neg(Var('b'))))

print('Is formula ' + str(formula4) + ' tautology? ' + str(tautology(formula4)))
print('---')
print('Is formula ' + str(formula5) + ' tautology? ' + str(tautology(formula5)))
print('---')
