# DLT_Pipelines
Procedure: Creating and Running a DLT Pipeline

#### 1. Installations
   a. Follow the DLT Installation Guide ([Installation Guide Link](https://dlthub.com/docs/reference/installation)).
   b. Ensure Python 3.8-3.11 is installed and 'pip' is available:
      ```
      python --version
      pip --version
      ```
   c. If Python or 'pip' is not installed, follow the platform-specific installation guides provided in the DLT Documentation.

#### 2. Set Up Environment
   a. Create a virtual environment to manage dependencies:
      - **Ubuntu / macOS**
        ```
        python3 -m venv env
        source env/bin/activate
        ```
      - **Windows**
        ```
        python -m venv env
        .\env\Scripts\activate
        ```

#### 3. DLT Library Installation
   a. Install the DLT library within your virtual environment:
      ```
      pip install -U dlt
      ```

#### 4. DLT Pipeline Creation
   a. Prepare DLT pipelines using the tutorial provided ([Tutorial Link](https://dlthub.com/docs/build-a-pipeline-tutorial)).
   b. Here we utilized three different approaches:
      - **DLT_Pipeline**: Python notebook created using Jupyter Notebook.
      - **DLT_Pipeline_2**: Python notebook created using Google Colab.
      - **DLT_Pipeline_3**: Python script executed from the command prompt in a virtual environment.

#### 5. Running the DLT Pipelines
   a. Execute the pipelines:
      - **DLT_Pipeline**: Run within Jupyter Notebook.
      - **DLT_Pipeline_2**: Run within Google Colab environment.
      - **DLT_Pipeline_3**: Run using a `.py` file by activating the virtual environment and running the script from the command prompt.



### Note:
- Ensure Python and 'pip' are correctly installed as per the DLT requirements.
- Activate the virtual environment before installing or running the DLT library.
- The three pipeline approaches demonstrate the versatility of DLT usage across different environments.
