# Valeo DFC Applied Python Evaluation

This project is a Python-based evaluation provided by Valeo. Below is a quick overview of how to execute the project and a brief explanation of its functionality.

## How to Execute the Project

1. **Clone the Repository**:
    ```bash
    git clone <repository-url>
    cd Valeo-DFC-Applied-Python-Evaluation
    ```

2. **Set Up the Environment**:
    Ensure you have Python 3.x installed. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**:
    Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Project**:
    Execute the main script creating resim_out.csv:
    ```bash
    ./main.py
    ```
    or specifing output_path of recim_out.csv
    ```bash
    ./main.py specified_recim_output.csv
    ```
    or using scripts individually
    ```bash
    ./f_cam.py
    ./f_cam.py specified_f_cam_output.csv
    ```
    ```bash
    ./sensor.py
    ./sensor.py specified_sensor_output.csv
    ```
    ```bash
    ./recim.py # Considering the f_cam_out.csv && camera_out.csv are in the same directory with default names
    ./recim.py specified_recim_output.csv specified_f_cam_input.csv specified_camera_input.csv 
    ```
   


