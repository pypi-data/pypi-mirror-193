"""Very simple tool to browse a SCOS-2000 database"""
import argparse
import re
from pathlib import Path

from pyscos2000 import SCOS


def main():
    args = parse_args()
    scos = SCOS(Path(args.database).expanduser())

    if args.check:
        scos.check()

    if args.tm is not None:
        tmpattern = re.compile(args.tm, re.I)
        for row in sorted(scos.pid.rows):
            description = row['PID_DESCR'].value
            spid = row['PID_SPID'].value
            text = f"{spid} {description}"
            if len(args.tm) > 0 and tmpattern.search(text) is None:
                continue
            print(f"({row['PID_TYPE'].value},{row['PID_STYPE'].value})",
                  spid, description)

    if args.fields is not None:
        tmpattern = re.compile(args.fields, re.I)
        for row in sorted(scos.pid.rows):
            description = row['PID_DESCR'].value
            spid = row['PID_SPID'].value
            text = f"{spid} {description}"
            if tmpattern.search(text) is None:
                continue
            print(spid)

            for plf in sorted(scos.plf.rows):
                if plf['PLF_SPID'].value != spid:
                    continue
                pcf = scos.pcf.get(plf['PLF_NAME'].value)
                print(pcf['PCF_NAME'].value, pcf['PCF_DESCR'].value)


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('database',
                        type=str,
                        help='Location of the SCOS database to browse or inspect')

    parser.add_argument('--check',
                        action='store_true',
                        default=False,
                        help='Run all checkers on the database')

    parser.add_argument('-m', '--tm',
                        default=None,
                        type=str,
                        help="List all matching TM packets (accepts regex pattern)")

    parser.add_argument('-c', '--tc',
                        default=None,
                        type=str,
                        help="List all matching TC packets")

    parser.add_argument('-f', '--fields',
                        default=None,
                        nargs="?",
                        help="List the fields of this TM packet (accepts regex pattern)")

    parser.add_argument('-p', '--parameters',
                        default=None,
                        nargs="?",
                        help="List the parameters of this TC")

    return parser.parse_args()


if __name__ == '__main__':
    main()
