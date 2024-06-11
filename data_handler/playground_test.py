import main as dh
from tools import *

path = "data/stl/cube.stl"

dh.clear_output_paths()
dh.get_stl_info(path,dh.info_output_dir)
dh.slice_stl_to_dwg(path,[0,0,1],[0,0,10],dh.dwg_output_dir)
dh.get_dwg_info("output/CAD/dwg/sliced.dwg",dh.info_output_dir)