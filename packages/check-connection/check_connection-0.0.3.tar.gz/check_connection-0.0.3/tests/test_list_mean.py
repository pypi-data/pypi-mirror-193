#%%
import sys
sys.path.insert(0, './src/check_connection')
from check_connection import list_mean

list=[1,2,3,4,5,6]

def test_list_mean():
    outcome = list_mean(list)
    assert outcome == 3.5
# %%
