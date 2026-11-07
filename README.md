# Train Route Finder

A Python project that validates train journeys and finds available direct and one-transfer routes between cities based on a requested earliest departure time.

## Overview

The project works with a sample train schedule and supports journeys with either one train or two connecting trains. It checks route compatibility and departure timing, then calculates elapsed journey durations and sorts the available options.

## Features

- Validate direct train journeys.
- Validate one-transfer journeys by checking the origin, destination, and connecting city.
- Ensure the first train departs no earlier than the requested start time.
- Check that the connecting train departs after the first train arrives.
- Search possible direct and one-transfer combinations.
- Sort route options by total elapsed journey time.

## Project Structure

| File | Description |
| --- | --- |
| `q1_a.py` | Train schedule and journey validation logic. |
| `q1_b.py` | Search for valid direct and connecting journeys. |
| `q1_a_test.py` | Test cases for journey validation. |
| `q1_b_test.py` | Test cases for route search and duration calculation. |

## How to Run

Requires Python 3.

Run the validation tests:

```bash
python q1_a_test.py
```

Run the route-search tests:

```bash
python q1_b_test.py
```

## Sample Data

The train schedule (T1–T12) is defined directly in the Python modules and represents illustrative route and timetable data. It is not connected to a live railway timetable or booking service.

## Testing

The included test scripts cover direct routes, valid and invalid connections, departure-time constraints, route search, and cases where no route is available. All 13 included test cases passed in the local run performed during project preparation.
