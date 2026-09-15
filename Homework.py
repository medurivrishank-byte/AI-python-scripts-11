import cv2
import numpy as np
def apply_color_filter(image,filter_type):
    filtered_image=image.copy()
    if filter_type=="red_tint":
        filtered_image[:,:,1]=0 #green channel to 0
        filtered_image[:,:,0]=0 #blue channel to 0
    elif filter_type=="blue_tint":
        filtered_image[:,:,1]=0 #green channel to 0
        filtered_image[:,:,2]=0 #red channel to 0
    elif filter_type=="green_tint":
        filtered_image[:,:,0]=0 #blue channel to 0
        filtered_image[:,:,2]=0 #red channel to 0
    elif filter_type=="increase_red":
        filtered_image[:,:,2]=cv2.add(filtered_image[:,:,2],50) #red channel incresed by 50
    elif filter_type=="decrease_blue":
        filtered_image[:,:,0]=cv2.subtract(filtered_image[:,:,0],50) #blue channel decresed by 50
    elif filter_type=="increase_green":
        filtered_image[:,:,1]=cv2.add(filtered_image[:,:,1],50) #red channel incresed by 50
    elif filter_type=="decrease_red":
        filtered_image[:,:,2]=cv2.subtract(filtered_image[:,:,2],50) #blue channel decresed by 50
    return filtered_image

image_path='example.jpeg'
image=cv2.imread(image_path)
if image is None:
    print("Error: Image not found!")
else:
    filter_type="original"
    print("Press the following key to apply the filters:")
    print("r: Red Tint")
    print("b: Blue Tint")
    print("g: Green Tint")
    print("i: Increase Red Intensity")
    print("d: Decrease Blue Intensity")
    print("up arrow: increase green")
    print("down arrow: decrease green")
    print("q: for quit")
    while True:
        filtered_image=apply_color_filter(image,filter_type)
        cv2.imshow("Filtered image",filtered_image)
        key=cv2.waitKey(0) & 0xFF
        if key==ord('r'):
            filter_type="red_tint"
        elif key==ord('b'):
            filter_type="blue_tint"
        elif key==ord('g'):
            filter_type="green_tint"
        elif key==ord('i'):
            filter_type="increase_red"
        elif key==ord('d'):
            filter_type="decrease_blue"
        elif key==ord('↑'):
            filter_type="increase_green"
        elif key==ord('↓'):
            filter_type="decrease_red"
        elif key==ord('q'):
            print("Exiting...")
            break
        else:
            print("Invalid key. Please use 'r','b','g','i','d', up arrow, down arrow or 'q'")

cv2.destroyAllWindows()