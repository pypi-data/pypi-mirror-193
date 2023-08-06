# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 16:49:37 2021

@author: alpha
"""

import napari
from magicgui import magic_factory
from napari_plugin_engine import napari_hook_implementation
import dask.array as da
# from napari.layers import Image
import fsspec, requests
from bs4 import BeautifulSoup
from skimage import io
from dask import delayed
from .dataset_info import get_datasets

@magic_factory(auto_call=False,call_button="Load Dataset",
                dataset={"choices": sorted([key for key in get_datasets()])}
                )



def load_bil_data(
    # viewer: napari.Viewer,
    dataset: str
) -> 'napari.types.LayerDataTuple':
    
    ''' 
    This panel provides a tool for load pre-determined datasets from BIL
    data currently available via https://download.brainimagelibrary.org/
    
    Current datasets are fMOST modality which included multi-resolution single-color
    projections.
    '''
    
    dataset_info = get_datasets()[dataset]
    
    bilData = dataset_info['url']
    ext = 'tif'

    def getFilesHttp(url: str,ext: str) -> list:
        def listFD(url, ext=''):
            page = requests.get(url).text
            # print(page)
            soup = BeautifulSoup(page, 'html.parser')
            return [url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]
        
        files = []
        for file in listFD(url, ext):
            files.append(file)
            
        return files

    def getImage(fileObj):
        with fileObj as f:
            print('Reading {} \n'.format(f))
            return io.imread(f)

    
    data = []
    for ii in bilData:
        images = sorted(getFilesHttp(ii, ext))
        images = [fsspec.open(x,'rb') for x in images]
        data.append(images)
    
    

    for idx,ii in enumerate(data):
        sampleImage = getImage(ii[0])
        images = [delayed(getImage)(x) for x in ii]
        images = [da.from_delayed(x, sampleImage.shape,dtype=sampleImage.dtype) for x in images]
        images = da.stack(images)
        data[idx] = images
    
    
    
    name = dataset
    scale = dataset_info['scale']
    multiscale = True if len(dataset_info['url']) > 1 else False
    contrast_limits = dataset_info['contrast_limits']
    data = data if len(data)>1 else data[0]
    
    meta = {
        'name':name,
        'scale':scale,
        'multiscale':multiscale,
        'contrast_limits':contrast_limits
        # 'channel_axis':meta['name'][cc],
        # 'metadata':meta['metadata'],
        
        }
        
        
    
    return (data,meta,'image')
    


@napari_hook_implementation
def napari_experimental_provide_dock_widget():
    return load_bil_data

