import os
import shutil
import psutil
import logging

# Configure logging
logging.basicConfig(filename='echosoft.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def get_unused_files(directory, days_unused=30):
    """Scans a directory for files not accessed in a specified number of days."""
    unused_files = []
    current_time = os.path.getatime(directory)
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            last_access_time = os.path.getatime(file_path)
            if (current_time - last_access_time) / (24 * 3600) >= days_unused:
                unused_files.append(file_path)
    return unused_files

def remove_files(file_list):
    """Removes files from the file system."""
    for file in file_list:
        try:
            os.remove(file)
            logging.info(f'Removed file: {file}')
        except Exception as e:
            logging.error(f'Failed to remove file: {file} - {e}')

def get_unused_applications():
    """Detects unused applications by checking for processes not run recently."""
    unused_apps = []
    # Placeholder logic for detecting unused applications
    # In real-world, this might require more sophisticated methods such as
    # checking application usage logs or registry keys
    installed_apps = os.listdir('C:/Program Files')
    for app in installed_apps:
        if not psutil.pid_exists(app):
            unused_apps.append(app)
    return unused_apps

def remove_applications(app_list):
    """Removes applications from the system."""
    for app in app_list:
        app_path = f'C:/Program Files/{app}'
        try:
            shutil.rmtree(app_path)
            logging.info(f'Removed application: {app}')
        except Exception as e:
            logging.error(f'Failed to remove application: {app} - {e}')

def clear_unused_items(directory='C:/Users/Public', days_unused=30):
    """Clears unused files and applications."""
    logging.info('Starting cleanup process...')
    
    # Clear unused files
    unused_files = get_unused_files(directory, days_unused)
    if unused_files:
        logging.info(f'Found unused files: {unused_files}')
        remove_files(unused_files)
    else:
        logging.info('No unused files found.')

    # Clear unused applications
    unused_apps = get_unused_applications()
    if unused_apps:
        logging.info(f'Found unused applications: {unused_apps}')
        remove_applications(unused_apps)
    else:
        logging.info('No unused applications found.')
    
    logging.info('Cleanup process completed.')

if __name__ == '__main__':
    clear_unused_items()