# 15/2/23 Last Updated
import sys, getopt, os, glob
import pandas as pd
import subprocess
from natsort import natsorted
# python3 GenerateMetadata.py -f ../DatasetCreationTool/ToolTestSet/Raw_Images/  -l 4 -s 4 -r 2 -o ./

### Handling optional arguments
# Default arguments
file_loc = None
leaves_per_img = 8
spots_per_leaf = 8
replicates = 1
output_loc = None

opts, args = getopt.getopt(sys.argv[1:], "f:l:s:r:o:h")
for opt, arg, in opts:
    if opt in "-h": # help
        print("python3 GenerateMetadata.py -f <filepath containing images> -l <max leaves per image> -s <spots per leaf> -r <replicates> -o <output directory>")
        sys.exit()
    elif opt == "-f": # filepath containing images
        file_loc = arg
    elif opt in "-l": # leaves per image
        leaves_per_img = arg
    elif opt in "-s": # spots per leaf
        spots_per_leaf = arg
    elif opt in "-r": # number of images per biological replicate
        replicates = arg
    elif opt in "-o": # output location
        output_loc = arg

subprocess.run(["mkdir", os.path.join(output_loc, 'Metadata/')])
#subprocess.run(["mkdir", os.path.join(output_loc, 'Scripts/')])

### CSV document for containing image filepaths
# Store the image filepaths in a list
dir_path = os.path.join(file_loc, '**/*.tif')
filenames = []
for file in glob.glob(dir_path, recursive=True):
    filenames.append(file)
filenames = natsorted(filenames)
# ID values (1 to number of images)
file_IDs = [FID for FID in range(1, len(filenames)+1)]
# Combine
Filepath_Doc = pd.DataFrame({'Img-ID': file_IDs, 'Path': filenames})
# Output to CSV in output location
Filepath_Doc.to_csv(os.path.join(output_loc, 'Metadata/Images.csv'), index=False)
### Check if len(filenames) % replicates == 0
print("Images.csv created")

### CSV document for containing treatments
# ID values (1 to number of spots)
Treatment_Doc = pd.DataFrame({'Treat-ID': [TID for TID in range(1, int(spots_per_leaf)+1)]})
# Suggested empty columns
Treatment_Doc['TreatmentName'] = None
Treatment_Doc['Effector'] = None
Treatment_Doc['NLR1'] = None
Treatment_Doc['NLR2'] = None
# Output to CSV in output location
Treatment_Doc.to_csv(os.path.join(output_loc, 'Metadata/Treatments.csv'), index=False)
print("Treatments.csv created")

### CSV document for the main data
total_count = int(spots_per_leaf) * int(leaves_per_img) * len(filenames)
USIs = []
Img_IDs = []
Plant_IDs = []
Plant_Per_Img_IDs = []
Leaf_IDs = []
Offsets = []
Spot_IDs = []
Replicates = []
Img_ID, Plant_ID, Plant_Per_Img_ID, Leaf_ID, Offset, Spot_ID, Replicate = 1, 1, 1, 1, 1, 1, 1

for i in range(1, total_count+1):
    #USI
    USIs.append('S' + str(i))

    # Img_ID
    Img_IDs.append(Img_ID)
    if i % (total_count / len(filenames)) == 0:
        Img_ID = Img_ID + 1

    # Plant_ID
    Plant_IDs.append(Plant_ID)
    if i % (2 * int(spots_per_leaf)) == 0:
        Plant_ID = Plant_ID + 1

    # Plant_Per_Image
    Plant_Per_Img_IDs.append(Plant_Per_Img_ID)
    if i % (2 * int(spots_per_leaf)) == 0:
        if Plant_Per_Img_ID == int(leaves_per_img) / 2:
            Plant_Per_Img_ID = 1
        else:
            Plant_Per_Img_ID = Plant_Per_Img_ID + 1

    # Leaf_ID
    Leaf_IDs.append(Leaf_ID)
    if i % int(spots_per_leaf) == 0:
        if Leaf_ID == 1:
            Leaf_ID = 2
        elif Leaf_ID == 2:
            Leaf_ID = 1

    # Offset
    Offsets.append(Offset)
    if i % (int(spots_per_leaf)*2) == 0:
        if Offset == int(spots_per_leaf):
            Offset = 1
        else:
            Offset = Offset + 1

    # Spot_ID
    if i % int(spots_per_leaf) == 0:
        Spot_ID = int(spots_per_leaf)
    else:
        Spot_ID = i % int(spots_per_leaf)
    Spot_IDs.append(Spot_ID)

    # I need to work out how to do replicates - I think they are tied to image, so the user may need to input replicates into Images.csv
    # Replicates
    #Replicates.append(Replicate)
    #if i % (2 * int(spots_per_leaf) * int(leaves_per_img)) == 0:
    #    Replicate = Replicate + 1

Main_Doc = pd.DataFrame({'Unique_Spot_ID': USIs, 'Img-ID': Img_IDs, 'Plant-ID': Plant_IDs, 'Plant-Per-Img-ID': Plant_Per_Img_IDs, 'Leaf-ID': Leaf_IDs, 'Spot-ID': Spot_IDs, 'Offset': Offsets})
Main_Doc['Treat-ID'] = Main_Doc['Spot-ID']
Main_Doc["Replicate"] = None
Main_Doc['Score'] = ""
Main_Doc['y1'] = None
Main_Doc['y2'] = None
Main_Doc['x1'] = None
Main_Doc['x2'] = None

Main_Doc.to_csv(os.path.join(output_loc, 'Metadata/USI.csv'), index=False)
print("USI.csv created")

# If a spot doesn't exist, create a tool where the user can skip spot (coords marked NA)
