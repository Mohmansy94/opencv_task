import cv2

# Initialize variables for tasks
save_frame = False
show_frame_number = False
show_mouse_coordinates = False
show_rectangle = False
rectangle_width = 0
rectangle_height = 0
canny_threshold1 = 0
canny_threshold2 = 0

# Create a window for the video stream
cv2.namedWindow("Video Stream")

# Create trackbars for rectangle width and height and canny threshold values
cv2.createTrackbar("Rectangle Width", "Video Stream", 0, 1000, lambda x: None)
cv2.createTrackbar("Rectangle Height", "Video Stream", 0, 1000, lambda x: None)
cv2.createTrackbar("Canny Threshold1", "Video Stream", 0, 1000, lambda x: None)
cv2.createTrackbar("Canny Threshold2", "Video Stream", 0, 1000, lambda x: None)

# Open a video stream from a file or the camera
cap = cv2.VideoCapture("video.mp4")

while True:
    # Capture a frame from the video stream
    ret, frame = cap.read()

    # Check if the video stream is over
    if not ret:
        break

    # Get the current values of the trackbars
    rectangle_width = cv2.getTrackbarPos("Rectangle Width", "Video Stream")
    rectangle_height = cv2.getTrackbarPos("Rectangle Height", "Video Stream")
    canny_threshold1 = cv2.getTrackbarPos("Canny Threshold1", "Video Stream")
    canny_threshold2 = cv2.getTrackbarPos("Canny Threshold2", "Video Stream")

    # Task 01: Save frame when 's' is pressed
    if cv2.waitKey(1) & 0xFF == ord('s'):
        save_frame = True
    if save_frame:
        cv2.imwrite("C:/frame.jpg", frame)
        save_frame = False
        print("Frame saved")

    # Task 02: Show/hide frame number when 'i' is pressed
    if cv2.waitKey(1) & 0xFF == ord('i'):
        show_frame_number = not show_frame_number
    if show_frame_number:
        cv2.putText(frame, str(cap.get(cv2.CAP_PROP_POS_FRAMES)), (10, frame.shape[0]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Task 03: Show/hide mouse coordinates when 'p' is pressed
    if cv2.waitKey(1) & 0xFF == ord('p'):
        show_mouse_coordinates = not show_mouse_coordinates
    if show_mouse_coordinates:
        cv2.setMouseCallback("Video Stream", lambda event, x, y, flags, param: cv2.putText(frame, f"({x}, {y})", (10, frame.shape[0]-10), cv2.FONT_HERSHEY_SIM
    # Task 04: Show/hide rectangle when 'r' is pressed
    if cv2.waitKey(1) & 0xFF == ord('r'):
        show_rectangle = not show_rectangle
    if show_rectangle:
        center_x = int(frame.shape[1]/2)
        center_y = int(frame.shape[0]/2)
        cv2.rectangle(frame, (center_x-int(rectangle_width/2), center_y-int(rectangle_height/2)), (center_x+int(rectangle_width/2), center_y+int(rectangle_height/2)), (0, 255, 0), 2)

    # Task 05: Apply canny detector and show result when 'e' is pressed
    if cv2.waitKey(1) & 0xFF == ord('e'):
        cv2.imshow("Canny", cv2.Canny(frame, canny_threshold1, canny_threshold2))

    # Show the frame
    cv2.imshow("Video Stream", frame)

    # Break the loop if the user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and destroy all windows
cap.release()
cv2.destroyAllWindows()
