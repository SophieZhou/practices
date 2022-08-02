import h5py
import numpy as np 

"""
create_dataset ： 新建 dataset
create_group ： 新建 group
"""

x = np.arange(100)

with h5py.File('test.h5','w') as f:
    f.create_dataset('gaze',data=x)
    subgroup = f.create_group('p1')
    subgroup.create_dataset('camera',data=x[:5])
    subgroup.create_dataset('filename',data=x)
    subgroup.create_dataset('distortion',data=x[:10])
    


"""
    keys() ： 获取本文件夹下所有的文件及文件夹的名字
    f['key_name'] : 获取对应的对象    
"""
def read_data(filename):
    with h5py.File(filename,'r') as f:

        def print_name(name):
            print(name)

        f.visit(print_name)
        print('---------------------------------------')
        subgroup = f['p1']  
        print(subgroup.keys())
        print('---------------------------------------')
        dset = subgroup['camera']
        print(dset)
        print(dset.name)
        print(dset.shape)
        print(dset.dtype)
        print(dset[:])
        print('---------------------------------------')

read_data('test.h5')