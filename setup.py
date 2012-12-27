from setuptools import setup

setup(
    name = "oraclesql-pygments-lexer",
    version = "0.1",
    packages = ['oraclesql',],
    install_requires = ['Pygments'],
    author = "Felipe Zorzo",
    author_email = "felipe.b.zorzo@gmail.com",
    description = "Pygments lexer for Oracle PL/SQL and Oracle Forms",
	
	entry_points={
          'pygments.lexers': ['forms = oraclesql.lexer:OracleFormsLexer', ]
    },
)