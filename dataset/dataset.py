from dataclasses import dataclass
from typing import Any 

@dataclass(repr=True,init=True,slots=True)
class DataSet:
    """ 
    
    Represent the dataset.
    
    Attributes:
    name:  the name of the dataset.
    description:  the descrition of the dataset.
    reference_url :  the url that will provide us the dataset and where we will found the dataset infos.
    download_url :  the url that will allows us to download the dataset.
    is_bundled :  the will allows us to know if the dataset is bundled into the solution.
    
    """
    name: str 
    description:str
    reference_url : str 
    download_url : str 
    is_bundled : bool  
    
    
    def download_dataset(self):
        """ Download a dataset and save its into the file system directory."""
        ### TODO: Use the _save model and others to implement the save logic.
        pass 
    def load_dataset(self):
        """ 
        Load the dataset given the name if the dataset is saved. on the file system. 
        Or download its save its and load its.
        """
        pass 
    def _save_dataset(self,dataset:Any)->bool:
        """ Save the dataset on the user filesystem."""
        #TODO : Implement the saving logics.
        pass 