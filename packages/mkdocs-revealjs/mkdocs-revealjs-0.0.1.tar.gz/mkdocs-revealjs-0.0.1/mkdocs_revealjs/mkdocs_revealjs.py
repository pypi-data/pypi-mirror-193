#  License: GNU GPLv3+, Rodrigo Schwencke (Copyleft) 

# import os
# import re
# import markdown
# import subprocess
# import base64
# import shlex
# from random import randint
# from .htmlColors import HTML_COLORS

from markdown.preprocessors import Preprocessor
import yaml

class MkdocsRevealjsExtension(markdown.Extension):

    def __init__(self, **kwargs):
        self.config = {
            'vartable' :        [DEFAULT_VARTABLE_DICT, 'Default Vartable Dict'],
            'priority' :        [DEFAULT_PRIORITY, 'Default Priority for this Extension']
        }
        super(MkdocsRevealjsExtension, self).__init__(**kwargs)

    def extendMarkdown(self, md):
        """ Add MkdocsRevealjsPreprocessor to the Markdown instance. """
        md.registerExtension(self)
        md.preprocessors.register(MkdocsRevealjsPreprocessor(md, self.config), 'revealjs_block', int(self.config['priority'][0]))

class MkdocsRevealjsPreprocessor(Preprocessor):
    def __init__(self, config):
        self.config = config

    def run(self, lines):
        # Get the metadata for the current page
        current_page = self.config['current_page']
        page_metadata = None
        for page in self.config['pages']:
            if page['file'] == current_page:
                page_metadata = page
                break

        # Add the metadata as YAML frontmatter
        if page_metadata:
            metadata_lines = yaml.dump(page_metadata, default_flow_style=False).split('\n')
            lines = metadata_lines + [''] + lines

        return lines

def makeExtension(*args, **kwargs):
    return MkdocsRevealjsExtension(*args, **kwargs)
