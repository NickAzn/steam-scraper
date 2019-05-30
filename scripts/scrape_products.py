import subprocess
import sys


def scrape_products(id_file, output_file, throttle):
    id_file_arg = 'id_file=' + id_file
    autothrottle = 'AUTOTHROTTLE_ENABLED=' + throttle
    subprocess.call(['scrapy', 'crawl', 'products',
                     '-a', id_file_arg, '-o', output_file,
                     '-s', 'HTTPCACHE_ENABLED=False',
                     '-s', autothrottle])


scrape_products(sys.argv[1], sys.argv[2], sys.argv[3])
