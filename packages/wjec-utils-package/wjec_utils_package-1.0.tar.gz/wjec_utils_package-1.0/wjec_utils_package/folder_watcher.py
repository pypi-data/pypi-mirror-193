"""
Module:   folder_watcher.py
Package:  varius/utils
Date:     Mar 2020
Owner:    WJE

Description:    A (somewhat) generalized folder watcher class
                used to periodically poll a folder or group of
                folders.

                To use this class, inherit from it and call the
                'on_filefound' function, placing the execution
                code there.
"""

import time
import os


class FolderWatcher(object):

    def __init__(self,
                 watch_folders,
                 check_period=0.5):
        """ Class constructor
        Sets the check period in seconds and initializes the
        dictionary used to hold the watched folders.
        :param watch_folders: dict - [key] folder common name, [value] folder path
        :param check_period: time in seconds between checks
        """
        self.check_period = check_period
        self.watch_list = {}
        for folders in watch_folders:
            self.add_subject(folders,
                             watch_folders[folders])
        self.is_running = True

    def execute_loop(self):
        """
        Execute a folder check with periodicity 'check_period'
        Calls the built-in function 'on_filefound' if
        the watched folders have file contents
        """
        while self.is_running:
            for folder in self.watch_list:
                if self.watch_list[folder].is_active():
                    file_list = self.watch_list[folder].get_files()
                    if file_list:
                        filepath = self.watch_list[folder].directory
                        self.on_filesfound(folder,
                                           filepath,
                                           file_list)
            time.sleep(self.check_period)

    def on_filesfound(self,
                      folder_name,
                      filepath,
                      files):
        """
        Function stub.
        This function gets called when extending the
        FolderWatcher class.
        :param folder_name: string -common name of the watched folder
        :param filepath: string - path to the file that was found
        :param files: list - string -of files in the folder
        :return:
        """
        pass

    def set_period(self,
                   check_period):
        """
        Set the folder check periodicity
        :param check_period: float - the folder watch period
        """
        # self.debug_log.debug("Folder watcher check period set to " + str(check_period) + " seconds")
        self.check_period = check_period

    def add_subject(self,
                    subject_name,
                    directory_path,
                    active=True):
        """
        Add a watch folder.
        Will not add the folder if it does not exist
        :param subject_name: string - The folder's common name
        :param directory_path: string - The path to the directory
        :param active: boolean - The active watch status, default=True
        """
        try:
            self.watch_list[subject_name] = SubjectFolder(directory_path,
                                                          active)
        except Exception:
            pass  # TODO

    def remove_subject(self,
                       subject_name=None):
        """
        Remove the watch folder specified by <subject_name>
        If subject name is not specified, do not remove
        :param subject_name: string - Name of the watch folder to remove
        :return: boolean, removal success
        """
        try:
            del self.watch_list[subject_name]
            return True
        except KeyError:
            return False
        except Exception as excep:
            return False


class SubjectFolder(object):
    """
    The watched folder and information used by FolderWatcher
    """

    def __init__(self,
                 directory_path,
                 active=True):
        """ Subclass constructor
        :param directory_path: string - Path name of the folder
        :param active: boolean - The watch status of the folder, default=True
        """
        self.directory = None
        try:
            self.set_directory(directory_path)
        except Exception as err:
            pass  # TODO
        self.active_watch = active

    def set_directory(self,
                      directory_path):
        """
        Set folder path to watch
        :param directory_path: The directory path
        """
        if os.path.exists(directory_path):
            pass
        else:
            os.makedirs(directory_path)
        self.directory = os.path.abspath(directory_path)

    def set_active(self,
                   active_level):
        """
        Set the watch status to true or false
        :param active_level:
        """
        self.active_watch = active_level

    def is_active(self):
        """
        Check if folder is an active watch target
        :return:
        """
        return self.active_watch

    def isempty(self):
        """
        Returns True if the watch is not active.
        :return: boolean, whether the directory has files (folders not counted)
        """
        if not self.is_active():
            return True
        else:
            directory_contents = os.listdir(self.directory)
            if directory_contents:
                return False
            else:
                return True

    def get_files(self):
        """
        Return a list of the files in the watched directory.
        Returns an empty list if the watch is not active.
        :return: list of string
        """
        if not self.is_active():
            return []
        else:
            folder_contents = os.listdir(self.directory)
            filelist = []
            for content in folder_contents:
                if os.path.isfile(os.path.join(self.directory,
                                               content)):  # This check removes special entries (.,..)
                    filelist.append(content)
            return filelist
