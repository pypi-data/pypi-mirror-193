import sys
from datetime import datetime
from typing import cast

from rvid.seq.basic import RIDMaker
from rvid.seq.common import RID_REGEXP, RIDType, epoch_ms2rid, rid2epoch_ms


def __help() -> None:
    print("Syntax: rid [epoch|epoch_ms|RID|benchmark]")
    print("  epoch:     an integer value of seconds since UTC 1970-01-01 00:00")
    print("  epoch_ms:  as above in milliseconds. Suffix 'ms' to your integer")
    print("  RID:       a RID string, e.g. '000-ABC-000'")
    print("  benchmark: Test how fast RID:s are generated in your installation")


def benchmark(rid_maker: RIDMaker, loop_count: int) -> None:
    print(f"Generating {loop_count} RID:s as fast as I can...")
    import time

    start = time.time()
    for _ in range(loop_count):
        rid_maker.next()
    duration = time.time() - start
    rate = int(loop_count / duration)
    print(f"Done in {duration:.2f}s. ({rate} RID:s/second)")


def command() -> None:
    if len(sys.argv) == 1:
        print(RIDMaker().next())
        return

    elif len(sys.argv) > 2:
        return __help()

    arg = sys.argv[1]

    if arg.lower() in ("--help", "-h"):
        return __help()

    elif arg.isnumeric():
        rid = epoch_ms2rid(int(arg) * 1000)
        print(f"{arg} seconds corresponds to {rid}")

    elif arg.lower().endswith("ms") and arg[:-2].isnumeric():
        rid = epoch_ms2rid(int(arg[:-2]))
        print(f"{arg} milliseconds corresponds to {rid}")

    elif RID_REGEXP.match(arg):
        rid = cast(RIDType, arg)
        epoch_ms = rid2epoch_ms(rid)
        epoch = epoch_ms // 1000
        date_str = datetime.fromtimestamp(epoch).strftime("%Y-%m-%d %H:%M:%S")
        print(f"{rid} corresponds to {date_str} (millisecond epoch {epoch_ms})")

    elif arg.lower() == "benchmark":
        benchmark(rid_maker=RIDMaker(), loop_count=100 * 1000)

    else:
        print(f"ERROR: No one has taught me to parse this input: '{arg}'")
        return __help()
