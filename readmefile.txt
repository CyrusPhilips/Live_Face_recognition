# Live Face Recognition using OpenCV and DeepFace

This Python script captures video from a webcam and performs live face recognition using OpenCV and DeepFace. It compares each frame with a reference image to determine whether there's a match or not.

** Requirements

- Python 3.x
- OpenCV (`opencv-python`)
- DeepFace (`deepface`)

Install the required packages using pip:


* Usage

1. Clone the repository:


2. Navigate to the project directory:


3. Ensure your webcam is connected and run the script:


4. Press 'q' to quit the program.

* Configuration

- Set the path to the reference image in the `REFERENCE_IMG_PATH` variable in the script.
- Adjust webcam frame dimensions as needed in the `main()` function.

* License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

* Acknowledgements

- DeepFace: [DeepFace GitHub](https://github.com/serengil/deepface)
- OpenCV: [OpenCV Documentation](https://docs.opencv.org/)
