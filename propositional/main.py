from argparse import ArgumentParser

import operators
import syntax
import session
import satisfier

parser = ArgumentParser()
parser.add_argument("mode", help="eval, satisfy")

SENTINEL = "("
TERMINAL = ")"
SEPARATOR = " "
TRUE = "true"
FALSE = "false"
VOCAB = [TRUE, FALSE]

ops = operators.operators(true=TRUE, false=FALSE)
syn = syntax.syntax(vocab=VOCAB,
                    sentinel=SENTINEL,
                    terminal=TERMINAL,
                    separator=SEPARATOR)

sat = satisfier.satisfier(ops, syn)
ses = session.session(ops, syn)

if __name__ == "__main__":
    args = parser.parse_args()

    match args.mode:
        case "eval":
            ses.driver_loop()
        case "satisfy":
            sat.driver_loop()
