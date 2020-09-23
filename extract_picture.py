import os
import shutil
import imghdr

save_picture_path = input('输入图片保存路径：') 
for name in os.listdir(): # 筛选当前目录下的所有文件夹
    if  os.path.isdir(name): 
        picture_path = os.path.join(name, 'materials') # 壁纸图片所在目录相对路径
        for file_name in os.listdir(picture_path):  # materials目录下的文件和文件夹名称
            file_path = os.path.join(picture_path, file_name) # materials目录下的文件和文件夹相对路径
            if os.path.isfile(file_path): #找出materials目录下的所有文件
                if imghdr.what(file_path): # 找出其中的图片文件
                    shutil.copy(file_path, save_picture_path) # 将图片移动到指定文件夹
