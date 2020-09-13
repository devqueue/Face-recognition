# Face Recognition using open-cv
This is a project that recognizes your face using webcam and adds your attandance to a csv file 
I used open-cv and face-recognition libraries. The faces must be saved in individual directories 
in `src/images`. There must be atleast 8-10 images for each face with clear features. Follow the 
steps below to get started.

## How to Install dependencies?
#### Using anaconda environment.yml (linux only)
The conda_environment.yml was created on a linux machine so I would recommend you not to use this unless you are on linux or if you can manually delete the linux dependencies that'll work fine as well 
1. Open conda_environment.yml
2. Replace the first line `name: FaceRec` to your prefered name
3. Replace 'user' with your username in `prefix: /home/user/.conda/envs/FaceRec`
4. cd into the folder
5. Now open terminal and run
`conda env create -f conda_environment.yml`

#### Using pip (For any OS)
1. Create a virtual environment 
2. Run `pip install -r requirements.txt`

## Setup for a new face
1. Go to src/images directory 
2. Create a directory with your name 
3. Add 8-10 images of your face in different lighiting conditions 
4. Now run `face-trainer.py`
Note: Everytime you add a new face you'll have to run this file again

## Final Recognition
Now you can run the `face-detect.py`. The script will recognize your face and add a time stamp
in `Attendance.csv`
