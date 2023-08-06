"""
Module:   file_manager.py
Package:  varius/utils
Date:     Mar 2020
Owner:    WJE

Description:    Reads, writes and moves files.

                The class calls each function as needed, closing
                the stream IO stream afterwards. Check correct
                moving of files, deletions, and writes, should be
                done outside of this class, or by calling the
                appropriate function from this class.
"""

import os


class FileManager(object):
    """

    """

    def __init__(self):
        """Constructor for  FileManager
        """
        pass

    def write(self,
              contents,
              file_name,
              directory):
        """
        Write the contents of 'string' to a file named 'file_name' in the 'directory'
        #TODO handle writing to an existing 'file_name' in 'directory'
        :param contents: the contents of the written file
        :param file_name: name of the new file
        :param directory: directory to write to
        :return:
        """
        if not os.path.exists(directory):
            os.makedirs(directory)
        filepath = os.path.join(directory,
                                file_name)
        try:
            filestream = open(filepath, 'w')
        except (IOError, OSError) as err:
            raise IOError(str(err))
        else:
            filestream.write(contents)
            filestream.close()

    def read(self,
             file_name,
             directory):
        """
        Read the contents of 'file_name', located in 'directory',
        outputing the contents as a string
        :param file_name: the name of the file, with extension
        :param directory: the directory to find file
        :return: string with the file contents
        """
        filepath = os.path.join(directory,
                                file_name)
        try:
            filestream = open(filepath, 'r')
        except Exception as err:
            contents = []
        else:
            contents = filestream.read()
            filestream.close()
        return contents

    def move(self,
             file_name,
             start_directory,
             destination):
        """
        Move the file 'file_name' from location 'start_directory'
        to 'destination'
        :param file_name: the name of the file to move, with extension
        :param start_directory: the directory to find the file
        :param destination: the directory to move the file to
        :return: True/False, success of operation
        """
        if not os.path.exists(destination):
            os.mkdir(destination)
        try:
            filepath_start = os.path.join(start_directory,
                                          file_name)
            filepath_end = os.path.join(destination,
                                        file_name)
            os.rename(filepath_start,
                      filepath_end)
            return True
        except Exception:
            return False
