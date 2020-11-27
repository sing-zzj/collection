# Scrapy settings for mySpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'mySpider'

SPIDER_MODULES = ['mySpider.spiders']
NEWSPIDER_MODULE = 'mySpider.spiders'

LOG_LEVEL = 'WARNING'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  # 'cookie': 'adProvider=AdManager; __gads=ID=4c110fe7126fc0e1:T=1597137553:S=ALNI_MZ-S351h5bf2wKdmG7zZ9nXa7Ak2w; __utmz=148946146.1600656998.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); cookieAccept=ok; locale=zh; __utmc=148946146; __utma=148946146.1462448825.1600656992.1601196407.1601254065.27; __utmc=148946146; __utmz=148946146.1600656998.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ld=%7B%22d%22%3A%5B%22en%3Alo%22%2C%22en%3Azh%22%2C%22zh%3Aen%22%2C%22en%3Amy%22%2C%22en%3Alzh%22%2C%22lo%3Aen%22%2C%22zh%3Avi%22%5D%7D; GLID=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJwIjpudWxsLCJ1c2VyX25hbWUiOiJvbGl2ZXIiLCJzY29wZSI6W10sImlkIjo2NzE0MzU4MjQ3NzM1NjkxNjM3LCJleHAiOjE2MzI4MDAyMTAsImlhdCI6MTYwMTI2NDIxMCwiYXV0aG9yaXRpZXMiOlsiUk9MRV9VU0VSIiwiVVNFUiJdLCJqdGkiOiI5MmViOWVjMS02NmJhLTRjYWQtYmExMi00ZDhiNDgxZGFlNTkiLCJjbGllbnRfaWQiOiJnbG9zYmUifQ.NBSDTFMz28dWsMKiK5Ziq-l8noIFk6CbwsTu-2jW7z03eMiTiTGk3ePKFcHqzdjxliRl49Jb2hNuYL31RRgS6ssMPy0KLMVIhoFgOXMqHqz7lChGiIlJmH3y1H_DsS5zrEn4oIq15OQXzngLbaB3Acm-6It5JoujSS9lxczHiHNcJvr8v86Pg1tfEseOh8MnfRDnnovpNGEIMjiKE1u6r0Ilt1Eysrq4yQtgWTlTBw1YyqbqcvCHT1mSRude8fIJP_B6YzmEFSvG3e9QeTNiQruENZ_KiNrX8T96Fom_sETR3_nHuvJBMIrjfajLqvnJ2Cgmq8BVceBdTVh9LPSuaA; adProvider=AdManager; __utma=148946146.1462448825.1600656992.1601196407.1601254065.27; __utmt=1; glosbeScreen=1119x625; __utmb=148946146.15.10.1601272558',
  'cookie': '__gads=ID=4c110fe7126fc0e1:T=1597137553:S=ALNI_MZ-S351h5bf2wKdmG7zZ9nXa7Ak2w; cookieAccept=ok; locale=zh; GLID=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJwIjpudWxsLCJ1c2VyX25hbWUiOiJvbGl2ZXIiLCJzY29wZSI6W10sImlkIjo2NzE0MzU4MjQ3NzM1NjkxNjM3LCJleHAiOjE2MzM4MzE4MDIsImlhdCI6MTYwMjI5NTgwMiwiYXV0aG9yaXRpZXMiOlsiUk9MRV9VU0VSIiwiVVNFUiJdLCJqdGkiOiIyNzllMGE3Ny1iMmI2LTQ1ZDItYTQ3MS02MDEyNDIwYzAxMzMiLCJjbGllbnRfaWQiOiJnbG9zYmUifQ.jqNwPiTEzA-tcx-frXWvBZ8EkUM8koyp82tBa9y1X2MZ6vmJVWKkinThDRve4LYvRlxUQRV_g-Dnna-i7RUs7SusR7bnRWI0r_OdxA84lD2LjXQrlxaWPX8v0oNtrSOXuYg6smkihZaQaPyvGXn_-TC7F6eUcJBeTAbCticNLAkwiSjeukyKB87J9r_0MfrUizMlc5qOJrScU57zy3DEKHY8IkMfEdpvNNlBhesUu_XtW9cKIGnvk_T4huBBZIifIysJR9DMlNLy-PgNCOddFWOgspdDxNr5GD4j_b9TG_A94pSlMmT0KXLlhsw8H-LP_VsGHsyL4NVihq8Dn2IinA; adProvider=AdManager; __utmc=148946146; __utmz=148946146.1606283224.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ld=%7B%22d%22%3A%5B%22en%3Ata%22%2C%22en%3Ath%22%2C%22en%3Auz%22%2C%22en%3Aur%22%5D%7D; glosbeScreen=449x625; __utma=148946146.1145824164.1606283215.1606370344.1606374135.7; __utmt=1; __utmb=148946146.1.10.1606374135'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'mySpider.middlewares.MyspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'mySpider.middlewares.MyspiderDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'mySpider.pipelines.MyspiderPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
