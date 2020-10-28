from shape_detection import square
from cv_tools.video import Video
from datetime import datetime
import numpy as np
import cv2


def shape_detection_filter(contours, hierarchy):
    """
    Go through the contours and return the squares
    """
    new_contour = []
    new_hierarchy = []
    for c in zip(contours, hierarchy):

        approx = square.is_square(c[0])

        if(type(approx) is square.Square):
            new_contour.append(approx.array)
            new_hierarchy.append(c[1])

    new_hierarchy = np.array(new_hierarchy)
    return new_contour, new_hierarchy


cap = Video(0, 480, 720)
video_capture = cap.select()

allContours = []
usedContours = []

while True:
    try:
        ret, frame = cap.read(video_capture)
    except Exception as e:
        print(e)
        break

    # Get Filtered Frame
    white, dilated = frame.filter_frame()

    # Get Contours
    contours, hierarchy = frame.get_contours(dilated)

    # Filter contours
    contour_filtered, hierarchy_filtered = shape_detection_filter(
        contours, hierarchy)

    # Draw contour one by one
    for index, contour in enumerate(contour_filtered):
        # Get bound of rectangle
        (x, y, w, h) = cv2.boundingRect(contour)

        # Draw Rectangle
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 255), 2)

        # Write in rectangle
        cv2.putText(frame, str(index), (int((x + (x+w))/2), int((y + (y+h))/2)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        # Get contour content
        content = frame[x:y, x+w:y+h]

    # Stats
    allContours.append(len(contours))
    usedContours.append(len(contour_filtered))

    cv2.putText(frame, str(len(contours)) + " Contours foud",
                (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    cv2.putText(frame, str(len(contour_filtered)) + ": Contours Used",
                (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

    # Show video
    cv2.imshow("Video", frame)
    cv2.imshow("dilated", dilated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print(str(sum(allContours)/len(allContours)) +
      ": Average contours per frame")
print(str(sum(usedContours)/len(usedContours)) +
      ": Average used contours per frame")

video_capture.release()
cv2.destroyAllWindows()
