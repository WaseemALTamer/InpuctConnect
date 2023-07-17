import requests
import zipfile
import os

persentage = 0

def TillCompletetion(download):
    global persentage
    persentage = download
    return persentage
    

def install():
    documents_path = os.path.expanduser("~/Documents")
    try:
        folder_path = f"{documents_path}\InputConnect"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    except:
        pass
    file_url = "https://www.amyuni.com/downloads/usbmmidd_v2.zip"
    installation_path = f"{folder_path}/usbmmidd_v2.zip"

    response = requests.get(file_url, stream=True)
    response.raise_for_status()
    total_size = int(response.headers.get('content-length', 0))
    download = 0
    with open(installation_path, "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
            download += len(chunk)
            print(TillCompletetion(f"{int(download/total_size * 100)}%"))
            
    print("File downloaded successfully.")



def extraction():
    documents_path = os.path.expanduser("~/Documents")
    folder_path = f"{documents_path}\InputConnect"
    
    zip_file_path = f"{folder_path}/usbmmidd_v2.zip"
    extract_directory = folder_path

    if os.path.exists(zip_file_path):
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_directory)
        return "Extracted"
    else:
        return None


def AddBatFiles():
    documents_path = os.path.expanduser("~/Documents")
    folder_path = f"{documents_path}/InputConnect/usbmmidd_v2"
    batch_file_path = folder_path
    batch_content = '''@cd /d "%~dp0"

@goto %PROCESSOR_ARCHITECTURE%
@exit

:AMD64
@cmd /c deviceinstaller64.exe install usbmmidd.inf usbmmidd
@cmd /c deviceinstaller64.exe enableidd 1
@goto end

:x86
@cmd /c deviceinstaller.exe install usbmmidd.inf usbmmidd
@cmd /c deviceinstaller.exe enableidd 1

:end
@pause
'''
    batch_content_2 = '''@cd /d "%~dp0"

@goto %PROCESSOR_ARCHITECTURE%
@exit

:AMD64
@cmd /c deviceinstaller64.exe install usbmmidd.inf usbmmidd
@cmd /c deviceinstaller64.exe enableidd 1
@goto end

:x86
@cmd /c deviceinstaller.exe install usbmmidd.inf usbmmidd
@cmd /c deviceinstaller.exe enableidd 1

:end
@pause
'''

    with open(f"{batch_file_path}/add monitor.bat", "w") as file:
        file.write(batch_content)

    with open(f"{batch_file_path}/remove monitor.bat", "w") as file:
        file.write(batch_content_2)

    print("Batch file created successfully.")