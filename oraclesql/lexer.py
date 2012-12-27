from pygments.lexers.sql import SqlLexer
from pygments.token import Keyword, Name

from _forms_builtins import FORMS_BUILTINS

__all__ = ['OracleFormsLexer']

# TODO: Use a custom lexer for SQL
class OracleFormsLexer(SqlLexer):
    name = 'Oracle Forms'
    aliases = ['forms']
    mimetypes = ['text/x-oracle-forms']
    
    def get_tokens_unprocessed(self, text):
        extra_content = [(FORMS_BUILTINS, Name.Builtin)]
		
        for index, token, value in SqlLexer.get_tokens_unprocessed(self, text):
            if token is Name:
                for i in extra_content:
                    if value in i[0]:
                        yield index, i[1], value
                        break;
                else:
                    yield index, token, value
            else:
                yield index, token, value