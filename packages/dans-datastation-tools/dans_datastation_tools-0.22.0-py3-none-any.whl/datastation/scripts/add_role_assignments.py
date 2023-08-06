import argparse
import datetime
import logging

from datastation.batch_processing import batch_process
from datastation.config import init
from datastation.ds_pidsfile import load_pids
from datastation.dv_api import add_dataset_role_assignment, get_dataset_roleassigments
from datastation.open_csv_file import open_csv_file


def add_roleassignment(server_url, api_token, csv_writer, pid, role_assignee, role_alias, dry_run):
    current_assignments = get_dataset_roleassigments(server_url, api_token, pid)
    found = False
    for current_assignment in current_assignments:
        if current_assignment.get('assignee') == role_assignee and current_assignment.get('_roleAlias') == role_alias:
            found = True
            break

    action = "None" if found else "Added"

    csv_writer.writerow({'DOI': pid, 'Modified': datetime.datetime.now(), 'Assignee': role_assignee, 'Role': role_alias,
                         'Change': action})

    if found:
        logging.warning("{} is already {} for dataset {}".format(role_assignee, role_alias, pid))
    else:
        if dry_run:
            logging.info("Dry run: not adding {} as {} for dataset {}".format(role_assignee, role_alias, pid))
        else:
            role_assignment = {"assignee": role_assignee, "role": role_alias}
            add_dataset_role_assignment(server_url, api_token, pid, role_assignment)


def add_roleassignment_command(server_url, api_token, output_file, pids_file, role_assignee, role_alias, dry_run):
    pids = load_pids(pids_file)

    headers = ["DOI", "Modified", "Assignee", "Role", "Change"]
    csv_file, csv_writer = open_csv_file(headers, output_file)

    batch_process(pids, lambda pid: add_roleassignment(server_url, api_token, csv_writer, pid, role_assignee,
                                                       role_alias, dry_run))

    if not output_file == '-':
        csv_file.close()


def main():
    config = init()
    parser = argparse.ArgumentParser(description='Add role assignment to specified datasets')
    parser.add_argument('-d', '--datasets', dest='pid_file', help='The input file with the dataset pids')
    parser.add_argument('--dry-run', dest='dry_run', help="only logs the actions, nothing is executed", action='store_true')
    parser.add_argument('-a', "--role-assignment", help="Role assignee and alias (example: @dataverseAdmin=contributor)")
    parser.add_argument('-r', '--report', required=True, dest='output_file',
                        help="Destination of the output report file, '-' sends it to stdout")
    args = parser.parse_args()

    role_assignee = args.role_assignment.split('=')[0]
    role_alias = args.role_assignment.split('=')[1]

    server_url = config['dataverse']['server_url']
    api_token = config['dataverse']['api_token']
    add_roleassignment_command(server_url, api_token, args.output_file, args.pid_file, role_assignee, role_alias,
                               args.dry_run)


if __name__ == '__main__':
    main()
