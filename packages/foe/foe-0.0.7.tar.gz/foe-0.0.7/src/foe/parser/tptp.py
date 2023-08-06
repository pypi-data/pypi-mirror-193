from lark import Lark, Token, Tree
from importlib.resources import files
from ..logic import Equation, Function, Sequent, Term, Variable


tptp_grammar = files('foe.parser').joinpath('tptp_grammar.lark').read_text()
tptp_parser = Lark(tptp_grammar, start='tptp_file')


def parse_tptp_file(input: Tree) -> dict:
    result = {
        "include": [],
        "axiom": [],
        "negated_conjecture": [],
        "functions": set(),
    }
    _parse_tptp_file(input, result)
    return result


def _parse_tptp_file(input: Tree, result: dict):
    for i in input.children:
        match i.children[0].data.value:
            case "include":
                result["include"].append(i.children[0].children[0].value)
            case "annotated_formula":
                _parse_annotated_formula(i.children[0], result)


def _parse_annotated_formula(input: Tree, data: dict):
    match input.children[0].data.value:
        case "fof_annotated":
            return _parse_fof_annotated(input.children[0], data)
        case _:
            raise ValueError(f"Only 'fof_annotated' allowed, \
input contains {input.children[0].data.value}")


def _parse_fof_annotated(input: Tree, data: dict) -> Sequent:
    match input.children[1].value:
        case "axiom" | "hypothesis" | "definition" | \
          "assumption" | "lemma" | "theorem":
            data["axiom"].append(
                Sequent(
                    [],
                    [Equation(
                        _parse_fof_formula(input.children[2], data), "true"
                    )]
                )
            )
        case "negated_conjecture":
            data["negated_conjecture"].append(
                Sequent(
                    [],
                    [Equation(
                        _parse_fof_formula(input.children[2], data), "true"
                    )]
                )
            )
        case "conjecture":
            data["negated_conjecture"].append(
                Sequent(
                    [Equation(
                        _parse_fof_formula(input.children[2], data), "true"
                    )],
                    []
                )
            )


def _parse_fof_formula(input: Tree, data: dict) -> Term:
    match input.children[0].data.value:
        case "fof_logic_formula":
            return _parse_fof_logic_formula(input.children[0], data)
        case _:
            raise ValueError(
                f"Only 'fof_logic_formula'allowed, \
input contains {input.children[0].data.value}")


def _parse_fof_logic_formula(input: Tree, data: dict) -> list[Term]:
    match input.children[0].data.value:
        case "fof_binary_formula":
            return _parse_fof_binary_formula(input.children[0], data)
        case "fof_unitary_formula":
            return _parse_fof_unitary_formula(input.children[0], data)
        case _:
            raise ValueError(f"Only 'fof_binary_formula', \
'fof_unitary_formula' allowed, input contains {input.children[0].data.value}")


def _parse_fof_binary_formula(input: Tree, data: dict) -> list[Term]:
    match input.children[0].data.value:
        case "fof_binary_nonassoc":
            return _parse_fof_binary_nonassoc(input.children[0], data)
        case "fof_binary_assoc":
            return _parse_fof_binary_assoc(input.children[0], data)
        case _:
            raise ValueError(f"Only 'fof_binary_nonassoc' and \
'fof_binary_assoc' allowed, input contains {input.data.value}")


def _parse_fof_binary_nonassoc(input: Tree, data: dict) -> Term:
    left = _parse_fof_unitary_formula(input.children[0], data)
    op = input.children[1].value
    right = _parse_fof_unitary_formula(input.children[2], data)
    match op:
        case "<=>":
            data["functions"].add("iff")
            return Function("iff", [left, right])
        case "=>":
            data["functions"].add("implies")
            return Function("implies", [left, right])
        case "<=":
            data["functions"].add("implies")
            return Function("implies", [right, left])
        case "<~>":
            data["functions"].add("xor")
            return Function("xor", [left, right])
        case "~|":
            data["functions"].add("nor")
            return Function("nor", [left, right])
        case "~&":
            data["functions"].add("nand")
            return Function("nand", [left, right])


def _parse_fof_binary_assoc(input: Tree, data: dict) -> Term:
    match input.children[0].data.value:
        case "fof_or_formula":
            return _parse_fof_or_formula(input.children[0], data)
        case "fof_and_formula":
            return _parse_fof_and_formula(input.children[0], data)
        case _:
            raise ValueError(f"Only 'fof_or_formula' and \
'fof_and_formula' allowed, input contains {input.data.value}")


def _parse_fof_or_formula(input: Tree, data: dict) -> Term:
    match input.children[0].data.value:
        case "fof_unitary_formula":
            left = _parse_fof_unitary_formula(input.children[0], data)
        case "fof_or_formula":
            left = _parse_fof_or_formula(input.children[0], data)
    right = _parse_fof_unitary_formula(input.children[1], data)
    data["functions"].add("or")
    return Function("or", [left, right])


def _parse_fof_and_formula(input: Tree, data: dict) -> Term:
    match input.children[0].data.value:
        case "fof_unitary_formula":
            left = _parse_fof_unitary_formula(input.children[0], data)
        case "fof_and_formula":
            left = _parse_fof_and_formula(input.children[0], data)
    right = _parse_fof_unitary_formula(input.children[1], data)
    data["functions"].add("and")
    return Function("and", [left, right])


def _parse_fof_unitary_formula(input: Tree, data: dict) -> Term:
    match input.children[0].data.value:
        case "fof_quantified_formula":
            return _parse_fof_quantified_formula(input.children[0], data)
        case "fof_unary_formula":
            return _parse_fof_unary_formula(input.children[0], data)
        case "fof_atomic_formula":
            return _parse_fof_atomic_formula(input.children[0], data)
        case "fof_logic_formula":
            return _parse_fof_logic_formula(input.children[0], data)


def _parse_fof_quantified_formula(input: Tree, data: dict) -> Term:
    quantifier = input.children[0].value
    variables = _parse_fof_variable_list(input.children[1], data)
    formula = _parse_fof_unitary_formula(input.children[2], data)
    match quantifier:
        case "!":
            data["functions"].add(f"forall{len(variables)}")
            return Function(f"forall{len(variables)}", variables + [formula])
        case "?":
            data["functions"].add(f"exists{len(variables)}")
            return Function(f"exists{len(variables)}", variables + [formula])


def _parse_fof_variable_list(input: Tree, data: dict) -> list[Term]:
    return [
        _parse_variable(i, data) for i in input.children
    ]


def _parse_variable(input: Tree, data: dict) -> Term:
    return Variable(1)


def _parse_fof_unary_formula(input: Tree, data: dict) -> Term:
    match input.children[0].data.value:
        case "fof_unitary_formula":
            data["functions"].add("not")
            return Function(
                "not",
                [_parse_fof_unitary_formula(input.children[0], data)]
            )
        case "fof_infix_unary":
            return _parse_fof_infix_unary(input.children[0], data)


def _parse_fof_infix_unary(input: Tree, data: dict) -> Term:
    left = _parse_fof_term(input.children[0], data)
    right = _parse_fof_term(input.children[2], data)
    data["functions"].add("neq")
    return Function("neq", [left, right])


def _parse_fof_term(input: Tree, data: dict) -> Term:
    if type(input.children[0]) == Token:
        return Variable(1)
    match input.children[0].data.value:
        case "fof_function_term":
            return _parse_fof_function_term(input.children[0], data)
        case _:
            raise ValueError(f"Only 'fof_function_term' and 'VARIABLE' \
                allowed, input contains {input.children[0].data.value}")


def _parse_fof_function_term(input: Tree, data: dict) -> Term:
    match input.children[0].data.value:
        case "fof_plain_term":
            return _parse_fof_plain_term(input.children[0], data)
        case _:
            raise ValueError(f"Only 'fof_plain_term' \
                allowed, input contains {input.children[0].data.value}")


def _parse_fof_plain_term(input: Tree | Token, data: dict) -> Term:
    match len(input.children):
        case 1:
            data["functions"].add(input.children[0].value)
            return Function(input.children[0].value, [])
        case _:
            data["functions"].add(input.children[0].value)
            return Function(
                input.children[0].value,
                [
                    _parse_fof_term(i, data)
                    for i in input.children[1].children
                ]
            )


def _parse_fof_plain_atomic_formula(input: Tree, data: dict) -> Term:
    return _parse_fof_plain_term(input.children[0], data)


def _parse_fof_atomic_formula(input: Tree, data: dict) -> Term:
    match input.children[0].data.value:
        case "fof_plain_atomic_formula":
            return _parse_fof_plain_atomic_formula(input.children[0], data)
        case "fof_defined_atomic_formula":
            return _parse_fof_defined_atomic_formula(input.children[0], data)
        case _:
            raise ValueError(f"Only 'fof_plain_atomic_formula' \
allowed, input contains {input.children[0].data.value}")


def _parse_fof_defined_atomic_formula(input: Tree, data: dict) -> Term:
    match input.children[0].data.value:
        case "fof_defined_infix_formula":
            return _parse_fof_defined_infix_formula(input.children[0], data)
        case _:
            raise ValueError(f"Only 'fof_defined_infix_formula' \
allowed, input contains {input.children[0].data.value}")


def _parse_fof_defined_infix_formula(input: Tree, data: dict) -> Term:
    left = _parse_fof_term(input.children[0], data)
    right = _parse_fof_term(input.children[2], data)
    data["functions"].add(input.children[1].children[0].value)
    return Function(input.children[1].children[0].value, [left, right])
