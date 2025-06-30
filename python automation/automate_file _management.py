# Python script to automate file management tasks such as organizing files into directories based on their extensions, renaming files, and deleting old files.
import os
import shutil


# Define the path to your download directory
downloads_folder ='D:\\Downloads' 


# Define target folders for different file types
folders = {
    'images': ['.jpg', '.jpeg', '.png', '.gif'],
    'documents': ['.pdf', '.docx', '.txt', '.xlsx'],
    'videos': ['.mp4', '.avi', '.mov'],
    'audio': ['.mp3', '.wav', '.flac'],
    'archives': ['.zip', '.rar', '.tar'],
    'scripts': ['.py', '.sh', '.js'],
    'installers': ['.exe', '.msi'],
    'others': []
}

# Create target folders if they don't exist
for folder in folders:
    folder_path = os.path.join(downloads_folder, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


# Loop through files in the downloads folder
for filename in os.listdir(downloads_folder):
    file_path = os.path.join(downloads_folder, filename)

    # Skip directories
    if os.path.isdir(file_path):
        continue

    # Check file extension and move to the appropriate folder
    for folder, extensions in folders.items():
        if any(filename.lower().endswith(ext) for ext in extensions):
            target_folder = os.path.join(downloads_folder, folder)
            shutil.move(file_path, target_folder)
            print(f'Moved {filename} to {target_folder}')
            break
        
        
#         Output 
        
#         PS D:\Namatovu-Christine-Maria>  d:; cd 'd:\Namatovu-Christine-Maria'; & 'd:\Namatovu-Christine-Maria\.venv\Scripts\python.exe' 'c:\Users\Maria\.vscode\extensions\ms-python.debugpy-2025.8.0-win32-x64\bundled\libs\debugpy\launcher' '49751' '--' 'd:\Namatovu-Christine-Maria\python automation\automate_file _management.py' 
# Moved Anaconda3-2024.10-1-Windows-x86_64.exe to D:\Downloads\installers
# Moved AssigmentFive.docx to D:\Downloads\documents
# Moved back.png to D:\Downloads\images
# Moved ChatGPT Image Jun 26, 2025, 02_43_18 PM.png to D:\Downloads\images
# Moved Chosen Becky - Kansubire.mp3 to D:\Downloads\audio
# Moved Christine.pdf to D:\Downloads\documents
# Moved CustoSpark_Launch_Support_Proposal.docx to D:\Downloads\documents
# Moved GMT20250409-144136_RecordingnewChat.txt to D:\Downloads\documents
# Moved logo.png to D:\Downloads\images
# Moved python-3.10.0-amd64.exe to D:\Downloads\installers
# Moved Python_Data_Structures_Explained.docx to D:\Downloads\documents
# Moved utorrent_installer.exe to D:\Downloads\installers
# Moved Voluntary Agreement.pdf to D:\Downloads\documents
# Moved xampp-windows-x64-8.2.12-0-VS16-installer.exe to D:\Downloads\installers
# PS D:\Namatovu-Christine-Maria> 