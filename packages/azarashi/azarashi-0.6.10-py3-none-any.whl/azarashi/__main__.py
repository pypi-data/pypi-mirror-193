import sys
import datetime
import argparse
from azarashi import QzssDcrDecoderException
from azarashi import decode
from azarashi import decode_stream


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('type', help='set a message type: "spresense", "ublox" or "hex"', type=str)
    parser.add_argument('--source', help='output source messages', action='store_true')
    parser.add_argument('--unique', help='supress duplicate messages', action='store_true')
    args = parser.parse_args()
    if args.type not in ('hex', 'spresense', 'ublox'):
        raise NotImplementedError('The message type must be specified as "spresense", "ublox" or "hex"')

    while True:
        now = datetime.datetime.now().isoformat()
        try:
            report = decode_stream(sys.stdin, args.type, unique=args.unique)
            print(f'{now} --------------------------------\n{report}\n')
            if args.source == True:
                if type(report.sentence) is bytes:
                    src = "b'" + ''.join(r'\x%02X' % c for c in report.sentence) + "'"
                else:
                    src = report.sentence
                print(f'# src: {src}\n# hex: {report.message.hex().upper()[:-1]}\n')
            sys.stdout.flush()
        except QzssDcrDecoderException as e:
            print(f'{now} --------------------------------\n# [{type(e).__name__}] {e}\n', file=sys.stderr)
        except NotImplementedError as e:
            print(f'{now} --------------------------------\n# [{type(e).__name__}] {e}\n', file=sys.stderr)
        except Exception as e:
            print(f'{now} --------------------------------\n# [{type(e).__name__}] {e}\n', file=sys.stderr)
            return 1


if __name__ == '__main__':
    exit(main())
