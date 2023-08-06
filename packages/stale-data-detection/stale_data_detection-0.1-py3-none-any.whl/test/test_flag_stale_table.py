import sys
sys.path.append('../stale_data_detection/')

import json
from flag_stale_table import is_stale_table
from extract_table_names import get_table_names
import argparse

def main():
    parser = argparse.ArgumentParser(description='Testing extract table names from URL')
    parser.add_argument('-u', '--url', help='URL to the GitHub repo')
    parser.add_argument('-b', '--branch', help='name of the GitHub branch')
    parser.add_argument('-a', '--access_token', help='Access token to authenticate')
    parser.add_argument('-e', '--ext', help='file extension to search for')
    parser.add_argument('-o', '--output', help='path to output file')

    args = parser.parse_args()

    access_token = None
    file_ext = '.hql'
    output_file = 'stale_list.json'

    if args.access_token:
        access_token = args.access_token
    if args.ext:
        file_ext = args.ext
    if args.output:
        output_file = args.output

    if args.url and args.branch:
        repo_url = args.url
        branch_name = args.branch

        tables = get_table_names(repo_url, branch_name, access_token, file_ext)
        
        staleness = {}
        for table_name in tables:
            table_name = table_name.strip()
            print(f'Processing Table {table_name}')
            staleness[table_name] = is_stale_table(table_name)

        with open(output_file, 'w') as output:
            json.dump(staleness, output, indent=4)

    else:
        print("Invalid arguments")


if __name__ == "__main__":
    main()