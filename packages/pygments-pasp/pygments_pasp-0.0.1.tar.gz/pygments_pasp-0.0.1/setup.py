from setuptools import setup

setup (
  packages=['pygments_pasp'],
  entry_points =
  """
  [pygments.lexers]
  pasplexer = pygments_pasp.pasp:PaspLexer
  """,
)
