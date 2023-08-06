# 20/2/23 Last Updated
import pandas as pd
import cv2 as cv
import numpy as np
import sys, os, subprocess, getopt

# Option for scoring
scoring = False

opts, args = getopt.getopt(sys.argv[1:], "hs")
for opt, arg in opts:
    if opt in "-h":
        print("python3 CDA_Boundary_Tool.py -s (OPTIONAL)")
        sys.exit()
    elif opt in "-s":
        scoring = True

pd.set_option("display.max_colwidth", None)

# Load data
USI_Data = pd.read_csv(r"../Metadata/USI.csv") # Change this path
Images = pd.read_csv(r"../Metadata/Images.csv") # Change this path
if scoring == True:
    Score_Key = cv.imread(cv.samples.findFile(r"Lesion_Score_Key.tif"))
# Identify next USI with no Coordinates and retrieve related data
for row in range(0, len(USI_Data["y1"])):
    if pd.isna(USI_Data.loc[row, "y1"]) == True:
        #USI = USI_Data.loc[row, "Unique_Spot_ID"]
        Current_Row = row
        break

def SaveAndQuit():
    # Save the output
    with open("VersionTracker.txt") as VersionTracker:
        Version = VersionTracker.readline().strip()
        Update = Version.replace(Version, str(int(Version) + 1))
    with open("VersionTracker.txt", "w") as VersionTracker:
        VersionTracker.write(Update)
    os.rename(r"../Metadata/USI.csv", r"../Metadata/USI_" + str(Version) + ".csv")
    USI_Data.to_csv(r"../Metadata/USI.csv", index=False)
    # Close the windows
    cv.destroyAllWindows()

def MakeSelectionSquare(Coordinates):
    # Horizontal Length HLen
    HLen = Coordinates[3] - Coordinates[1]
    # Vertical Length VLen
    VLen = Coordinates[2] - Coordinates[0]
    # Difference
    Diff = abs(HLen-VLen)
    # Add half the difference between them to the greater of the shorter axis
    # Subtract half the difference between them to the lesser of the shorter axis
    if HLen == max(HLen, VLen):
        Coordinates[2] = Coordinates[2] + (Diff / 2)
        Coordinates[0] = Coordinates[0] - (Diff / 2)
    else:
        Coordinates[3] = Coordinates[3] + (Diff / 2)
        Coordinates[1] = Coordinates[1] - (Diff / 2)
    return Coordinates

def Skip_Spots(Row, Colname, Variablename):
    # Find the first row of the next leaf or image
    Temp_Offsets = []
    to_skip = 0
    while True:
        # If the end of the data frame is reached, save and quit
        if(Current_Row + to_skip == len(USI_Data)):
            print("End of Dataframe!")
            SaveAndQuit()
            break_out_flag = True
            break
        # If it isn't the end of the dataframe
        else:
            # Test to see if the current ID is the same as the previous one
            test_ID = int(USI_Data.loc[Current_Row+to_skip, Colname])
            # If it is, then we can skip this row, since it's not different
            if test_ID == Variablename:
                # We can store the Offset values found here, since we may need them later
                Temp_Offsets.append(USI_Data.loc[Current_Row + to_skip, "Offset"])
                # Fill the coordinates, scores, and offset values of this row with "Skip""
                USI_Data.loc[Current_Row + to_skip, "y1"] = "Skip"
                USI_Data.loc[Current_Row + to_skip, "y2"] = "Skip"
                USI_Data.loc[Current_Row + to_skip, "x1"] = "Skip"
                USI_Data.loc[Current_Row + to_skip, "x2"] = "Skip"
                USI_Data.loc[Current_Row + to_skip, "Score"] = "Skip"
                USI_Data.loc[Current_Row + to_skip, "Offset"] = 0
                to_skip = to_skip + 1
                # Move on to the next row
                continue
            # If on the other hand, the current ID is different to the previous one, this is our stop point
            else:
                # If Img is skipped, if the replicate is not finished (i.e. the offset is not 8), those offset values may need to carry forward
                if Colname == "Img-ID":
                    # If the current offset is 0, then it was the left over rows after an offset block was shunted with an image skip, so can be skipped
                    if USI_Data.loc[Current_Row, "Offset"] == 0:
                        #to_skip = to_skip + 1
                        pass
                    # If the current offset isn't the maximum offset, there are still spots left, so shunt the previous offset values along, replacing the final ones with 0s.
                    elif USI_Data.loc[Current_Row, "Offset"] != USI_Data["Offset"].max():
                        print("Shunting Offsets")
                        USI_Data.iloc[Current_Row:Current_Row+to_skip, USI_Data.columns.get_loc("Offset")] = 0
                        USI_Data.iloc[Current_Row+to_skip:Current_Row+(2*to_skip), USI_Data.columns.get_loc("Offset")] = Temp_Offsets
                        USI_Data.iloc[Current_Row+(2*to_skip):Current_Row+(3*to_skip), USI_Data.columns.get_loc("Offset")] = 0

                # For both Leaf skip and Img skip
                print("Skipped " + str(to_skip))
                Row = Row + to_skip
                print("Row " + str(Row))
                return(Row)


while True:
    # Retrieve metadata
    USI = USI_Data.loc[Current_Row, "Unique_Spot_ID"]
    ImgID = int(USI_Data.loc[Current_Row, "Img-ID"])
    PlantPerImgID = int(USI_Data.loc[Current_Row, "Plant-Per-Img-ID"])
    LeafID = int(USI_Data.loc[Current_Row, "Leaf-ID"])
    SpotID = int(USI_Data.loc[Current_Row, "Spot-ID"])
    Offset = int(USI_Data.loc[Current_Row, "Offset"])
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
    MetaData = "".join(str(e) for e in ["USI:", USI, ", PlantPerImgID:", PlantPerImgID, ", LeafID:", LeafID, ", Offset:", Offset, ", SpotID:", SpotID])
    cv.putText(img = Concat_Image, text = MetaData, org = (50, 160), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=8, color=(0, 0, 0),thickness=8)

    # Scale score key to width of image and append to the bottom.
    if scoring == True:
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

    # Select bounding box
    fromCenter, showCrosshair = False, False
    r = cv.selectROI("Concat Image", full_downsize, fromCenter)

    # Decide what to do next: ESC, or if score pressed, save score to USI_Data in Josh_Score column
    if scoring == True:
        print("Please press either ESC to exit or enter a score between 0 and 6.")
    else:
        print("Please press either ESC to exit or any other value to continue")

    break_out_flag = False

    while True:
        k = cv.waitKey(0)
        if k == 27: # Escape
            break_out_flag = True
            print("ESC Pressed")
            # Save and quit
            SaveAndQuit()
            break

        elif k == ord('m'): # missing leaf
            print("Skipping to next leaf")
            Current_Row = Skip_Spots(Current_Row, "Leaf-ID", LeafID)

        elif k == ord('n'): # skip to next image
            print("Skipping to next image")
            Current_Row = Skip_Spots(Current_Row, "Img-ID", ImgID)

        else:
            if scoring == True:
                if k in [ord('0'), ord('1'), ord('2'), ord('3'), ord('4'), ord('5'), ord('6')]: # if a score is pressed
                    print("Score given: " + str(chr(k)))
                    USI_Data.loc[Current_Row, "Josh_Score"] = chr(k) # save the score (chr is reverse of ord)
                else:
                    print("That did not work. Please press either ESC to exit or a score from 0 to 6.")
                    continue
            # Saving scaled coordinates
            y1 = int(r[1])
            y2 = int(r[1] + r[3])
            x1 = int(r[0])
            x2 = int(r[0] + r[2])

            # Remove from Up and Low the number of pixels added by the Metadata bar
            y1 -= Scale_Value * 200 # 200 is height of box
            y2 -= Scale_Value * 200

            # Scale these coordinates
            Coords = [y1/Scale_Value, x1/Scale_Value, y2/Scale_Value, x2/Scale_Value]

            # Make selection square
            SquareCoords = MakeSelectionSquare(Coords)

            # Store in USI_Data
            USI_Data.loc[Current_Row, "y1"] = SquareCoords[0]
            USI_Data.loc[Current_Row, "y2"] = SquareCoords[2]
            USI_Data.loc[Current_Row, "x1"] = SquareCoords[1]
            USI_Data.loc[Current_Row, "x2"] = SquareCoords[3]

            if Current_Row == len(USI_Data)-1:
                print("End of Dataframe!")
                # Clean up dataframe
                SaveAndQuit()
                break_out_flag = True
                break
            else:
                Current_Row += 1

        print("Current Row: ", str(Current_Row))
        # So that the image isn't always opened each loop - only if it is a new image
        PrevImagePath = ImagePath
        break

    if break_out_flag:
        break
