from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings

from helpers.chuck_norris import CHUCKNORRIS


class ChuckNorrisPlugin(WillPlugin):

    def __init__(self, *args, **kwargs):
        self.cn = CHUCKNORRIS()
        return WillPlugin.__init__(self, *args, **kwargs)

    @respond_to("^chuck norris me$")
    def chuck_norris_me(self, message):
        """
        chuck norris me: Get the a joke about Chuck Norris (there is no gaurentee it will be good).
        """
        self.reply(message, self.cn.get_chuck_norris_joke())

    @respond_to("^joke me f=(?P<first_name>.*)$ l=(?P<last_name>.*)$")
    def joke_me(self, message, first_name, last_name):
        """
        joke me f=__ l=__: Get the a joke about a person (f = first name, l= last name). There is no gaurentee it will be good.
        """
        if not first_name or not last_name:
            self.reply(message, 'I need both a first and last name to provide a joke about a person!')
        else:
            self.reply(message, self.cn.get_joke_with_name(first_name, last_name))