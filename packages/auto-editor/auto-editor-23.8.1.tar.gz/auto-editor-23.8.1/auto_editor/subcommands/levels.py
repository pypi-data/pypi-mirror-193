from __future__ import annotations

import sys
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any

import numpy as np

from auto_editor.analyze import Levels
from auto_editor.ffwrapper import FFmpeg, FileInfo
from auto_editor.objs.edit import (
    audio_builder,
    motion_builder,
    pixeldiff_builder,
    subtitle_builder,
)
from auto_editor.objs.util import ParserError, parse_dataclass
from auto_editor.output import Ensure
from auto_editor.utils.bar import Bar
from auto_editor.utils.func import setup_tempdir
from auto_editor.utils.log import Log
from auto_editor.utils.types import frame_rate, pos
from auto_editor.vanparse import ArgumentParser

if TYPE_CHECKING:
    from fractions import Fraction

    from numpy.typing import NDArray


@dataclass
class LevelArgs:
    input: list[str] = field(default_factory=list)
    edit: str = "audio"
    timebase: Fraction | None = None
    ffmpeg_location: str | None = None
    my_ffmpeg: bool = False
    help: bool = False


def levels_options(parser: ArgumentParser) -> ArgumentParser:
    parser.add_required("input", nargs="*")
    parser.add_argument(
        "--edit",
        metavar="METHOD:[ATTRS?]",
        help="Select the kind of detection to analyze with attributes",
    )
    parser.add_argument(
        "--timebase",
        "-tb",
        metavar="NUM",
        type=frame_rate,
        help="Set custom timebase",
    )
    parser.add_argument("--ffmpeg-location", help="Point to your custom ffmpeg file")
    parser.add_argument(
        "--my-ffmpeg",
        flag=True,
        help="Use the ffmpeg on your PATH instead of the one packaged",
    )
    return parser


def print_floats(arr: NDArray[np.float_]) -> None:
    for a in arr:
        sys.stdout.write(f"{a:.20f}\n")


def print_ints(arr: NDArray[np.uint64] | NDArray[np.bool_]) -> None:
    for a in arr:
        sys.stdout.write(f"{a}\n")


def main(sys_args: list[str] = sys.argv[1:]) -> None:
    parser = levels_options(ArgumentParser("levels"))
    args = parser.parse_args(LevelArgs, sys_args)

    ffmpeg = FFmpeg(args.ffmpeg_location, args.my_ffmpeg)

    bar = Bar("none")
    temp = setup_tempdir(None, Log())
    log = Log(quiet=True, temp=temp)

    sources = {}
    for i, path in enumerate(args.input):
        sources[str(i)] = FileInfo(path, ffmpeg, log, str(i))

    assert "0" in sources
    src = sources["0"]

    tb = src.get_fps() if args.timebase is None else args.timebase
    ensure = Ensure(ffmpeg, src.get_samplerate(), temp, log)

    if ":" in args.edit:
        method, attrs = args.edit.split(":", 1)
    else:
        method, attrs = args.edit, ""

    def my_var_f(name: str, val: str, coerce: Any) -> Any:
        if src.videos:
            if name in ("x", "width"):
                return pos((val, src.videos[0].width))
            if name in ("y", "height"):
                return pos((val, src.videos[0].height))
        return coerce(val)

    for src in sources.values():
        method_map = {
            "audio": audio_builder,
            "motion": motion_builder,
            "pixeldiff": pixeldiff_builder,
            "subtitle": subtitle_builder,
        }
        levels = Levels(ensure, src, tb, bar, temp, log)

        if method in method_map:
            builder = method_map[method]

            try:
                obj = parse_dataclass(attrs, builder)
            except ParserError as e:
                log.error(e)

            if "threshold" in obj:
                del obj["threshold"]

        if method == "audio":
            print_floats(levels.audio(obj["stream"]))
        elif method == "motion":
            print_floats(levels.motion(obj["stream"], obj["blur"], obj["width"]))
        elif method == "pixeldiff":
            print_ints(levels.pixeldiff(obj["stream"]))
        elif method == "subtitle":
            print_ints(
                levels.subtitle(
                    obj["pattern"],
                    obj["stream"],
                    obj["ignore_case"],
                    obj["max_count"],
                )
            )
        else:
            log.error(f"Method: {method} not supported")

    log.cleanup()


if __name__ == "__main__":
    main()
