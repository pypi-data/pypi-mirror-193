import sys, os, subprocess, getopt
import pandas as pd
import cv2 as cv
import numpy as np

def saveandquit(input_loc, output_loc, dataframe):
    # Function to save to output location and close the tool
    os.rename(input_loc, "backup_" + input_loc) # Keep a backup of the previous version incase of user error
    cdata.to_csv(output_loc, index=False)
    cv.destroyAllWindows() # Close the windows

def query(input_loc, output_loc, images, scoring):

    # Make sure all columns are loaded
    pd.set_option("display.max_colwidth", None)

    # Load cdata and imagedata
    cdata = pd.read_csv(input_loc)
    cdata["Query"] = np.nan
    cdata["Rescore"] = np.nan
    image_paths = pd.read_csv(image_loc)
    previmg = ""

    if scoring == True:
        key = cv.imread(cv.samples.findFile(r"Lesion_Score_Key.tif")) # Need to add Lesion Score Key to PyPI files.

    # Identify next row with no coordinates and retrieve related data
    for row in range(0, len(cdata["Query"])):
        if pd.isna(cdata.loc[row, "Query"]) == True:
            currentrow = row
            break

    # Loop through cdata, presenting the corresponding image and metadata in a window, in which the user can drag coordinates around individual CDAs and optionally score them.
    while True:

        # Retrieve metadata
        usi = cdata.loc[currentrow, "Unique_Spot_ID"]
        imgid = int(cdata.loc[currentrow, "Img-ID"])
        plantperimgid = int(cdata.loc[currentrow, "Plant-Per-Img-ID"])
        leafid = int(cdata.loc[currentrow, "Leaf-ID"])
        spotid = int(cdata.loc[currentrow, "Spot-ID"])
        offset = int(cdata.loc[currentrow, "Offset"])

        # Check if current imgid is same as previous - if not, load current imgid
        imgpath = image_paths.loc[image_paths["Img-ID"] == imgid, "Path"].to_string(index = False)
        if imgpath != previmg:
            img = cv.imread(cv.samples.findFile(imgpath))

        if img is None:
            print("Could not read image: " + imgpath)

        # Add space to the top containing current row metadata needed to identify a CDA
        metadatabar = np.full((200, img.shape[1], 3), 255, dtype=np.uint8)
        imgwithmetadata = np.concatenate((metadatabar, img))
        metadatatext = "".join(str(e) for e in ["USI:", usi, ", PlantPerImgID:", plantperimgid, ", LeafID:", leafid, ", Offset:", offset, ", SpotID:", spotid])
        cv.putText(img = imgwithmetadata, text = metadatatext, org = (50, 160), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=8, color=(0, 0, 0),thickness=8)

        # Append score key to bottom if scoring option chosen
        if scoring == True:
            scorescale = key.shape[1] / imgwithmetadata.shape[1]
            keydimensions = (int(key.shape[1]/scorescale), int(key.shape[0]/scorescale))
            scaledkey = cv.resize(key, keydimensions)
            imgwithmetadata = np.concatenate((imgwithmetadata, scaledkey))

        # Scale image down (large images take very long to load)
        scaleval = 0.25
        dim = (int(imgwithmetadata.shape[1]*scaleval), int(imgwithmetadata.shape[0]*scaleval))
        scaledfinalimg = cv.resize(imgwithmetadata, dim)

        # Display image and bring to front
        cv.imshow("Cell Death Area Coordinate and Scoring Tool", scaledfinalimg)
        cv.setWindowProperty("Cell Death Area Coordinate and Scoring Tool", cv.WND_PROP_TOPMOST, 1)

        # Select bounding box
        fromCenter = False
        boundingbox = cv.selectROI("Cell Death Area Coordinate and Scoring Tool", scaledfinalimg, fromCenter)

        # Message for next steps
        if scoring == True:
            print("Please press either ESC to exit or enter a score between 0 and 6.")
        else:
            print("Please press either ESC to exit or any other value to continue")

        break_out_flag = False # Because there is a nested while loop here, need this method to break out

        while True:
            keypress = cv.waitKey(0)
            if keypress == 27: # Escape
                print("ESC Pressed")
                saveandquit(input_loc, output_loc, dataframe)
                break_out_flag = True
                break

            elif keypress == ord('q'): # Query Score
                print("Score queried")
                cdata.loc[currentrow, "Query"] = 1

                keyrescore = cv.waitKey(0)
                if keyrescore in [ord('0'), ord('1'), ord('2'), ord('3'), ord('4'), ord('5'), ord('6')]: # if a score is pressed
                    print("Score given: " + str(chr(keyrescore)))
                    cdata.loc[currentrow, "Rescore"] = chr(keyrescore) # save the score (chr is reverse of ord)
                else:
                    print("That did not work. Please press either ESC to exit or a score from 0 to 6.")
                    continue

            else:
                cdata.loc[currentrow, "Query"] = 0
                # If end of dataframe reached, save and quit, else move to next row
                if currentrow == len(cdata)-1:
                    print("End of Dataframe!")
                    saveandquit(input_loc, output_loc, dataframe)
                    break_out_flag = True
                    break
                else:
                    currentrow += 1
                    print("Current Row: ", str(currrentrow), "/", str(len(cdata)))

        previmg = imgpath

        if break_out_flag:
            break
