#!/usr/bin/python


## ------------ Imports ----------- ##
## ------------ Imports ----------- ##


class FormatSynthesiser(object):
    """."""
    def __init__(self):
        """."""
        pass

    def uniform_content(self, content):
        """."""
        # Expecting the content type as file object.
        _content = content.body.readlines()

        # and convert the content into a plain text.
        return "".join(_content)

    def page_offsets(self, content):
        """."""
        return """<pre>{0}{1}{2}</pre>""".format("<br>", content, "<br>"*10)

    def character_spacers(self, content):
        """."""
        return content.replace(' ', '&nbsp;')


class JsonFormatizer(FormatSynthesiser):
    """."""
    pass


class SnippetFormatizer(FormatSynthesiser):
    """."""
    def __init__(self, content):
        """."""
        self.content = self.uniform_content(content)

    def colourise(self):
        """."""
        pass

    def synthesis(self, spacers=True, page_offsets=True, color=False):
        """."""
        if spacers:
            self.content = self.character_spacers(self.content)
        if page_offsets:
            self.content = self.page_offsets(self.content)

        return self.content
