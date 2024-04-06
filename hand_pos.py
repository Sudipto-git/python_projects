import cv2
import mediapipe as mp


# Initialize MediaPipe Hand model
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)

cam_index = 1 # Set the camera index
# Initialize the webcam
cap = cv2.VideoCapture(cam_index)

while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1) # Flip the frame horizontally
    if not ret:
        break
    # Detect hand keypoints
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]
        hand_landmarks = hand_landmarks.landmark[8] # Select the landmark for the tip of the index finger
        x = int(hand_landmarks.x*frame.shape[1]) # Convert the x-coordinate to the frame's width
        y = int(hand_landmarks.y*frame.shape[0]) # Convert the y-coordinate to the frame's height
        cv2.circle(frame, (int(x), int(y)), 5, (0, 255, 0), -1)
        
        
    cv2.imshow("hand pos", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break