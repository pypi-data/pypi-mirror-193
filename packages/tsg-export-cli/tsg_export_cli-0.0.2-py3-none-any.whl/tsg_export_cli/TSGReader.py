from pathlib import Path
import pandas as pd
import numpy as np

import pytsg
from tsgxr.read import tsg_to_xarray, cras_to_dataarray, reorder_variables

class TSGReader:
    def ds_to_df(ds):
        '''
        ds: xarray.Dataset

        converts an xarray Dataset to a pandas DatFrame
        can't be done automatically due to performance issues?

        to_dataframe tries to allocate ridicilous amounts of memory
        
        results in an infinite loop,
        even when the problematic columns are removed:
            (Spectra/Centres/Depths/Widths)
        '''
        df = pd.DataFrame()
        delete_columns = []
        for x in ds.data_vars:
            if x.lower() in [
                'spectra',
                'centres',
                'depths',
                'widths',
            ]:
                continue

            try:
                df[x] = ds[x].to_series().fillna('NULL').replace('', 'NULL')
            except np.core._exceptions._ArrayMemoryError:
                delete_columns.append(x)

        for x in delete_columns:
            del df[x]

        return df.fillna('NULL')

    def load_full_tsg(
        directory,
        spectra='NIR',
        index_coord='sample',
        image=True,
        subsample_image=1,
        drop=[],
    ):
        directory = Path(directory)
        tsgdata = pytsg.parse_tsg.read_package(directory, read_cras_file=image)
        dataset = tsg_to_xarray(tsgdata, spectra, index_coord=index_coord)
        if image:
            dataset['Image'] = cras_to_dataarray(tsgdata, subsample=subsample_image)
        dataset = reorder_variables(dataset, drop=drop)
        return dataset

    def save_as_csv(
        ds,
        save_path='nir.csv',
    ):
        '''
        nir and tir CSV files can't be combined
        this is because their data isn't exactly 1:1

        this method produces 2 csvs
        '''
        df = TSGReader.ds_to_df(ds)
        depth_column = df['Depth (m)']
        del df['Depth (m)']

        df.insert(2, 'EndDepth', depth_column)
        df.insert(2, 'StartDepth', depth_column)
        df.to_csv(save_path, na_rep='NULL', index=False)

    def save_nir_tir_pair(
        ds_nir,
        ds_tir,
        nir_save_path='nir.csv',
        tir_save_path='tir.csv',
    ):
        TSGReader.save_as_csv(ds_nir, nir_save_path)
        TSGReader.save_as_csv(ds_tir, tir_save_path)

    def tsg_to_csv(
        directory,
        index_coord='sample',
        image=True,
        subsample_image=1,
        drop=[],
        nir_save_path='nir.csv',
        tir_save_path='tir.csv',
    ):
        nir_ds = TSGReader.load_full_tsg(
            directory,
            spectra='NIR',
            index_coord=index_coord,
            image=image,
            subsample_image=subsample_image,
            drop=drop,
        )

        tir_ds = TSGReader.load_full_tsg(
            directory,
            spectra='TIR',
            index_coord=index_coord,
            image=image,
            subsample_image=subsample_image,
            drop=drop,
        )

        TSGReader.save_nir_tir_pair(
            nir_ds,
            tir_ds,
            nir_save_path=nir_save_path,
            tir_save_path=tir_save_path,
        )
