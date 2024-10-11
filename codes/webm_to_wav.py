from pydub import AudioSegment
import os

def convert_webm_to_wav(input_file, output_file):
    # Check if input file exists
    if not os.path.isfile(input_file):
        print(f"Error: Input file '{input_file}' does not exist.")
        return

    try:
        # Load the WebM file
        audio = AudioSegment.from_file(input_file, format="webm")

        # Export as WAV
        audio.export(output_file, format="wav")

        print(f"Successfully converted '{input_file}' to '{output_file}'")
    except Exception as e:
        print(f"Error occurred during conversion: {e}")

# Example usage
input_file = r"C:\Users\OM\Desktop\Anvesshan\audio2\09976800-a17a-4ab5-b9a2-547a8091e6b6.webm"
output_file ="C:/Users/OM/Desktop/Anvesshan/Final_supported_file/output100.wav"
convert_webm_to_wav(input_file, output_file)



# from pydub import AudioSegment
# import os

# def convert_webm_to_wav(input_file, output_file):
#     try:
#         # Load the WebM file
#         audio = AudioSegment.from_file(input_file, format="webm")
        
#         # Export as WAV
#         audio.export(output_file, format="wav")
        
#         print(f"Successfully converted '{input_file}' to '{output_file}'")
#     except Exception as e:
#         print(f"Error occurred during conversion of {input_file}: {e}")

# def batch_convert_webm_to_wav(input_folder, output_folder):
#     # Create output folder if it doesn't exist
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)
    
#     # Counter for tracking conversions
#     successful_conversions = 0
#     failed_conversions = 0
    
#     # Get all WebM files in the input folder
#     for filename in os.listdir(input_folder):
#         if filename.lower().endswith('.webm'):
#             input_path = os.path.join(input_folder, filename)
            
#             # Create output filename (replace .webm with .wav)
#             output_filename = filename.rsplit('.', 1)[0] + '.wav'
#             output_path = os.path.join(output_folder, output_filename)
            
#             try:
#                 convert_webm_to_wav(input_path, output_path)
#                 successful_conversions += 1
#             except Exception as e:
#                 print(f"Failed to convert {filename}: {e}")
#                 failed_conversions += 1
    
#     # Print summary
#     print("/nConversion Summary:")
#     print(f"Successfully converted: {successful_conversions} files")
#     print(f"Failed conversions: {failed_conversions} files")
#     print(f"Total files processed: {successful_conversions + failed_conversions}")

# def main():
#     # Define your input and output folders
#     input_folder = "C:/Users/OM/Desktop/Anvesshan/Final"
#     output_folder = "C:/Users/OM/Desktop/Anvesshan/Final_supported_file"
    
#     print(f"Starting batch conversion from: {input_folder}")
#     print(f"Output files will be saved to: {output_folder}")
    
#     batch_convert_webm_to_wav(input_folder, output_folder)

# if __name__ == "__main__":
#     main()