from .ProgramArgParser import ProgramArgParser
from .TSGReader import TSGReader
from .TSGImageReader import TSGImageReader
from tqdm import tqdm
import sys
import os

class TSGInterface:
    def __init__(self):
        self.args = ProgramArgParser()
        match self.args.command:
            case 'export-csvs':
                self.args.execute = self.export_csvs
            case 'export-images':
                self.args.execute = self.export_images
            case other:
                raise NotImplementedError('Implement this command choice in TSGInterface')

    def execute(self):
        if not os.path.exists(self.args.output_dir):
            os.mkdir(self.args.output_dir)

        return self.args.execute()

    def export_csvs(self):
        nir_output = os.path.join(self.args.output_dir, 'nir.csv')
        tir_output = os.path.join(self.args.output_dir, 'tir.csv')

        TSGReader.tsg_to_csv(
            self.args.data_dir,
            image=False,
            nir_save_path=nir_output,
            tir_save_path=tir_output,
        )

    def get_depth_ranges(self, **kwargs):
        def gen_depth_ranges():
            start_depth = self.args.start_depth
            while start_depth < self.args.end_depth:
                end_depth = min(self.args.end_depth, start_depth + self.args.depth_delta)
                yield (start_depth, end_depth)
                start_depth = end_depth

        depth_ranges = [depth_range for depth_range in gen_depth_ranges()]
        depth_ranges_with_progress = tqdm(
            depth_ranges,
            unit_scale=(self.args.end_depth - self.args.start_depth) / len(depth_ranges),
            unit='m',
            **kwargs
        )

        return depth_ranges_with_progress

    def export_images(self):
        ds = TSGReader.load_full_tsg(self.args.data_dir, subsample_image=self.args.subsampling_factor)

        for (start_depth, end_depth) in self.get_depth_ranges():
            image = TSGImageReader.from_ds(ds, start_depth, end_depth)
            img_name = f'{start_depth}-{end_depth}m.png'
            img_path = os.path.join(self.args.output_dir, img_name)
            image.save(img_path)

def execute_tsg_interface():
    try:
        TSGInterface().execute()
    except ValueError as e:
        print(e, file=sys.stderr)
        return 1
    except Exception as e:
        print(e, file=sys.stderr)
        return 2

    return 0
