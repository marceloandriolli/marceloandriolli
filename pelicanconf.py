AUTHOR = 'Marcelo Andriolli'
SITENAME = 'Marcelo Andriolli'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Theme dir
THEME = '/Users/marcelodossantosandriolli/Projects/pelican-clean-blog'

# Header background color
HEADER_COLOR = 'grey'

# D
DISPLAY_PAGES_ON_MENU = True

SHOW_SOCIAL_ON_INDEX_PAGE_HEADER = True

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/myprofile'),
          ('github', 'https://github.com/myprofile'),
          ('facebook','https://facebook.com/myprofile'),
          ('flickr','https://www.flickr.com/myprofile/'),
          ('envelope','mailto:my@mail.address'))


GITHUB_URL = 'http://github.com/marceloandriolli/'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Custom Home page
# DIRECT_TEMPLATES = (('index', 'blog', 'tags', 'categories', 'archives'))
# PAGINATED_DIRECT_TEMPLATES = (('blog',))
# TEMPLATE_PAGES = {'home.html': 'index.html',}