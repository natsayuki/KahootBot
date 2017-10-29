from setuptools import setup
setup(
  name = 'KahootBot',
  packages = ['KahootBot\.py'], # this must be the same as the name above
  version = '29.10.17',
  description = 'A bot to play kahoot for you',
  author = 'the42ndturtle',
  author_email = 'throwawayemail@gmail.com',
  url = 'https://github.com/the42ndturtle/KahootBot', # use the URL to the github repo
  download_url = 'https://github.com/the42ndturtle/KahootBot/archive/0.2.tar.gz', # I'll explain this in a second
  keywords = ['kahoot', 'bot', 'win'], # arbitrary keywords
  classifiers = [],
  install_requires=['PIL'],
)
