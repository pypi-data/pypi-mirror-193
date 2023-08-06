import re
import requests
from sql_metadata import Parser

def get_raw_urls(repo_url, branch_name , access_token=None, ext='.hql'):
    """
    Args:
        repo_url (str): string url to the GitHub repo
        branch_name (str): specify branch name of the repo (main/master/other?)
        access_token (str, optional): GitHub access token. Defaults to None.
        ext (str): file extension. Defaul: .hql
    Returns:
        raw_urls (list[str]): list of raw url to files in the repo
    """

    api_url, sub_dir = get_repo_api_url(repo_url, branch_name)
    if api_url == '':
        return []

    url_parts = repo_url.strip().split('/')
    owner, repo = url_parts[3], url_parts[4]

    # Define headers for API request in case requiring access token
    headers={"Accept":"application/vnd.github.v3+json"}
    if access_token:
        headers["Authorization"] = f"token {access_token}"

    # send GET request to GitHub API to get the file contents
    response = requests.get(api_url, headers = headers)
    
    # Get JSON response and extract the file content
    if response.ok:
        response_json = response.json()
        raw_urls = []
        for item in response_json['tree']:
            if not item['type']=='blob':
                continue
            if sub_dir not in item['path']:
                continue
            if not item['path'].endswith(ext):
                continue
            raw_urls.append(f"https://{url_parts[2]}/raw/{owner}/{repo}/{branch_name}/{item['path']}")
        return raw_urls
    else:
        print('Failed to fetch the files list. Please check the repo url or include access token')


def get_repo_api_url(repo_url, branch_name):
     """
    Args:
        repo_url (str): string url to the GitHub repo
        branch_name (str): specify branch name of the repo (main/master/other?)

    Returns:
        api_url (str): api url for that repo/branch to send HTTPS request
        sub_dir (str): path to subdirectory if it's a subdirectory of a repo/branch
    """
    # check if the given URL is valid
    url_parts = repo_url.strip().split('/')
    if len(url_parts) < 5:
        print("Not a valid repo URL. Please check the URL")
        return ['','']

    # construct the Github API url for the repo
    owner, repo = url_parts[3], url_parts[4]
    api_url = f'https://{url_parts[2]}/api/v3/repos/{owner}/{repo}/git/trees/{branch_name}?recursive=1'
    
    # construct the path to the subdirectory if included in the url
    sub_dir = ''
    branch_tokens = branch_name.split('/')
    for i in reversed(range(len(url_parts))):
        if url_parts[i]== branch_tokens[-1]:
            sub_dir = '/'.join(url_parts[i+1:])
    
    return api_url, sub_dir

def get_table_names(repo_url, branch_name, access_token=None, ext='.hql'):
    """
    Args:
        repo_url (str): string url to the GitHub repo
        branch_name (str): specify branch name of the repo (main/master/other?)
        access_token (str, optional): GitHub access token. Defaults to None.
        ext (str): file extension. Default: .hql

    Returns:
        table_names (set(str)): set of table names from the given repo
    """

    # get raw urls of all files with given extension on that repo
    raw_urls = get_raw_urls(repo_url, branch_name, access_token, ext)
    table_names = set()

    # loop through each url, read content and extract table names
    for url in raw_urls:
        # get file content from url
        file_content = get_file_content(url, access_token)
        # extract table names from file content
        tables = extract_table_names(file_content)
        if len(tables) > 0:
            table_names.update(tables)
    
    return table_names


def extract_table_names(file_content):
    """
    Args:
        file_content (str): content of a file

    Returns:
        table_names (set(str)): set of table names given file content
    """
    file_content = file_content.lower()
    
    # seearch for the hive variables
    # replace all hive variables with table real names
    hive_vars = re.findall(r'hivevar:(.+?)=', file_content)
    for var in hive_vars:
        if len(var.strip().split(" "))>1:
            continue
        # find the correspond hive variables real names
        var_name = re.findall(f'hivevar:{var}=(.+?);',file_content)
        if len(var_name) > 0:
            var = var.strip()
            pattern = f"${{hivevar:{var}}}".strip()
            # replace hive variables with real names
            file_content = re.sub(re.escape(pattern), var_name[0].strip(), file_content)

    # clean file content, remove newline character
    file_content = re.sub("\n", " ", file_content)
    
    # split content into tokens
    tokens = file_content.split(" ")
    
    queries = get_queries(tokens)
    table_names = set()

    # extract table names using sql_metadata
    for query in queries:
        parser = Parser(query)
        try:
            tables = parser.tables
            for table in tables:
                parser.columns
                if table.split(".")[0] not in parser._table_aliases and len(table.split(" ")) <2:
                    table_names.add(table)
        except Exception as e:
            table_names = set()
       
    return table_names

def get_file_content(file_raw_url, access_token=None):
    """
    Args:
        file_raw_url (str): GitHub raw url to file

    Returns:
        content: file content in str
    """

    # construct headers for GET request
    headers={"Accept":"application/vnd.github.v3+json"}
    if access_token:
        headers["Authorization"] = f"token {access_token}"

    try:
        # sending GET request to get the file content
        response = requests.get(file_raw_url, headers=headers)
        if response.status_code == 200:
            content = response.content.decode("utf-8")
            return content
    except requests.exceptions.RequestException:
        print("Error fetching file, check the file raw url or include access token")

def get_queries(tokens):
    """
    Args:
        tokens (list(str)): list of string

    Returns:
        queries (list(str)): list of queries (SELECT or WITH queries) from tokens
    """

    cur_query = []
    queries = []
    on_query = False
    # loop through tokens and identify SELECT or WITH-AS SELECT queries
    for i in range(len(tokens)):
        if on_query:
            # add string to current query, stop when seeing ';' character
            cur_query.append(tokens[i])
            if tokens[i]!='' and tokens[i][-1]==';':
                on_query = False
                query = " ".join(cur_query)
                queries.append(query)
                cur_query = []
        else:
            # check if current query is WITH - AS query
            if tokens[i] == 'with' and tokens[i+2] == 'as' and (i==0 or len(tokens[i-1]) < 1 or tokens[i-1][-1] != '-'):
                cur_query.append(tokens[i])
                on_query = True
            # check if current query is SELECT query
            elif tokens[i] == 'select' and (i==0 or len(tokens[i-1]) < 1 or tokens[i-1][-1] != '-'):
                cur_query.append(tokens[i])
                on_query = True
            else:
                continue
    return queries


