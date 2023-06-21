import subprocess



def add(number):
    if number == -1:
        batch_file_path = r'usbmmidd_v2\remove monitor.bat'
    if number == 1:
        batch_file_path = r'usbmmidd_v2\add monitor.bat'
    result = subprocess.run(batch_file_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
    if result.returncode == 0:
        return result.stdout
    else:
        return result.stderr