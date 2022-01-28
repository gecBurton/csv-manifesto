import io
import json
from itertools import chain
from typing import Dict, Iterator


def read_csv(file: io.StringIO) -> Iterator[Dict]:
    """read in a CSV encoded text-stream and convert to native Python

    >>> txt = '''"Name", "Sex", "Age", "Height (in)", "Consent Given"
    ... "Alex", "M", 41, null, true
    ... "Bert", "F", 42, 68.5, null
    ... "Carl", null, 32, 70.0, false
    ... '''

    >>> for line in read_csv(io.StringIO(txt)):
    ...     print(line)
    {'Name': 'Alex', 'Sex': 'M', 'Age': 41, 'Height (in)': None, 'Consent Given': True}
    {'Name': 'Bert', 'Sex': 'F', 'Age': 42, 'Height (in)': 68.5, 'Consent Given': None}
    {'Name': 'Carl', 'Sex': None, 'Age': 32, 'Height (in)': 70.0, 'Consent Given': False}
    """

    def f(_row):
        return json.loads(f"[{_row}]")

    header = f(next(file))

    for row in file:
        yield dict(zip(header, f(row)))


def write_csv(rows: Iterator[Dict], file: io.StringIO) -> None:
    """write native Python to a CSV encoded text-stream

    >>> data = [
    ...     {"Name": "Alex", "Sex": "M", "Age": 41, "Height (in)": None, "Consent Given": True},
    ...     {"Name": "Bert", "Sex": "F", "Age": 42, "Height (in)": 68.5, "Consent Given": None},
    ...     {"Name": "Carl", "Sex": None, "Age": 32, "Height (in)": 70.0, "Consent Given": False},
    ... ]

    >>> csv_file = io.StringIO()
    >>> write_csv(iter(data), csv_file)
    >>> _ = csv_file.seek(0)

    >>> print(csv_file.read())
    "Name", "Sex", "Age", "Height (in)", "Consent Given"
    "Alex", "M", 41, null, true
    "Bert", "F", 42, 68.5, null
    "Carl", null, 32, 70.0, false
    <BLANKLINE>
    """

    def f(_row) -> str:
        return f"{json.dumps(list(_row))[1:-1]}\n"

    first = next(rows)
    file.write(f(first.keys()))

    for row in chain([first], rows):
        file.write(f(row.values()))
