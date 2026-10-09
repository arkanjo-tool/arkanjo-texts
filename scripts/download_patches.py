from argparse import Namespace
import argparse
from pathlib import Path
import re
import shutil

import yaml
import b4
import b4.mbox


whitelist_trailers = [ "Subject:", "From" ]


NAME_EMAIL_RE = re.compile(
    rb'\b[A-Za-z][A-Za-z0-9._-]*(?:[ \t\r\n]+[A-Za-z][A-Za-z0-9._-]*)*'
    rb'[ \t\r\n]+'
    rb'<[A-Za-z0-9.!#$%&\'*+/=?^_`{|}~-]+@'
    rb'[A-Za-z0-9.-]+\.[A-Za-z]{2,}>'
)


workdir_path = Path("data")
output_path = workdir_path / "anom-series"


def process_mbox(filename):
    path = Path(filename)

    with path.open("rb") as file:
        lines = file.readlines()

    output = []
    inside_message = True

    for line in lines:
        if line.startswith(b"From "):
            inside_message = False

        if line.startswith(b"\n") or line.startswith(b"\r\n"):
            inside_message = True

        if (
            not inside_message and
            not any(line.startswith(trailer.encode()) for trailer in whitelist_trailers)
        ):
            continue

        output.append(line)


    data = b"".join(output)

    data = NAME_EMAIL_RE.sub(b"#### <####>", data)

    path.write_bytes(data)

def append_file(source, destination):
    with source.open("rb") as src, destination.open("ab") as dst:
        shutil.copyfileobj(src, dst)


def main(year):
    with open(workdir_path / "patches.yaml", "r") as file:
        patches = yaml.safe_load(file)

    for patch in patches:
        if year not in patch.get("context", ""):
            continue

        message_ids = patch["messageId"]

        if isinstance(message_ids, str):
            message_ids = [message_ids]

        wantname = message_ids[0].strip("/").split("/")[-1]
        series_path = output_path / f"{wantname}.mbx"

        series_path.unlink(missing_ok=True)

        for index, message_id in enumerate(message_ids):
            message_id = message_id.strip("/").split("/")[-1]

            temporary_path = output_path / f".{wantname}.{index}.mbx"

            try:
                cmdargs = Namespace(
                    subcmd="mbox",
                    checknewer=True,
                    refetch=False,
                    localmbox=None,
                    msgid=message_id,
                    minimize=False,
                    outdir=output_path,
                    maildir=False,
                    wantname=temporary_path.name,
                    config={}
                )

                b4.setup_config(cmdargs=cmdargs)
                b4.mbox.main(cmdargs)

                process_mbox(temporary_path)

                append_file(temporary_path, series_path)
            finally:
                temporary_path.unlink(missing_ok=True)


if __name__ == "__main__":
    project_root = Path.cwd()

    if not (project_root / "scripts").is_dir():
        print("Error: this command must be run from the project root directory.")
        exit(1)

    if not (project_root / "data" / "patches.yaml").is_file():
        print("Error: 'data/patches.yaml' not found. Run this command from the project root directory.")
        exit(1)

    parser = argparse.ArgumentParser(description="Patch series processing script")
    parser.add_argument("-y", "--year", type=str)

    args = parser.parse_args()

    output_path.mkdir(parents=True, exist_ok=True)
    main(args.year)
