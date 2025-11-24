● RIDS CHEMISTRY INPUT BUILDER APP

● Overview of the project: A new era of quantum chemistry research is being shaped by the development of Python GUI-based applications, and the Input Builder App exemplifies this innovation. 
Traditionally, chemists have relied on text editors or command-line tools to generate input files for quantum chemistry software, making the process time-consuming and prone to errors. 
The Input Builder App addresses this gap by providing an intuitive, user-friendly interface designed specifically for the quantum chemistry community.
Unlike most existing solutions, this app allows users to input data and instantly receive outputs in multiple formats, facilitating seamless transfer to quantum chemistry packages such as ChemCompute, GAMESS, or PSI4.
Its multi-format support streamlines workflow and significantly reduces the learning curve for new users, while also catering to advanced needs through flexible output options. 
By consolidating data entry, validation, and format conversion into a single tool, the Input Builder App empowers researchers and students to focus more on scientific exploration and less on technical formatting tasks. 
As Python and GUI frameworks continue to gain traction in the computational chemistry domain, tools like this app are paving the way for more accessible and efficient.

● Features:

1)File Input Handling
Allows users to select and open molecular coordinate input files via a file dialog.
Reads coordinate data and number of atoms from the file and displays it.

2)Interactive Parameter Input
Provides a graphical interface with dropdowns and entry fields for run type, SCF type, molecular charge, multiplicity, basis sets, and other calculation options.
Supports selection of point group symmetry and optimization flags.

3)Dynamic Input File Generation
Constructs input scripts dynamically based on user parameters for multiple quantum chemistry suites like GAMESS and PSI4.
Enables generation of calculation sections like CONTROL, SCF, BASIS, and DATA blocks according to specified options.

4)Multi-format Output Support
Supports saving generated input scripts in multiple output formats compatible with different quantum chemistry software.

5)Preview and Display
Displays the full generated input script in the GUI for user review.
Shows summary information such as the number of atoms and input title within the app.

6)Error Handling
Includes exception handling to catch and report errors occurring during file load or processing to the user in the GUI.

7)User-Friendly GUI
Built using Tkinter for cross-platform compatibility.
Intuitive button, label, and entry placements for smooth user interaction.
Allows resetting inputs and easy navigation.

● Technologies/tools used :

1)Python Programming Language

2)Tkinter GUI Framework

3)File Handling and Dialogs

4)String Formatting and Processing

5)Cross-platform Compatibility


● Steps to install & run the project 

Installation Steps:

1)Install Python
Download and install Python (version 3.6 or above) from the official website

2)Install Required Python Packages
If Tkinter is missing (on some Linux systems), install it via your package manager.

3)Get the Project Code

4)Running the Project

 i)Run the Main Python Script
   Execute the main script that launches the Tkinter GUI.
   
 ii)Use the GUI:
   The graphical interface will open.
   Use buttons to open input coordinate files.
   Enter parameters in the provided fields.
   Generate and save input files according to your workflow.


● Instructions for testing :

1)Setup Testing Environment
 Ensure Python and Tkinter are properly installed as per installation instructions.
 Open a terminal or command prompt and navigate to the project directory.
 
2)Launch the Application
 Run the main script. 
 Confirm the GUI window opens without errors.
 
3)File Load Tests
 Use the "Open File" button to load sample coordinate input files ( .xyz).
 Verify that:
 
  i)The number of atoms is correctly displayed.
  
  ii)The input coordinate data is displayed in the output area.
  
  iii)Invalid or malformed files show appropriate error messages.
  
4)Parameter Input Tests
 Enter values into each parameter field (run type, SCF, charge, multiplicity, basis sets, etc.).
 Test selection options in the dropdown menus.
 Verify fields accept expected inputs and reject invalid entries (e.g., non-numeric where numeric expected).
 
5)Input Generation Tests
 After entering parameters, trigger input generation (via generate or save buttons).
 Check:
 
  i)The generated input text preview corresponds correctly to the selected options.
  
  ii)The output conforms to expected syntax of target quantum chemistry software.
  
6)File Save Tests

 i)Save generated input files to disk.
 
 ii)Confirm files are properly saved with user-specified names and extensions.
 
 iii)Open saved files in an editor to verify the content correctness.
 
7)GUI Behavior Tests

 i)Test resetting inputs and clearing displayed outputs.
 
 ii)Verify UI responsiveness and that no crashes occur during typical workflows.
 
 iii)Test cancel or close buttons and confirm graceful exit.
 
8)Edge Case and Error Handling

 i)Try opening non-supported or corrupted files.
 
 ii)Input boundary values (very large numbers, empty fields).
 
 iii)Observe error messages and stability.


● Screenshots 

Input Code:

Initialization
<img width="1637" height="469" alt="image" src="https://github.com/user-attachments/assets/10816bc2-5adf-4e00-92c8-92758fbff71b" />
Functions
<img width="913" height="655" alt="image" src="https://github.com/user-attachments/assets/db7e64f9-4056-4c31-9d84-4c1b5b700321" />
<img width="1634" height="655" alt="image" src="https://github.com/user-attachments/assets/1ff25b9f-3c8f-4124-bdec-cec63835cc43" />
<img width="702" height="667" alt="image" src="https://github.com/user-attachments/assets/92f1b658-3b9f-43df-a0dd-e2a3fdd99b1b" />
<img width="988" height="667" alt="image" src="https://github.com/user-attachments/assets/e40977ab-3c93-4350-8485-02f591e361b2" />
<img width="966" height="650" alt="image" src="https://github.com/user-attachments/assets/92eeb47c-687d-4f1a-aeea-8628c8544830" />
<img width="930" height="650" alt="image" src="https://github.com/user-attachments/assets/5c88bc88-2a74-404d-8a68-da8e55632428" />
<img width="928" height="665" alt="image" src="https://github.com/user-attachments/assets/0e8ca12a-0087-4a9f-8297-f3bfd1e660ea" />
<img width="917" height="665" alt="image" src="https://github.com/user-attachments/assets/5a896ef2-78b9-4e78-b48a-924355b5fd6e" />
<img width="898" height="591" alt="image" src="https://github.com/user-attachments/assets/924e612c-6b22-4b4a-9833-88949550f3c7" />
<img width="851" height="591" alt="image" src="https://github.com/user-attachments/assets/24d32c97-a35a-46b8-8c23-98f221283694" />
<img width="1138" height="729" alt="image" src="https://github.com/user-attachments/assets/2a5f9fe5-3223-438e-a22b-b85127371cc3" />
<img width="1158" height="697" alt="image" src="https://github.com/user-attachments/assets/af2070e8-63e2-4a41-b04b-92e28b6fcac5" />
<img width="624" height="728" alt="image" src="https://github.com/user-attachments/assets/e4a2b57f-d438-4a09-8d85-8a463c58fe18" />
<img width="624" height="721" alt="image" src="https://github.com/user-attachments/assets/49d432eb-ee21-44dc-bc5c-9fb031fbc795" />
<img width="1111" height="715" alt="image" src="https://github.com/user-attachments/assets/3f69e94c-8b17-47f9-b170-87332a6b5d26" />
<img width="699" height="723" alt="image" src="https://github.com/user-attachments/assets/c0d6fbef-9b72-4816-9199-73b56a21b18d" />
<img width="580" height="724" alt="image" src="https://github.com/user-attachments/assets/2f8c1ebd-caa4-42cb-bd3f-90a33d3314cd" />
<img width="735" height="731" alt="image" src="https://github.com/user-attachments/assets/417f3ed4-726d-4505-a24e-b996ab1deb1c" />
<img width="1698" height="508" alt="image" src="https://github.com/user-attachments/assets/580bbccc-aa67-4493-b047-3e6a58a4a5b0" />
<img width="1295" height="731" alt="image" src="https://github.com/user-attachments/assets/93b9809e-5ed8-4bc9-9c7d-8ecbadeb0a13" />
<img width="1673" height="516" alt="image" src="https://github.com/user-attachments/assets/4cf3ab95-a430-406a-a582-8edb5da70b5d" />
<img width="1227" height="736" alt="image" src="https://github.com/user-attachments/assets/c0937200-0608-4806-9699-f57274f2ecb9" />
Variables:
<img width="1000" height="476" alt="image" src="https://github.com/user-attachments/assets/56374970-a2e6-4ed9-a447-8d6c77b616ee" />
Frames:
<img width="1530" height="293" alt="image" src="https://github.com/user-attachments/assets/65fe3114-9b7f-4615-8b0d-852f10646d01" />
Buttons
<img width="1561" height="577" alt="image" src="https://github.com/user-attachments/assets/6ad8c950-3ebf-4eb7-b798-321185beb939" />
Logos and Images:
<img width="1408" height="526" alt="image" src="https://github.com/user-attachments/assets/16cac3c4-e5f6-4585-8c36-bd58d360964f" />



Output:
Main Window
<img width="1446" height="721" alt="image" src="https://github.com/user-attachments/assets/071502b7-307b-4547-ab5a-d146322ae150" />
Basis Button Page
<img width="1445" height="715" alt="image" src="https://github.com/user-attachments/assets/865e5763-0d09-40ce-827f-4f07383905eb" />
Control Button Page
<img width="1447" height="719" alt="image" src="https://github.com/user-attachments/assets/b59a1fb8-9a6f-41a5-b7fd-7bf5f8632374" />
Data Button Page
<img width="1443" height="723" alt="image" src="https://github.com/user-attachments/assets/4c65a95a-6c9d-46d9-a330-74e238ef7182" />
System Button Page
<img width="1450" height="718" alt="image" src="https://github.com/user-attachments/assets/04809bb5-8526-4486-8316-f6ede351d418" />
SCF Options Button Page
<img width="1445" height="721" alt="image" src="https://github.com/user-attachments/assets/21e57f55-b7b2-475e-b150-de5b8643ff68" />
Summary Button Page
<img width="1442" height="720" alt="image" src="https://github.com/user-attachments/assets/59ed927c-61dd-4f70-88f9-47dc7c1acf44" />






