# workflow

[![Build Status](https://travis-ci.org/richard-ma/workflow.svg?branch=master)](https://travis-ci.org/richard-ma/workflow)

# Usage
## Code Example
```
from workflow import *

if __name__ == "__main__":
    Workflow(
    ).push(Action(hello='world')
    ).push(Action(buy='buy buy')
    ).execute()
```
