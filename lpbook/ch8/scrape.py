# learning-python/NEW/ch8/scrape.py
# See w_pacb45.pdf, page 250

import argparse

print("DEBUG: learning-python/NEW/ch8/scrape.py")

if __name__ == '__main__':
    print("DEBUG: Inside __main__")
    parser = argparse.ArgumentParser(
        description='Scrape a webpage.')
    parser.add_argument(
        '--t',
        '--type',
        choices=['all', 'png', 'jpg'],
        default='all',
        help='The iamge type you want to scrape.'
    )
    parser.add_argument(
        '-f',
        '--format',
        choices=['img', 'json'],
        default='img',
        help='The format images are saved to.'
    )
    parser.add_argument(
        'url',
        help='The URL we want to scape for images.'
    )
    args = parser.parse_args()
    # TODO scrape(args.url, args.format, args.type)

# EOF
