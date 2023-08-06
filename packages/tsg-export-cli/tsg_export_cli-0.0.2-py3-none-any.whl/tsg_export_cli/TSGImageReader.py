from PIL import Image
import numpy as np

class TSGImageReader:
    '''
    Provides an interface to TSG image data
    can query the borehole image based on the depth range
    '''
    def from_ds(ds, *args, **kwargs):
        '''
        ds: xarray.Dataset
        '''
        return TSGImageReader.from_arr(ds['Image'], *args, **kwargs)

    # TODO: this doesn't give the correct image
    # I think I slice in 1d but it should be in 2d
    def from_arr(arr, start_depth, end_depth, subsample=1):
        '''
        arr: np.array representing the RGB values in the image
        start_depth: depth as a float in metres
        end_depth: depth as a float in metres
        subsample: uint representing how many points are discarded:
            image should already be subsampled when loaded so be careful
        '''
        subsampled_arr = arr
        start_index = np.searchsorted(subsampled_arr.depth, start_depth)
        end_index   = np.searchsorted(subsampled_arr.depth, end_depth)
        array_in_range = subsampled_arr[start_index:end_index + 1]
        return Image.fromarray(np.array(array_in_range)[::subsample], 'RGB')
