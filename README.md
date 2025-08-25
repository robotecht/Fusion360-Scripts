# Fusion360-Scripts

This guide explains how to run a Python script in Autodesk Fusion 360 using the built-in script editor.

## Prerequisites

- Autodesk Fusion 360 installed
- A valid Autodesk account
- Python script file (e.g., `logarithmic_spiral.py`)

## Steps to Run the Script

1. **Open Fusion 360**  
   Launch Autodesk Fusion 360 and open a new or existing design.

2. **Access the Script and Add-Ins Panel**  
   - Go to the **Tools** tab in the toolbar.
   - Click on **Scripts and Add-Ins**.

3. **Locate the Script**  
   - In the Scripts and Add-Ins dialog, switch to the **Scripts** tab.
   - Click **+ Add** to add a new script.
   - Browse to the folder containing your script and select it.

4. **Run the Script**  
   - Select the script from the list.
   - Click **Run** to execute the script.

## Notes

- Ensure the script is written using Fusion 360's API (`adsk.core`, `adsk.fusion`, etc.).
- You may need to restart Fusion 360 if the script does not appear immediately.
- Scripts are executed in the context of the active design.

## Troubleshooting

- If the script fails, check the **Text Commands** window for error messages.
- Make sure all required modules are imported and the script is syntactically correct.

## Author

Developed by Finny Varghese
