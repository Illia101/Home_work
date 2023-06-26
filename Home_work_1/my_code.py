#import glob
#import shutil
import os
import unicodedata

# def file_home_work(file):



#     file_normalize = unicodedata.normalize('NFKC', file) and os.listdir()
    
    
    
    
#     if file_normalize == glob.glob1(file_normalize ,'*.png') or glob.glob1(file_normalize ,'*.jpeg') or glob.glob1(file_normalize ,'*.jpg') or glob.glob1(file_normalize ,'*.svg'):
#     #Файли з фотографіями
#         for file_name in file_normalize:
#             source_path = os.path.join(file_name,'D:\Home_work_1\images' )
#         return source_path
#     elif file_normalize == glob.glob1(file_normalize ,'*.avi') or glob.glob1(file_normalize ,'*.mp4') or glob.glob1(file_normalize ,'*.mov') or glob.glob1(file_normalize ,'*.mkv'):
#          for file_name in file_normalize:
#             source_path = os.path.join(file_name,'D:\Home_work_1\_video' )
#          return source_path
#     # Відео файли
#     elif file_normalize == glob.glob1(file_normalize ,'*.doc') or glob.glob1(file_normalize ,'*.docx') or glob.glob1(file_normalize ,'*.txt') or glob.glob1(file_normalize ,'*.pdf') or glob.glob1(file_normalize ,'*.xlsx') or glob.glob1(file_normalize ,'*.pptx'):
#     # Файли документів
#         for file_name in file_normalize:
#             source_path = os.path.join(file_name,'D:\Home_work_1\documents' )
#         return source_path
  
#     elif file_normalize == glob.glob1(file_normalize ,'*.mp3') or glob.glob1(file_normalize ,'*.ogg') or glob.glob1(file_normalize ,'*.wav') or glob.glob1(file_normalize ,'*.amr'):
#     # Файли з музикою
#          for file_name in file_normalize:
#             source_path = os.path.join(file_name,'D:\Home_work_1\_audio' )
#          return source_path
        
#     elif file_normalize == glob.glob1(file_normalize ,'*.zip') or glob.glob1(file_normalize ,'*.gz') or glob.glob1(file_normalize ,'*.tar'):
#     # Файли з архівом
#          for file_name in file_normalize:
#             source_path = os.path.join(file_name,'D:\Home_work_1\_archives' )
#          return source_path
        
#     else:
#         for file_name in file_normalize:
#             source_path = os.path.join(file_name,'D:\Home_work_1\_archives' )
#         return source_path


def file_home_work(file):
    file_normalize = unicodedata.normalize('NFKC', file.name)
    
    if file_normalize.endswith(('.png', '.jpeg', '.jpg', '.svg')):
        source_path = os.path.join(file.path, 'D:\Home_work_1\images')
        #Файли з фотографіями
        return source_path
    elif file_normalize.endswith(('.avi', '.mp4', '.mov', '.mkv')):
        source_path = os.path.join(file.path, 'D:\Home_work_1\_video')
        #Відео файли
        return source_path
    elif file_normalize.endswith(('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx')):
        source_path = os.path.join(file.path, 'D:\Home_work_1\documents')
        #Файли з документами
        return source_path
    elif file_normalize.endswith(('.mp3', '.ogg', '.wav', '.amr')):
        source_path = os.path.join(file.path, 'D:\Home_work_1\_audio')
        #Аудіо файли
        return source_path
    elif file_normalize.endswith(('.zip', '.gz', '.tar')):
        source_path = os.path.join(file.path, 'D:\Home_work_1\_archives')
        #Архівні файли
        return source_path
    else:
        source_path = os.path.join(file.path, 'D:\Home_work_1\_archives')
        return source_path

path_1 = 'D:\Games\path_1'

for entry in os.scandir(path_1):
    if entry.is_file():
        file_home_work(entry)
    elif entry.is_dir():
        try:
            os.rmdir(entry.path)  # Видалення порожніх папок
        except OSError as e:
            print(f"Помилка видалення папки {entry.path}: {e}")


    
