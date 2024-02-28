# Custom Fields and Property Setters Export Checker

## Overview

This utility assists in validating the completeness of exported fixtures for Custom Fields and Property Setters in a Frappe App. It ensures that all defined Custom Fields and Property Setters are correctly included in the export, promoting a reliable deployment process.

## Usage

1. **Setup**

   - move the [check_fixtures.py](./check_fixtures.py) to the root of your custom app folder.

2. **Spin up bench console**

   - Use the bench console to run the function, _*sitename*_ is the sitename of the site you want to check.

   ```bash
       bench --site sitename console
   ```

3. **Run Fixtures Checker:**

   - Execute the fixtures checker function.

   ```python
   import check_fixtures

   check_fixtures.check_fixtures()
   ```
