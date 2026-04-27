import cv2
import numpy as np

def main():

    filters = [
        [[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]],
        [[0,-1,0],[-1,5,-1],[0,-1,0]],
        [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]
    ]
    output_image = {1:"Blur.jpg", 2:"Sharpen.jpg", 3:"Edge Detection.jpg"}
    img = cv2.imread("Itachi.jpeg")

    if img is None:
        print("Error loading image")
        return

    while True:
        try:
            choice = int(input(
                "\n1. Blur\n2. Sharpen\n3. Edge Detection\n4. Exit\n>> "
            ))

            if choice == 4:
                break

            if choice not in [1, 2, 3]:
                print("Invalid choice")
                continue

            kernel = np.array(filters[choice - 1], dtype=np.float32)

            final = cv2.filter2D(img, -1, kernel, borderType=cv2.BORDER_REFLECT)

            cv2.imshow("Final Image", final)
            cv2.waitKey(0)
            cv2.imwrite(output_image[choice],final)

        except ValueError:
            print("Enter valid number")

    print("Done ")


if __name__ == "__main__":
    main()