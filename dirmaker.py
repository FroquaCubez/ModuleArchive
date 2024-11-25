import os

# Define the main directory and subdirectories
main_dir = 'grade8'
quarters = ['q1', 'q2', 'q3', 'q4']

# Define the subjects with their IDs
subjects = [
    {"name": "Araling Panlipunan", "id": "ap"},
    {"name": "English", "id": "english"},
    {"name": "Filipino", "id": "filipino"},
    {"name": "Science", "id": "science"},
    {"name": "Math", "id": "math"},
    {"name": "MAPEH", "id": "mapeh"},
    {"name": "Edukasyon sa Pagkatao", "id": "esp"},
    {"name": "Technology and Livelihood Education", "id": "tle"}
]

# Define additional folders inside the MAPEH folder
mapeh_subfolders = ['music', 'arts', 'pe', 'health']

# Create the main directory
os.makedirs(main_dir, exist_ok=True)

# Create subdirectories for each quarter and subject
for quarter in quarters:
    quarter_path = os.path.join(main_dir, quarter)
    os.makedirs(quarter_path, exist_ok=True)
    
    for subject in subjects:
        # Create a folder for each subject using its ID
        subject_folder_path = os.path.join(quarter_path, subject['id'])
        os.makedirs(subject_folder_path, exist_ok=True)

        # If the subject is MAPEH, create additional subfolders
        if subject['id'] == 'mapeh':
            for mapeh_subfolder in mapeh_subfolders:
                mapeh_subfolder_path = os.path.join(subject_folder_path, mapeh_subfolder)
                os.makedirs(mapeh_subfolder_path, exist_ok=True)

print("Directory layout created successfully!")