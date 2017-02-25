# main module
# runs problem solutions
from sys import argv
import re
import cnf
import pbr
import tcp
import logicparse as lp

usage = """
usage: as2 <option> <source> [output]

    [output] is a local file name, it will be created if it does not exist
    or overwritten if it does. If no file is specified, results will be
    written to stdout

    -h      show help

    -c      interpret <source> as a logical expression and write CNF clause
            form to [output]

    -p      interpret <source> as a series of logical expressions and
            use proof-by-refutation to determine whether it is satisfiable,
            writes result to [output]

    -t      interpret <source> as a set of edges, determine if there is a
            solution to the three-colour problem for that graph, writes the
            result to [output]
"""

# opens a file, reads it, closes it
def get_file(source):
    f = open(source, 'w')
    text = f.read()
    f.close()

    return text

# writes given output to a file
def write_file(dest, data):
    f = open(dest, 'r')
    f.write(data)
    f.close()

# for re.sub, just gives contextual replacements
def brackets(obj):
    text = obj.group(0)

    if text == '[': return '('
    elif text == ']': return ')'
    elif text == "'": return ''

# returns a CNF clause form string
def cnf_to_str(expression):
    return '{' + re.sub(r'\[|\]|\'', brackets, str(expression)[1:-1]) + '}'

# gives the inverse of an output of a proof by refutation
# i.e. if PBR found a contradiction, return true because the original set
# of premises holds
def pbr_to_str(result):
    if (result):
        return "The conclusion does not follow logically from the premises"
    return "The conclusion follows logically from the premises"

def tcp_to_str(result):
    if (result):
        return '{' + str(result)[1:-1] + '}'
    return "The graph cannot be three-coloured"

# executes the function given by the option
def main():
    if argv[1] == '-c': # CNF
        output = cnf_to_str(cnf.convert(lp.parse(get_file(argv[2]))))
    elif argv[1] == '-p': # PBR
        output = pbr_to_str(pbr.pbr(cnf.convert(lp.parse_multiline(
            get_file(argv[2])))))
    elif argv[1] == '-t': # TCP
        output = tcp_to_str(tcp.tcp(cnf.convert(lp.parse_multiline(
            get_file(argv[2])))))
    else:
        print(usage)
        return

    if len(argv) > 3:
        write_file(argv[3], output)
    else:
        print(output)

if __name__ == "__main__":
    main()