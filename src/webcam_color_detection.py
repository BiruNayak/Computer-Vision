import cv2 as cv
import numpy as np
import csv

# Load colors from CSV
def load_colors_from_csv(csv_path):
    colors = []
    with open(csv_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header
        for row in reader:
            color_name = row[0]
            r, g, b = int(row[2]), int(row[3]), int(row[4])  # RGB
            colors.append((color_name, (b, g, r)))  # Store in BGR for OpenCV
    return colors

# Find closest color name
def get_closest_color_name(b, g, r, colors):
    min_dist = float('inf')
    closest_name = "Unknown"
    for name, (cb, cg, cr) in colors:
        dist = np.sqrt((int(b) - int(cb))**2 + (int(g) - int(cg))**2 + (int(r) - int(cr))**2)
        if dist < min_dist:
            min_dist = dist
            closest_name = name
    return closest_name

# Mouse callback function
def mouse_click(event, x, y, flags, param):
    global click_info
    if event == cv.EVENT_LBUTTONDOWN:
        frame, colors = param
        b, g, r = frame[y, x]
        color_name = get_closest_color_name(b, g, r, colors)
        click_info = (x, y, b, g, r, color_name)

# Load CSV and initialize webcam
colors = load_colors_from_csv("../Dataset/csv/colors.csv")  # Replace with actual path
cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

cv.namedWindow("Color Detector")

click_info = None  # Store last click info

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame.")
        break

    img_copy = frame.copy()

    # Show quit instruction
    cv.putText(img_copy, "Press 'Q' to Quit", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    # Display last clicked color info
    if click_info:
        x, y, b, g, r, name = click_info
        text = f"{name} ({b}, {g}, {r})"
        cv.putText(img_copy, text, (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        cv.rectangle(img_copy, (int(x), int(y)), (int(x) + 100, int(y) + 40), (int(b), int(g), int(r)), -1)

    # Update mouse callback with latest frame and color list
    cv.setMouseCallback("Color Detector", mouse_click, param=(frame, colors))

    # Show result
    cv.imshow("Color Detector", img_copy)

    # Exit on 'q'
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
