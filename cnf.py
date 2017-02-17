import logicparse as lp
from neg import neg, invert

def elim(formula):
    # combined elimination of <-> and ->
    iffIndices = findall(formula, '<->')
    if iffIndices != []: #eliminate top level iffs
        lastIffIndex = iffIndices[-1]
        termA = elim(formula[:lastIffIndex])     # start of list to <->
        termB = elim(formula[lastIffIndex + 1:]) # <-> to end of list.
        #formula = [[termA, '->', termB], '^', [termB, '->', termA]]
        formula = [['!',termA, 'v', termB], '^',['!',termB, 'v', termA]]
    else: # eliminate implications
        impIndices = findall(formula, '->')
        if impIndices != []:
            lastImpIndex = impIndices[-1]
            termA = elim(formula[:lastImpIndex])
            termB = elim(formula[lastImpIndex + 1:])
            formula = ['!', termA, 'v', termB]
    return formula

# def collapse_not(expr_list):
#     """
#     Takes a nested expression tree thing, checks for uncollapsed nots
#     """
#     for each in expr_list:


# def demorgan(formula): return neg([invert(symbol) if symbol in ('^', 'v') else neg(symbol) for symbol in formula])
def demorgan(formula):
    output = neg(formula)

    if output[0] == '!':
        demorgan_op(output[1])
    else:
        demorgan_op(output)

    return output

# demorgan operation: negates literals and bracketed expressions,
# inverts conjunctions and disjunctions
def demorgan_op(formula):
    for symbol in enumerate(formula):
        if symbol[1] in ('^', 'v'):
            formula[symbol[0]] = invert(symbol[1])
        # probably shouldn't ever happen?
        elif symbol[1] == '!':
            del formula[symbol[0]]
        else:
            formula[symbol[0]] = neg(symbol[1])

# applies demorgan's theorem recursively to resolve negated bracketed
# expressions
def demorgan_r(formula):
    output = demorgan(formula)

    for clause in enumerate(output):
        if type(clause[1]) == list:
            output[clause[0]] = demorgan_r(clause[1])
            print("did step two!")

    return output


def findall(seq, elem):
    """
    find indices of all occurences of elem at top level of list.
    """
    return [i for i in range(0, len(seq)) if seq[i] == elem]
