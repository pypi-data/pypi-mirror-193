#%%
from check_connection.check_connection import check_connection, list_mean

avg = check_connection("orf.at", 15)

test_list = [1, "a", 4, "b", 3, "c", 2]
mean = list_mean(test_list)
print("List mean:", mean)
# %%
