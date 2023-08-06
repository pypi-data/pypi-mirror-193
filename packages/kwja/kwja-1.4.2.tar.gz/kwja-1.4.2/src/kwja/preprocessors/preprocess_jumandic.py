import csv
import logging
import sys
from argparse import ArgumentParser
from pathlib import Path

from kwja.utils.jumandic import JumanDic
from kwja.utils.progress_bar import track

logger = logging.getLogger(__name__)
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s: %(message)s", level=logging.DEBUG)


def main():
    parser = ArgumentParser()
    parser.add_argument(
        "-i",
        "--input-dir",
        type=str,
        help="path to JumanDIC root directory",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        type=str,
        default="./data",
        help="path to directory to save data",
    )
    args = parser.parse_args()
    if not Path(args.input_dir).is_dir():
        sys.stderr.write("--input must be an existing JumanDIC root directory\n")
        exit(1)
    input_path = Path(args.input_dir) / "kwja_dic" / "kwja.dic"
    if not input_path.is_file():
        sys.stderr.write(
            "JumanDIC KWJA dictionary not found\nmake sure you have built the KWJA dictionary by calling 'make kwja'\n"
        )
        exit(1)
    outdir = Path(args.output_dir)
    if outdir.exists():
        if not outdir.is_dir():
            sys.stderr.write("--output-dir must be a directory\n")
            exit(1)
    else:
        outdir.mkdir(parents=True)

    with open(str(input_path)) as f:
        dicreader = csv.reader(f)
        rows = list(dicreader)
    # entries = {}
    entries = []
    for row in track(rows):
        surf, _, _, _, pos, subpos, conjform, conjtype, lemma, reading, repname, sem = row
        semantics = ""
        if repname != "*":
            semantics = f"代表表記:{repname}"
        if sem != "NIL":
            if len(semantics) > 0:
                semantics += " "
            semantics += sem
        entries.append([surf, reading, lemma, pos, subpos, conjtype, conjform, semantics])
    JumanDic.build(outdir, entries)


if __name__ == "__main__":
    main()
