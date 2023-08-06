import json
import os
import subprocess

import psycopg2


PARENT_DIR = os.path.join(os.path.dirname(__file__), '..')
DB_CREDS_FILE = os.path.join(PARENT_DIR, "auth/postgres_creds.json")


def connect_to_db():
    with open(DB_CREDS_FILE, 'r') as f:
        creds = json.load(f)

    conn = psycopg2.connect(
        database=creds['name'],
        host=creds['host'],
        user=creds['user'],
        password=creds['password'],
        port=creds['port']
    )
    return conn, conn.cursor(), creds


def backup_db(db_name: str, db_user: str, db_host: str, db_port: str):
    os.system(
        f"pg_dump -U {db_user} -h {db_host} -p {db_port} " \
        f"-F c -b -f 'tests/backup_pg_db.sql' {db_name}"
    )


def clear_db(cursor):
    cursor.execute(
        "TRUNCATE TABLE users, orgs, users_to_orgs, api_keys, " \
        "transactions, datasets, dataset_lineages, " \
        "storage_used_snapshots, egressed_data_records, b2_app_keys, " \
        "charges, rates;"
    )


def run_tests():
    print("--------------- running python client tests ---------------")
    os.system("pytest knapsack/test_setup_account.py")
    # print("------------------ running backend tests ------------------")


def restore_db(
    cursor,
    db_name: str,
    db_user: str,
    db_host: str,
    db_port: str
):
    # TODO: why is this so particular? Having trouble getting
    # this running in os.system, and trying to wait on restore_process
    # always hangs..?
    restore_process = subprocess.Popen(
        [
            "pg_restore",
            "--clean",
            "-U", f"{db_user}",
            "-h", f"{db_host}",
            "-d", f"{db_name}",
            "./tests/backup_pg_db.sql"
        ]
    )
    # this fails
    # restore_process.wait()


def remove_files() -> None:
    # TODO: this ought to be made more robust.
    os.remove(os.path.expanduser("~/.knapsack_local/storage/knap_tester/blueprints.json"))


if __name__ == "__main__":
    conn, cursor, creds = connect_to_db()
    backup_db(creds['name'], creds['user'], creds['host'], creds['port'])
    clear_db(cursor)
    conn.close()

    run_tests()

    conn, cursor, creds = connect_to_db()
    restore_db(cursor, creds['name'], creds['user'],
               creds['host'], creds['port'])

    remove_files()
    conn.close()
