# EchoSoft

EchoSoft is a Python utility designed to automatically detect and clear unused files and applications on Windows devices to free up space. This program helps maintain system efficiency by removing unnecessary clutter from your computer.

## Features

- **Unused File Detection**: Scans directories for files that have not been accessed within a user-defined timeframe.
- **Unused Application Detection**: Identifies installed applications that are no longer in use.
- **Automated Cleanup**: Removes detected unused files and applications to free up disk space.
- **Logging**: Keeps a log of all activities, including successfully removed items and errors encountered.

## Installation

1. Ensure you have Python installed on your system.
2. Clone this repository or download the `echosoft.py` file to your local machine.
3. Install required Python packages using pip:
   ```bash
   pip install psutil
   ```

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory where `echosoft.py` is located.
3. Run the script using Python:
   ```bash
   python echosoft.py
   ```
4. The program will start scanning for unused files in the default directory `C:/Users/Public` and unused applications in `C:/Program Files`. You can modify these paths and parameters in the script as needed.

## Configuration

- Change the `directory` variable in the `clear_unused_items` function to specify a different directory for unused file detection.
- Adjust the `days_unused` parameter to redefine what constitutes an "unused" file.

## Logging

All operations are logged to `echosoft.log` in the script's directory. This includes information on removed files, applications, and any errors encountered during the process.

## Disclaimer

Use EchoSoft at your own risk. Ensure you have backups of important data before running the program, as it will permanently delete files and applications it identifies as unused.

## License

This project is licensed under the MIT License - see the LICENSE file for details.