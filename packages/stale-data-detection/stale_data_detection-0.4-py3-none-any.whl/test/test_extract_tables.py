import sys
sys.path.append('../stale_data_detection/')
from extract_table_names import get_table_names, get_raw_urls
import argparse

def main():
    parser = argparse.ArgumentParser(description='Testing extract table names from URL')
    parser.add_argument('-u', '--url', help='URL to the GitHub repo')
    parser.add_argument('-b', '--branch', help='name of the GitHub branch')
    parser.add_argument('-a', '--access_token', help='Access token to authenticate')
    parser.add_argument('-e', '--ext', help='file extension to search for')

    args = parser.parse_args()

    access_token = None
    file_ext = '.hql'

    if args.access_token:
        access_token = args.access_token
    if args.ext:
        file_ext = args.ext
    
    if args.url and args.branch:
        repo_url = args.url
        branch_name = args.branch

        raw_urls = get_raw_urls(repo_url, branch_name, access_token, file_ext)
        for url in raw_urls:
            print(url)
        print('\n')
        tables = get_table_names(repo_url, branch_name, access_token, file_ext)
        for table in tables:
            print(table)

    else:
        print("Invalid arguments")
        
if __name__ == "__main__":
    main()