from argparse import ArgumentParser, BooleanOptionalAction
from boto3 import Session
from json import loads
from requests import get, put, post
from requests_aws4auth import AWS4Auth

def main():
    args = parser.parse_args()
    args.func(args)

def list_repositories(args):
    """Query repositories available"""
    r = get(f'{args.endpoint}/_snapshot?pretty', verify=not args.insecure)
    print(r.text)

def add_repository(args):
    """Register S3 repository"""

    payload = loads(args.payload)
    region = payload["settings"]["region"]
    url = f'{args.endpoint}/_snapshot/{args.name}'

    credentials = Session().get_credentials()

    if not credentials:
        raise "Fail to detect AWS credentials"

    auth = AWS4Auth(
        credentials.access_key,
        credentials.secret_key,
        region,
        'es',
        session_token=credentials.token)

    headers = {"Content-Type": "application/json"}

    r = put(url, auth=auth, json=payload, headers=headers, verify=not args.insecure)

    print(r.status_code)
    print(r.text)

def list_snapshots(args):
    r = get(f'{args.endpoint}/_snapshot/{args.name}/_all?pretty', verify=not args.insecure)
    print(r.text)

def create_snapshot(args):
    r = put(f'{args.endpoint}/_snapshot/{args.repo}/{args.name}', verify=not args.insecure)
    print(r.text)

def restore_snapshot(args):
    r = post(f'{args.endpoint}/_snapshot/{args.repo}/{args.name}/_restore', verify=not args.insecure)
    print(r.text)

def default(args):
    parser.print_help()


parser = ArgumentParser(
    prog = 'aws-ossm',
    description = 'Add snapshots repository on S3 bucket to ElasticSearch')
parser.add_argument('-e', '--endpoint', default="https://127.0.0.1:8443", help="ElasticSearch endpoint. Default: https://127.0.0.1:8443")
parser.add_argument('-k', '--insecure', action=BooleanOptionalAction, default=False, help="Disable SSL verification")
parser.set_defaults(func=default)

subparsers = parser.add_subparsers()

repo_add_parser = subparsers.add_parser('repo-add', help="Register snapshots repository on S3")
repo_add_parser.set_defaults(func=add_repository)
repo_add_parser.add_argument('name', help="Name of the repository")
repo_add_parser.add_argument('payload', help="JSON payload with repository settings")

repo_list_parser = subparsers.add_parser('repo-list', help="List registered repositories")
repo_list_parser.set_defaults(func=list_repositories)

snap_list_parser = subparsers.add_parser('snap-list', help="List snapshots")
snap_list_parser.set_defaults(func=list_snapshots)
snap_list_parser.add_argument('name', help="Repository name")

snap_save_parser = subparsers.add_parser('snap-save', help="Create snapshot")
snap_save_parser.set_defaults(func=create_snapshot)
snap_save_parser.add_argument('repo', help="Repository name")
snap_save_parser.add_argument('name', help="Snapshot name")

snap_load_parser = subparsers.add_parser('snap-load', help="Restore snapshot")
snap_load_parser.set_defaults(func=restore_snapshot)
snap_load_parser.add_argument('repo', help="Repository name")
snap_load_parser.add_argument('name', help="Snapshot name")
