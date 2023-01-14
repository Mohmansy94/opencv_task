include <opencv2/opencv.hpp>

using namespace cv;

int main() {
    // Initialize variables for tasks
    bool save_frame = false;
    bool show_frame_number = false;
    bool show_mouse_coordinates = false;
    bool show_rectangle = false;
    int rectangle_width = 0;
    int rectangle_height = 0;
    int canny_threshold1 = 0;
    int canny_threshold2 = 0;

    // Create a window for the video stream
    namedWindow("Video Stream");

    // Create trackbars for rectangle width and height and canny threshold values
    createTrackbar("Rectangle Width", "Video Stream", &rectangle_width, 1000);
    createTrackbar("Rectangle Height", "Video Stream", &rectangle_height, 1000);
    createTrackbar("Canny Threshold1", "Video Stream", &canny_threshold1, 1000);
    createTrackbar("Canny Threshold2", "Video Stream", &canny_threshold2, 1000);

    // Open a video stream from a file or the camera
    VideoCapture cap("video.mp4");

    while (true) {
        // Capture a frame from the video stream
        Mat frame;
        cap >> frame;

        // Check if the video stream is over
        if (frame.empty()) {
            break;
        }

        // Task 01: Save frame when 's' is pressed
        char key = (char)waitKey(1);
        if (key == 's') {
            save_frame = true;
        }
        if (save_frame) {
            imwrite("C:/frame.jpg", frame);
            save_frame = false;
            std::cout << "Frame saved" << std::endl;
        }

        // Task 02: Show/hide frame number when 'i' is pressed
        if (key == 'i') {
            show_frame_number = !show_frame_number;
        }
        if (show_frame_number) {
            putText(frame, std::to_string(cap.get(CAP_PROP_POS_FRAMES)), Point(10, frame.rows - 10), FONT_HERSHEY_SIMPLEX, 0.5, Scalar(0, 0, 255), 2);
        }

        // Task 03: Show/hide mouse coordinates when 'p' is pressed
        if (key == 'p') {
            show_mouse_coordinates = !show_mouse_coordinates;
        }
        if (show_mouse_coordinates) {
            setMouseCallback("Video Stream", [](int event, int x, int y, int flags, void* userdata) {
                if (event == EVENT_MOUSEMOVE) {
                    putText(frame, "(" + std::to_string(x) + ", " + std::to_string(y) + ")", Point(10, frame.rows - 10), FONT_HERSHEY_SIMPLEX, 0.5, Scalar(0, 0, 255), 2);
                }
            });
        }

    // Task 04: Show/hide rectangle when 'r' is pressed
        if (key == 'r') {
            show_rectangle = !show_rectangle;
        }
        if (show_rectangle) {
            int center_x = frame.cols / 2;
            int center_y = frame.rows / 2;
            rectangle(frame, Point(center_x - rectangle_width / 2, center_y - rectangle_height / 2), Point(center_x + rectangle_width / 2, center_y + rectangle_height / 2), Scalar(0, 255, 0), 2);
        }

        // Task 05: Apply canny detector and show result when 'e' is pressed
        if (key == 'e') {
            Mat canny;
            Canny(frame, canny, canny_threshold1, canny_threshold2);
            imshow("Canny", canny);
        }

        // Show the frame
        imshow("Video Stream", frame);

        // Break the loop if the user presses 'q'
        if (key == 'q') {
            break;
        }
    }

    // Release the video capture and destroy all windows
    cap.release();
    destroyAllWindows();

    return 0;
}
