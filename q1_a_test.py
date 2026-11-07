from q1_a import is_valid_trip

tests = [
    # --- from README ---
    ("direct T2, departs 14 >= 10",          ("istanbul", "ankara",  10, ("T2",)),       True),
    ("direct T1, departs 10 >= 10",          ("istanbul", "ankara",  10, ("T1",)),       True),
    ("one-stop T5->T6, valid connection",    ("istanbul", "ankara",  10, ("T5", "T6")),  True),
    ("one-stop T3->T4, T3 departs 9 < 10",  ("istanbul", "ankara",  10, ("T3", "T4")),  False),
    ("one-stop T5->T8, cities don't connect",("istanbul", "ankara",  10, ("T5", "T8")), False),
    # --- extra cases ---
    ("direct T11, correct route",            ("izmir",    "afyon",   10, ("T11",)),      True),
    ("direct T9, wrong end_city",            ("samsun",   "trabzon",  9, ("T9",)),       False),
    ("one-stop T9->T10, valid connection",   ("samsun",   "trabzon",  9, ("T9", "T10")), True),
]

correct = 0
wrong = 0

for desc, args, expected in tests:
    result = is_valid_trip(*args)
    status = "PASS" if result == expected else "FAIL"
    if result == expected:
        correct += 1
    else:
        wrong += 1
    print(f"[{status}] {desc} => got {result}, expected {expected}")

print(f"\nResults: {correct} correct, {wrong} wrong out of {len(tests)} tests")
