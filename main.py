import cv2
import os

img = cv2.imread("app_icon.svg", 1)
assert img, "Failed to read image"
output_folder = "icons"

resolutions = (20, 29, 40, 60, 76, 83.5, 1024)

if not os.path.isdir(output_folder):
    os.mkdir(output_folder)

for resolution in resolutions:
    for scale in range(1, 4):
        fname = f"Icon-App-{resolution}x{resolution}@{scale}x.png"
        print(f"Generating {fname}")
        output_path = os.path.join(output_folder, fname)

        size = float(resolution * scale)
        if not size.is_integer():
            continue
        size = int(size)
        
        img_rescaled = cv2.resize(img, (size, size))
        cv2.imwrite(output_path, img_rescaled)


