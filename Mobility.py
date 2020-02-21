import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
import numpy as np
from sodapy import Socrata
import mobility_config
import seaborn as sns
sns.set()
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline

###Call NYC OpenData API
client = Socrata("data.cityofnewyork.us", '7YJroGSBVCt6gzuLz6whih0yc')

# Example authenticated client (needed for non-public datasets):
client = Socrata('data.cityofnewyork.us',
                  mobility_config.app_token,
                  username=mobility_config.app_user,
                  password=mobility_config.app_pw)

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
trip_diary = client.get("kcey-vehy", limit=8000)
main_survey = client.get("jpcp-ic7c", limit=4000)
# Convert to pandas DataFrame
trip_diary_df = pd.DataFrame.from_records(trip_diary)
main_survey_df = pd.DataFrame.from_records(main_survey)
