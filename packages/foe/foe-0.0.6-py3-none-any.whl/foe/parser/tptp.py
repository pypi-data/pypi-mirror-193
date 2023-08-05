from lark import Lark
from importlib.resources import files

# read the grammar from the tptp_grammar.txt file
tptp_grammar = files('foe.parser').joinpath('tptp_grammar.txt').read_text()
tptp_parser = Lark(tptp_grammar, start='tptp_file')

"""
def parse_tptp_file(input: Tree) -> dict:
    result = {
        "include": [],
        "formula": []
    }
    _parse_tptp_file(input, result)
    return result


def _parse_tptp_file(input: Tree, result: dict):
    for i in input.children:
        match i.children[0].data.value:
            case "include":
                result["include"].append(i.children[0].children[0].value)
            case "annotated_formula":
                result["formula"].append(i.children[0].children[0])


def _parse_annotated_formula(input: Tree) -> Formula:
    match input.data.value:
        case "fof_annotated":
            return _parse_fof_annotated(input)
        case _:
            raise ValueError(f"Only 'fof_annotated' allowed, input contains {input.data.value}")


def _parse_fof_annotated(input: Tree) -> Formula:
    name = input.children[0].value
    role = input.children[1].value
    return _parse_fof_formula(input.children[2])


def _parse_fof_formula(input: lark.tree.Tree) -> Formula:
    match input.data.value:
        case "fof_logic_formula":
            return _parse_fof_logic_formula(input)
        case "fof_sequent":
            return _parse_fof_sequent(input)
        case _:
            raise ValueError(f"Only 'fof_logic_formula' and 'fof_sequent' allowed, input contains {input.data.value}")


def _parse_fof_logic_formula(input: Tree) -> Formula:
    match input.data.value:
        case "fof_binary_formula":
            return _parse_fof_binary_formula(input)
        case "fof_unitary_formula":
            return _parse_fof_unitary_formula(input)
        case "fof_quantified_formula":
            return _parse_fof_quantified_formula(input)
        case "fof_conditional":
            return _parse_fof_conditional(input)
        case "fof_let":
            return _parse_fof_let(input)
        case _:
            raise ValueError(f"Only 'fof_binary_formula', 'fof_unitary_formula', 'fof_quantified_formula', 'fof_conditional' and 'fof_let' allowed, input contains {input.data.value}")
"""
