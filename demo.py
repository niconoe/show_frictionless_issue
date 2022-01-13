import json
import os

from pathlib import Path
from pprint import pprint

from frictionless import validate_package

THIS_SCRIPT_PATH = Path(__file__).parent
EXAMPLE_DESCRIPTOR_PATH = THIS_SCRIPT_PATH / "example" / "datapackage.json"

with open(EXAMPLE_DESCRIPTOR_PATH) as json_file:
    descriptor_data = json.load(json_file)
    #os.chdir(EXAMPLE_DESCRIPTOR_PATH.parent)

    report = validate_package(descriptor_data)
    if report.valid:
        print("✔︎ valid package")
    else:
        print("✕ valid package, errors:")
        # Here, we should report top-level errors

        for task in report.tasks:
            if len(task.errors) != 0:
                print(f"Errors for resource {task.resource['name']}:")

                if len(task.errors) == 1:
                    errors_to_print = [task.error]
                else:
                    errors_to_print = task.errors

                for task_err in errors_to_print:
                    pprint(task_err)