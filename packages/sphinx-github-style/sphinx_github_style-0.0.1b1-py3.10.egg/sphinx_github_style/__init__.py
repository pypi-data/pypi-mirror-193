__version__ = "0.0.1b1"
__author__ = 'Adam Korn <hello@dailykitten.net>'

from sphinx.application import Sphinx


def setup(app: Sphinx):
    # imports defined inside setup function, so that the __version__ can be loaded,
    # even if Sphinx is not yet installed.
    from sphinx.writers.text import STDINDENT

    from .github_style import TDKStyle
    from .meth_lexer import TDKMethLexer
    from .add_linkcode_class import add_linkcode_node_class

    app.require_sphinx('1.4')
    app.add_lexer('tdk', TDKMethLexer)
    app.add_css_file('_static/github_linkcode.css')
    app.connect('doctree-resolved', add_linkcode_node_class)

    app.add_config_value('rst_file_suffix', ".rst", False)
    """This is the file name suffix for reST files"""
    app.add_config_value('rst_link_suffix', None, False)
    """The is the suffix used in internal links. By default, takes the same value as rst_file_suffix"""
    app.add_config_value('rst_file_transform', None, False)
    """Function to translate a docname to a filename. By default, returns docname + rst_file_suffix."""
    app.add_config_value('rst_link_transform', None, False)
    """Function to translate a docname to a (partial) URI. By default, returns docname + rst_link_suffix."""
    app.add_config_value('rst_indent', STDINDENT, False)

    return {
        'version': __version__,
        # 'env_version': 1,  # not needed; restbuilder does not store data in the environment
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
