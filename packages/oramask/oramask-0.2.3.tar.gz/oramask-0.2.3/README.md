[![build status](https://github.com/andzhi4/raws/actions/workflows/matrix-test.yml/badge.svg)](https://github.com/andzhi4/raws/actions/workflows/matrix-test.yml)
# oramask

Oramask is a simplistic converter of Oracle specific date/time masks to Python's strftime masks.

## Installation

You can install the oramask by cloning the repository and running pip install:
```shell
git clone git@github.com:andzhi4/oramask
cd oramask && pip install .
```

or using PyPi:
```shell
python3 -m pip install oramask
```

## Examples
Here is an example of usage:
```python
from oramask import ora_to_sft
from datetime import datetime

now = datetime.now()
formatted = now.strftime(ora_to_sft('DD-MON-YYYY HH24:MI:SS'))
print(formatted)
# Output: 23-Feb-2023 17:51:15
```

## Contributing

If you find a bug or have an idea for a new feature, feel free to create an issue or submit a pull request.

## License

Oramask is released under the MIT License.





