import os
import sys
import shutil
import pandas as pd

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


class obrpy(object):
    """
        Main class
        for correct treatment of .obr files
        * See "compute" function below for details
    """

    def __init__(self,path=None,showpath=False):

        # Launch GUI if no path is provided
        if not path:
            from .PathSelector import PathSelector
            import tkinter as tk
            # Initialize gui
            root = tk.Tk()
            root.geometry("400x100")
            root.title("Path Selector")

            # Create gui
            app = PathSelector(master=root)
            app.pack_propagate(0)
            app.mainloop()

            # Get path
            path = app.path

        # In construction generates absolute path and name based on the folder name
        self.path = os.path.abspath(path)
        self.name = f'{os.path.basename(os.path.normpath(path))}.pkl'

        # Just to check it
        if showpath:
             print(os.listdir(self.path))

        # Tries to load dataset object, else, if not found, creates one
        try:
            print('\nDATASET OBJECT FOUND IN PATH')
            self.load()

        except Exception as e:

            if 'No such file or directory' in str(e):
                print('\nNO DATASET OBJECT FOUND IN PATH')
                print('Creating new one \n')
            else:
                print(e)
                exit()

            # Folder structure
            self.folders = {
            '0_OBR'              : './0_OBR',
            '1_PROCESSED_DATA'   : './1_PROCESSED_DATA',
            '2_INFORMATION'      : './2_INFORMATION'}

            # Creates folder structure if not exists
            for key,val in self.folders.items():
                if not os.path.exists(os.path.join(self.path,val)):
                    os.makedirs(os.path.join(self.path,val))

            # Move all .obr files to its folder, if they exists
            for file in os.listdir(self.path):
                if file.endswith('.obr'):
                    print('Moving',file,'to',self.folders['0_OBR'])
                    shutil.move(os.path.join(self.path,file), os.path.join(self.path,self.folders['0_OBR'],file))

            # Information filenames
            self.INFO = {
            'obr book filename'             :   'obr_book.csv',
            'conditions filename'           :   'conditions.csv',
            'slices book filename'          :   'slices_book.csv',
            'slices filename'               :   'slices.pkl',
            'dataset book filename'         :   'dataset_book.csv',
            'dataset filename'              :   'dataset.pkl',
            'obrfiles filename'             :   'obrfiles.pkl',
            'measures filename'             :   'measures.pkl',
            'fiber distribution filename'   :   'fiber_distribution.txt'}

            # OBR files as an object
            self.obrfiles = dict()


