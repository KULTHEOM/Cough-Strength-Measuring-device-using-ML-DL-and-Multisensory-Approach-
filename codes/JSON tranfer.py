import os
import json
import shutil


source_folder = "C:/Users/OM/Desktop/VLSID/archive" 
destination_folder = "C:/Users/OM/Desktop/Anvesshan/Final_audio_files"

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

target_datetime ="2020-05-14 10:46:15.883301+00:00"

files = os.listdir(source_folder)

for i, filename in enumerate(files):
    if filename.endswith('.json'):
        json_file_path = os.path.join(source_folder, filename)

        try:
            # Open and load the JSON file
            with open(json_file_path, 'r') as f:
                data = json.load(f)
            print(f"Processing file: {filename}")
            print(f"Datetime in JSON: {data.get('datetime')}")

            # Check if 'datetime' key exists and matches the target
            if 'datetime' in data and data['datetime'] == target_datetime:
                # Copy the JSON file
                shutil.copy(json_file_path, destination_folder)
                print(f"JSON file copied: {filename}")
                # Check if there's a next file and if it's WEBM or OGG format
                if i + 1 < len(files):
                    next_file = files[i + 1]
                    print(f"Next file: {next_file}")  # Debug: Print next file name
                    if next_file.endswith('.webm') or next_file.endswith('.ogg'):
                        media_file_path = os.path.join(source_folder, next_file)
                        shutil.copy(media_file_path, destination_folder)
                        print(f"Media file copied: {next_file}")
                    else:
                        print(f"No media file found right after {filename}")
                else:
                    print(f"No media file after {filename}")
                
        except json.JSONDecodeError:
            print(f"Error: {filename} is not a valid JSON file.")
        except Exception as e:
            print(f"Unexpected error with file {filename}: {e}")

print(f"Operation completed. Files with matching datetime and corresponding media files have been copied to {destination_folder}.")





# import os
# import json
# import shutil
# import pandas as pd
# from datetime import datetime

# def print_debug_info(json_data, target_datetime):
#     print("/nDebug Info:")
#     print(f"Target datetime: '{target_datetime}'")
#     print(f"JSON datetime: '{json_data.get('datetime', 'Not found')}'")
#     print(f"Types - Target: {type(target_datetime)}, JSON: {type(json_data.get('datetime', ''))}")
#     print(f"Length - Target: {len(str(target_datetime))}, JSON: {len(str(json_data.get('datetime', '')))}")
#     print("Are they equal?", target_datetime == json_data.get('datetime', ''))
#     print("-" * 50)

# def copy_files_for_datetime(source_folder, destination_folder, target_datetime, files):
#     found_match = False
    
#     print(f"/nSearching for files matching datetime: {target_datetime}")
#     print(f"Number of files to check: {len(files)}")
#     print(f"Source folder: {source_folder}")
#     print(f"Destination folder: {destination_folder}")
    
#     for i, filename in enumerate(files):
#         if filename.endswith('.json'):
#             json_file_path = os.path.join(source_folder, filename)
            
#             try:
#                 # Open and load the JSON file
#                 with open(json_file_path, 'r') as f:
#                     data = json.load(f)
                
#                 print(f"/nProcessing file: {filename}")
#                 json_datetime = data.get('datetime', '')
                
#                 # Print debug info
#                 print_debug_info(data, target_datetime)
                
#                 # Strip any whitespace and ensure exact match
#                 if json_datetime and json_datetime.strip() == target_datetime.strip():
#                     found_match = True
#                     print(f"Match found in file: {filename}")
                    
#                     # Copy the JSON file
#                     try:
#                         shutil.copy2(json_file_path, destination_folder)
#                         print(f"Successfully copied JSON file: {filename}")
#                     except Exception as e:
#                         print(f"Error copying JSON file: {e}")
                    
#                     # Check for and copy associated audio file
#                     if i + 1 < len(files):
#                         next_file = files[i + 1]
#                         if next_file.endswith(('.webm', '.ogg')):
#                             media_file_path = os.path.join(source_folder, next_file)
#                             try:
#                                 shutil.copy2(media_file_path, destination_folder)
#                                 print(f"Successfully copied media file: {next_file}")
#                             except Exception as e:
#                                 print(f"Error copying media file: {e}")
#                         else:
#                             print(f"No valid media file found after {filename}")
                    
#             except json.JSONDecodeError:
#                 print(f"Error: {filename} is not a valid JSON file.")
#             except Exception as e:
#                 print(f"Unexpected error with file {filename}: {e}")
    
#     if not found_match:
#         print("No matching files found for this datetime!")

# def main():
#     # Define paths
#     source_folder = "C:/Users/OM/Desktop/VLSID/archive"
#     destination_folder = "C:/Users/OM/Desktop/Anvesshan/Final_audio_files"
#     csv_path = "C:/Users/OM/Desktop/Anvesshan/newdataset.csv"
    
#     # Verify paths exist
#     print("/nChecking paths...")
#     print(f"Source folder exists: {os.path.exists(source_folder)}")
#     print(f"CSV file exists: {os.path.exists(csv_path)}")
    
#     # Create destination folder if it doesn't exist
#     if not os.path.exists(destination_folder):
#         try:
#             os.makedirs(destination_folder)
#             print(f"Created destination folder: {destination_folder}")
#         except Exception as e:
#             print(f"Error creating destination folder: {e}")
#             return
    
#     try:
#         # Read CSV file
#         df = pd.read_csv(csv_path)
#         print(f"/nSuccessfully read CSV file. Found {len(df)} rows")
        
#         # Get datetime values
#         datetime_values = df['datetime'].head(50).tolist()
#         print(f"First datetime value in CSV: {datetime_values[0]}")
        
#         # Get list of files
#         files = sorted(os.listdir(source_folder))
#         print(f"Number of files in source folder: {len(files)}")
#         print(f"First few files: {files[:5]}")
        
#         # Process each datetime value
#         for datetime_value in datetime_values:
#             print(f"/nProcessing datetime: {datetime_value}")
#             copy_files_for_datetime(source_folder, destination_folder, str(datetime_value), files)
        
#         # Final check
#         copied_files = os.listdir(destination_folder)
#         print(f"/nFiles in destination folder: {len(copied_files)}")
#         if copied_files:
#             print("First few copied files:", copied_files[:5])
#         else:
#             print("No files were copied!")
        
#     except Exception as e:
#         print(f"Error in main process: {e}")

# if __name__ == "__main__":
#     main()


# import os
# import json
# import shutil
# import pandas as pd

# def copy_files_for_datetime(source_folder, destination_folder, target_datetime, files):
#     for i, filename in enumerate(files):
#         if filename.endswith('.json'):
#             json_file_path = os.path.join(source_folder, filename)
            
#             try:
#                 # Open and load the JSON file
#                 with open(json_file_path, 'r') as f:
#                     data = json.load(f)
                    
#                 print(f"Processing file: {filename}")
#                 print(f"Datetime in JSON: {data.get('datetime')}")
                
#                 # Check if 'datetime' key exists and matches the target
#                 if 'datetime' in data and data['datetime'] == target_datetime:
#                     # Copy the JSON file
#                     shutil.copy(json_file_path, destination_folder)
#                     print(f"JSON file copied: {filename}")
                    
#                     # Check if there's a next file and if it's WEBM or OGG format
#                     if i + 1 < len(files):
#                         next_file = files[i + 1]
#                         print(f"Next file: {next_file}")
#                         if next_file.endswith('.webm') or next_file.endswith('.ogg'):
#                             media_file_path = os.path.join(source_folder, next_file)
#                             shutil.copy(media_file_path, destination_folder)
#                             print(f"Media file copied: {next_file}")
#                         else:
#                             print(f"No media file found right after {filename}")
#                     else:
#                         print(f"No media file after {filename}")
                    
#             except json.JSONDecodeError:
#                 print(f"Error: {filename} is not a valid JSON file.")
#             except Exception as e:
#                 print(f"Unexpected error with file {filename}: {e}")

# def main():
#     # Define paths
#     source_folder = "C:/Users/OM/Desktop/VLSID/archive"
#     destination_folder = "C:/Users/OM/Desktop/Anvesshan/Final_audio_files"
#     csv_path = "C:/Users/OM/Desktop/Anvesshan/newdataset.csv"

#     # Create destination folder if it doesn't exist
#     if not os.path.exists(destination_folder):
#         os.makedirs(destination_folder)
    
#     try:
#         # Read datetime values from CSV and limit to first 500 samples
#         df = pd.read_csv(csv_path)
#         datetime_values = df['datetime'].head(100).tolist()
        
#         # Get list of files in source folder
#         files = os.listdir(source_folder)
        
#         # Process each datetime value
#         for datetime_value in datetime_values:
            
#             print(f"/nProcessing datetime: {datetime_value}")
#             copy_files_for_datetime(source_folder, destination_folder, datetime_value, files)
            
#         print(f"/nOperation completed. First 100 samples have been copied to {destination_folder}")
        
#     except Exception as e:
#         print(f"Error processing CSV file: {e}")

# if __name__ == "__main__":
#     main()