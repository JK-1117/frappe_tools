# Role Permission Patch

## Overview

This patch simplifies the management of role permissions by utilizing an Excel file. To get started, follow these steps:

1. **Prepare Excel File:** Create an Excel file using the specified format found in [sample_excel.xlsx](./sample_excel.xlsx).

2. **Generate JSON File:**

   - Execute the [main.py](./main.py) Python script to convert the Excel data into a JSON file.
   - Example:
     ```bash
     python main.py
     ```

3. **Dependencies:**

   - Ensure you have the necessary dependencies installed before running the scripts.
     ```bash
     pip install -f requirements.txt
     ```

4. **Import Role Permissions:**
   - Utilize the generated JSON file with the provided patch sample: [set_base_role_permissions_patch.py](./set_base_role_permissions_patch.py).

## Usage

Put the generated JSON file together with the `set_base_role_permissions_patch.py` inside your custom app's patch folder and include it in the patches file.

## Note

Ensure that your Excel file adheres to the format in [sample_excel.xlsx](./sample_excel.xlsx). The generated JSON file from [main.py](./main.py) is crucial for importing role permissions with the patch script. Simplify your role permission management process using this convenient patch.
