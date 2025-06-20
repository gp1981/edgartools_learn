# Setting things up  
# [Overview](https://edgartools.readthedocs.io/en/latest/)

# 1. Import the library
from edgar import *
from tqdm.notebook import tqdm

# 2. Tell the SEC who you are (required by SEC regulations)
set_identity("email@address.com")  # Replace with your email
download_edgar_data()
use_local_storage()
