#!/usr/bin/env python3

from siprawn import simap

def main():
    import argparse

    parser = argparse.ArgumentParser(
        description='Generate map and template wiki for image')
    parser.add_argument('--user',
                        required=True,
                        help='User name (ie wiki user name)')
    parser.add_argument('--copyright',
                        default=None,
                        help='Copyright release base')
    parser.add_argument('files', nargs="+", help='Images to map')
    args = parser.parse_args()
    simap.map_user(user=args.user,
        copyright_=args.copyright,
        files=args.files,
        run_img2doku=True)


if __name__ == "__main__":
    main()
