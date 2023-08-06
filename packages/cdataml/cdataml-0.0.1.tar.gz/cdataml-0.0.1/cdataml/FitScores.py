import pandas as pd
import sys, os, getopt

opts, args = getopt.getopt(sys.argv[1:], "hf:")
for opt, arg in opts:
    if opt in "-h":
        print("python3 FitScores.py -f <Raw_Data_File>")
        sys.exit()
    elif opt in "-f":
        Raw_FilePath = os.path.abspath(arg)

pd.set_option("display.max_colwidth", None)

# Load in USI.csv
USI_Data = pd.read_csv(r"../Metadata/USI.csv")
# Load in Raw_Data.csv
Raw_Data = pd.read_csv(Raw_FilePath) # Make this an option

# Subset data for rows containing coordinates
USI_Data_Subsetted = USI_Data.loc[USI_Data["Score"] != "Skip"].reset_index()

# Replace Unique_Spot_ID column

# Drop index

# Fill in Score and Replicate columns
USI_Data_Subsetted["Score"] = Raw_Data["Score"]
USI_Data_Subsetted["Replicate"] = Raw_Data["Replicate"]

# Save scored dataframe as USI.csv
USI_Data_Subsetted.to_csv(r"../Metadata/USI_Scored.csv", index=False)
