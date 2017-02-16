# conjunctive
* __converts logical expressions to CNF__
* __performs proofs-by-refutation__
* __solves the three-colour problem__

## main module

## question modules
Question modules answering questions 1-3.

### pbr
__pbr.py : performs proof-by-refutation using the DPLL algorithm__

uses modules deepcopy (standard library) and neg (provided)
contains functions `pbr()`, `dpll()`, `unit_prop()`, `pure_lit()`, `clear()`, `units()`, `consistent_lits()`

#### `pbr()`
Takes logical expression in cnf clause form and creates a list of available literals that will be used in the dpll algorithm, then calls the dpll algorithm

#### `dpll()`
Implements the DPLL algorithm. Returns true if SAT.

Takes logical expression in cnf clause form and a list of all literals currently in the clause. Copies both so they can be destroyed without issue.

Exits if no literals remain or the list of clauses is a consistent set of pure literals. The list is thus satisfiable.

Exits if any clause is empty or list is inconsistent. The list is thus unsatisfiable

Applies the unit propagation and pure literal algorithms to approach a solution.

Takes the first available literal in the set, and its negation. Appends each respectively to a copy of the set of clauses and recurses on each. If no literals are available, recurses one more time to find a solution (set will either be empty or contain an empty clause.

#### `unit_prop()`
Unit propagation algorithm. Given a unit clause, deletes all clauses that contain it and deletes all literals equal to its negative in the expression. No return.

#### `pure_lit()`
Pure literal algorithm. Deletes all unit clauses whose negatives are not present. No return.

#### `clear()`
Removes an element from a list, or all of an element from a list. Was used only once or twice.

#### `units()`
Returns a list of all unit clauses in a clause form logical expression

#### `consistent_lits()`
Checks whether the expression is a consistent set of literals
If not a set of literals (unit clauses), returns false.
If a consistent set of literals, returns true (satisfiable)
If inconsistent set of literals, returns none (unsatisfiable)

## helper modules
Helper modules were created to assist in the question modules' execution.

### logicparse
__logicparse.py : parses logical expressions so they can be used by other modules__

uses module re (standard library)
contains functions `parse()`, `nestgen()`, `find_and_group()`

#### `parse()`
Returns a list of all values in given logical expression matching regular expression `splitter`. `slitter` effectively matches brackets, all literals, and all operators, disregarding spaces.

#### `nestgen()`
Destructively interprets a list generated by parse. Turns bracketed expressions into nested lists, destroying brackets. Optionally also nests operations hierarchically by precedence: `!, ^, v, ->, <->`

#### `find_and_group()`
Commonly used in nestgen, finds an operator taking n terms, takes it, the term following it, and the term preceding it if it takes 2 arguments, and puts them into a list. Nests the list in the position where the first item used to be, deletes the operator and arguments from the original list.

### neg
__neg.py : negation module__

neg contains two functions; `neg()` and `invert()`. 

#### `neg()`
Takes a string representing a literal or a list representing a complex logical expression.
neg returns the negation of a literal or bracketed expression. Maps `'C' -> '!C'` and vice versa, `['A', '^', 'B'] -> ['!', ['A', '^', 'B']]` and vice versa.

#### `invert()`
Takes a string representing an and `^` or an or `v` logical operator.
Returns the inverse; `^` yields `v`, vice-versa. Useful in applying DeMorgan.
