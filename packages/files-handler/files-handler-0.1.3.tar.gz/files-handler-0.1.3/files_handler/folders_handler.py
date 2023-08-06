import os
import shutil
class folders_handler:

    def __init__(self, path_ref):
        self.path_ref = path_ref

    def clear_folder(self, folder_path_to_clear):
        """
        Clear the folder
        
        :param folder_path_to_clear: the path of the folder to clear 
        :type folder_path_to_clear: string
    
        :return: void
        """
        print(f"Clearing folder: {folder_path_to_clear}")

        if os.path.exists(folder_path_to_clear):
            shutil.rmtree(folder_path_to_clear)

    def verify_and_create_folder(self, folder_path_to_create, message=''):
        """
        Verifify and Create a Folder
        
        :param folder_path_to_create: the path of the folder to create 
        :type folder_path_to_create: string
    
        :return: if the folder not exists create the folder and returns True, if exists returns False
        :type: boolean 
        """
        print(f"Verifying and creating folder: {folder_path_to_create}")
        if not os.path.exists(folder_path_to_create):
            print(message)
            os.mkdir(folder_path_to_create)
            return True
        return False