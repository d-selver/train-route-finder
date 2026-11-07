from q1_b import find_trips

def trips_equal(result, expected):
    """
    Compare two trip lists allowing any order among trips that share
    the same total_duration AND number of trains.
    """
    if len(result) != len(expected):
        return False
    # Group by (duration, num_trains) and sort within each group
    def sort_key(item):
        return (item[1], len(item[0]))
    def normalize(lst):
        from itertools import groupby
        groups = []
        for _, g in groupby(sorted(lst, key=sort_key), key=sort_key):
            group = sorted(g, key=lambda x: str(x[0]))
            groups.extend(group)
        return groups
    return normalize(result) == normalize(expected)

tests = [
    # (description, args, expected)
    # --- from README ---
    (
        "istanbul->ankara from 10",
        ("istanbul", "ankara", 10),
        [
            [("T2",),       210],
            [("T5", "T6"),  330],
            [("T7", "T8"),  330],
            [("T1",),       330],
        ]
    ),
    # --- extra cases ---
    (
        "istanbul->ankara from 14 (only T2 valid)",
        ("istanbul", "ankara", 14),
        [
            [("T2",), 210],
        ]
    ),
    (
        "samsun->trabzon from 9 (one-stop via giresun)",
        ("samsun", "trabzon", 9),
        [
            [("T9", "T10"), 330],
        ]
    ),
    (
        "izmir->antalya from 10 (one-stop via afyon)",
        ("izmir", "antalya", 10),
        [
            [("T11", "T12"), 360],
        ]
    ),
    (
        "no valid trips (ankara->istanbul)",
        ("ankara", "istanbul", 0),
        []
    ),
]

correct = 0
wrong = 0

for desc, args, expected in tests:
    result = find_trips(*args)
    status = "PASS" if trips_equal(result, expected) else "FAIL"
    if status == "PASS":
        correct += 1
    else:
        wrong += 1
    print(f"[{status}] {desc}")
    if status == "FAIL":
        print(f"       got:      {result}")
        print(f"       expected: {expected}")

print(f"\nResults: {correct} correct, {wrong} wrong out of {len(tests)} tests")
