import cv2
import numpy as np

def convolve_direct(image, kernel):
    rows, cols = image.shape
    k = len(kernel)
    pad = k // 2

    padded = np.pad(image, ((pad, pad), (pad, pad)), mode='constant')

    output = np.zeros((rows, cols), dtype=np.int32)

    for i in range(rows):
        for j in range(cols):

            value = 0

            for x in range(k):
                for y in range(k):
                    value += padded[i + x][j + y] * kernel[x][y]

            value = max(0, min(255, int(value)))
            output[i][j] = value

    return output.astype(np.uint8)


def process_color_image(img, kernel):
    b, g, r = cv2.split(img)

    b_out = convolve_direct(b, kernel)
    g_out = convolve_direct(g, kernel)
    r_out = convolve_direct(r, kernel)

    return cv2.merge((b_out, g_out, r_out))


def main():
    filters = [
        [[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]],  # Blur
        [[0,-1,0],[-1,5,-1],[0,-1,0]],               # Sharpen
        [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]            # Edge
    ]

    img = cv2.imread("image.jpg")

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

            final = process_color_image(img, kernel)

            cv2.imshow("Final Image", final)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        except ValueError:
            print("Enter valid number")

    print("Done ")


if __name__ == "__main__":
    main()