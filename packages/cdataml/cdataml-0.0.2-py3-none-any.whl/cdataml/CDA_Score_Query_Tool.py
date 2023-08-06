# 20/2/23 Last Updated
import pandas as pd
import cv2 as cv
import numpy as np
import sys, os, subprocess, getopt, shutil

print("Now Querying the Scores")

opts, args = getopt.getopt(sys.argv[1:], "h")
for opt, arg in opts:
    if opt in "-h":
        print("python3 CDA_Boundary_Tool.py -s (OPTIONAL)")
        sys.exit()

pd.set_option("display.max_colwidth", None)

# Load data
USI_Data = pd.read_csv("../Metadata/USI_Scored.csv") # Change this path
USI_Data["Query"] = np.nan
Images = pd.read_csv(r"../Metadata/Images.csv") # Change this path
Score_Key = cv.imread(cv.samples.findFile(r"../CDA_BoundaryTool/Lesion_Score_Key.tif"))
for row in range(0, len(USI_Data["Query"])):
    if pd.isna(USI_Data.loc[row, "Query"]) == True:
        USI = USI_Data.loc[row, "Unique_Spot_ID"]
        Current_Row = row
        break

def SaveAndQuit():
    # Save the output
    with open(r"../CDA_BoundaryTool/VersionTracker.txt") as VersionTracker:
        Version = VersionTracker.readline().strip()
        Update = Version.replace(Version, str(int(Version) + 1))
    with open(r"../CDA_BoundaryTool/VersionTracker.txt", "w") as VersionTracker:
        VersionTracker.write(Update)
        # Check if a query file already exists. If not, the current USI file becomes that file.
    if os.path.exists(r"../Metadata/Query.csv") == False:
        shutil.copy2(r"../Metadata/USI.csv", r"../Metadata/Query.csv")
    else:
        pass
    os.rename(r"../Metadata/Query.csv", r"../Metadata/Query_" + str(Version) + ".csv")
    USI_Data.to_csv(r"../Metadata/Query.csv", index=False)
    # Close the windows
    cv.destroyAllWindows()

def Skip_Spots(Row, Colname, Variablename):
    # Find the first row of the next leaf or image
    to_skip = 0
    while True:
        if(Current_Row + to_skip == len(USI_Data)):
            print("End of Dataframe!")
            SaveAndQuit()
            break_out_flag = True
            break
        else:
            test_leaf_ID = int(USI_Data.loc[Current_Row+to_skip, Colname])
            if test_leaf_ID == Variablename:
                to_skip = to_skip + 1
                continue
            else:
                print("Skipped " + str(to_skip))
                Row = Row + to_skip
                return(Row)

while True:
    # Retrieve metadata
    USI = USI_Data.loc[Current_Row, "Unique_Spot_ID"]
    ImgID = int(USI_Data.loc[Current_Row, "Img-ID"])
    PlantPerImgID = int(USI_Data.loc[Current_Row, "Plant-Per-Img-ID"])
    LeafID = int(USI_Data.loc[Current_Row, "Leaf-ID"])
    SpotID = int(USI_Data.loc[Current_Row, "Spot-ID"])
    Offset = int(USI_Data.loc[Current_Row, "Offset"])
    Score = int(USI_Data.loc[Current_Row, "Score"])
    PrevImagePath = ""

    # Check if current ImgID is same as previous ImgID
    # If not, load current ImgID into memory
    ImagePath = Images.loc[Images["Img-ID"] == ImgID, "Path"].to_string(index = False)
    if ImagePath == PrevImagePath:
        pass
    else:
        img = cv.imread(cv.samples.findFile(ImagePath))

    if img is None:
        print("Could not read image: " + ImagePath)
        continue

    # Add space to the top containing putText
    Shape_To_Add = np.full((200, img.shape[1], 3), 255, dtype=np.uint8)
    Concat_Image = np.concatenate((Shape_To_Add, img))
    Basename = os.path.basename(ImagePath)
    MetaData = "".join(str(e) for e in ["USI:", USI, ", Score:", Score, ", PlantPerImgID:", PlantPerImgID, ", LeafID:", LeafID, ", Offset:", Offset, ", SpotID:", SpotID])
    cv.putText(img = Concat_Image, text = MetaData, org = (50, 160), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=8, color=(0, 0, 0),thickness=8)

    # Scale score key to width of image and append to the bottom.
    Score_Scale_Val = Score_Key.shape[1] / Concat_Image.shape[1]
    Key_dim = (int(Score_Key.shape[1]/Score_Scale_Val), int(Score_Key.shape[0]/Score_Scale_Val))
    Downsize_Key = cv.resize(Score_Key, Key_dim)
    Concat_Image = np.concatenate((Concat_Image, Downsize_Key))

    # Display scaled down image
    Scale_Value = 0.25
    dim = (int(Concat_Image.shape[1]*Scale_Value), int(Concat_Image.shape[0]*Scale_Value))
    full_downsize = cv.resize(Concat_Image, dim)

    cv.imshow("Concat Image", Concat_Image)
    cv.setWindowProperty("Concat Image", cv.WND_PROP_TOPMOST, 1)

    print("Please press either ESC to exit, or q to query, or any other value to not query")

    break_out_flag = False

    while True:
        k = cv.waitKey(0)
        if k == 27: # Escape
            break_out_flag = True
            print("ESC Pressed")
            # Save and quit
            SaveAndQuit()
            break

        elif k == ord('q'): # skip to next image
            print("Score queried")
            USI_Data.loc[Current_Row, "Query"] = 1

        elif k == ord('m'): # missing leaf
            print("Skipping to next leaf")
            Current_Row = Skip_Spots(Current_Row, "Leaf-ID", LeafID)

        elif k == ord('n'): # skip to next image
            print("Skipping to next image")
            Current_Row = Skip_Spots(Current_Row, "Img-ID", ImgID)

        else:
            USI_Data.loc[Current_Row, "Query"] = 0

        if Current_Row == len(USI_Data)-1:
            print("End of Dataframe!")
            SaveAndQuit()
            break_out_flag = True
            break
        else:
            Current_Row += 1

        print("Current Row: ", str(Current_Row), "/", str(len(USI_Data)))
        # So that the image isn't always opened each loop - only if it is a new image
        PrevImagePath = ImagePath
        break

    if break_out_flag:
        break
