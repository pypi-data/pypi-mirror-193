import os
import pickle

def load(self):
    """ Load the object existing in the root of the folder """

    path_to_dataset = os.path.join(self.path,self.name)

    new_path = self.path
    new_name = self.name

    with open(path_to_dataset, 'rb') as inp:
        self.__dict__ = pickle.load(inp)

    self.path = new_path
    self.name = new_name

    print(f'{self.name} loaded!')

    return self