"""
Additional Pylint checkers for string constant spaces formatting operations.
"""
import tokenize

from pylint.checkers import BaseTokenChecker
from pylint.interfaces import ITokenChecker


class StringConstantSpacesChecker(BaseTokenChecker):
    """
    Look for string concatenation operations, spaces is a bad practice!
    """

    __implements__ = ITokenChecker

    name = 'string_concatenation_spaces'
    msgs = {'E8404': ('Prefer string concatenation to string substitution %s',
                      'string-concat-spaces',
                      'Used when a string concatenation no operation is found! Sometimes you just missing it.')}

    def process_tokens(self, tokens):
        for index, (tok_type, _, (start_row, start), _, line_str) in enumerate(tokens):
            if tok_type == tokenize.STRING and index > 1:
                last_tok_type, _, _, (_, last_end), last_line_str = tokens[index - 1]
                if last_tok_type == tokenize.STRING:    # if last tok_type is string
                    line = ''
                    # if is same line or break line with \
                    if line_str == last_line_str:
                        line = line_str
                    elif last_line_str.find('\\\n'):
                        line = last_line_str.replace('\\\n', '') + line_str

                    string_between = line[last_end: start]
                    if string_between.replace(' ', '') == '':
                        self.add_message('string-concat-spaces',
                                         line=start_row, args=(line, ))


def register(linter):
    """
    register
    """
    linter.register_checker(StringConstantSpacesChecker(linter))
