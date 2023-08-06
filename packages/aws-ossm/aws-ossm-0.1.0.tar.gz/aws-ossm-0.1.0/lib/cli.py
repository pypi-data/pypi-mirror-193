from argparse import ArgumentParser, BooleanOptionalAction
from requests_aws4auth import AWS4Auth
import boto3
from requests import put
from json import loads

def main():
    args = parser.parse_args()
    args.func(args)

def list_repositories(args):
    """Query repositories available"""
    pass

def add_repository(args):
    """Register S3 repository"""

    payload = loads(args.payload)
    region = payload["settings"]["region"]
    url = f'{args.endpoint}/_snapshot/{args.name}'

    credentials = boto3.Session().get_credentials()

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

def list_snapshots():
    pass

def create_snapshot():
    pass

def restore_snapshot():
    pass

def default(args):
    parser.print_help()


parser = ArgumentParser(
    prog = 'aws-ossm',
    description = 'Add snapshots repository on S3 bucket to ElasticSearch')
parser.add_argument('-e', '--endpoint', default="https://127.0.0.1:8443", help="ElasticSearch endpoint")
parser.set_defaults(func=default)

subparsers = parser.add_subparsers()

repo_add_parser = subparsers.add_parser('add_repository', help="Register snapshots repository on S3")
repo_add_parser.set_defaults(func=add_repository)


repo_add_parser.add_argument('name', help="Name of the repository to create")
repo_add_parser.add_argument('payload', help="JSON payload with repository settings")
repo_add_parser.add_argument('-k', '--insecure', action=BooleanOptionalAction, default=False, help="Disable SSL verification")


