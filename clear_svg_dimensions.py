import os
import sys
import xml.etree.ElementTree as ET

def remove_width_height(svg_file_path):
    try:
        # Parse the SVG file
        tree = ET.parse(svg_file_path)
        root = tree.getroot()

        # Namespace handling (if the SVG file uses namespaces)
        namespaces = {'svg': 'http://www.w3.org/2000/svg'}
        ET.register_namespace('', namespaces['svg'])

        # Remove width and height attributes if they exist
        for attribute in ['width', 'height']:
            if attribute in root.attrib:
                del root.attrib[attribute]

        # Create /parsed/ directory if it doesn't exist
        parsed_dir = os.path.join(os.path.dirname(svg_file_path), 'parsed')
        if not os.path.exists(parsed_dir):
            os.makedirs(parsed_dir)

        # Construct new file path
        new_file_path = os.path.join(parsed_dir, os.path.basename(svg_file_path))

        # Write the modified SVG to the new file path
        tree.write(new_file_path)

        return True
    except Exception as e:
        print(f"Error processing {svg_file_path}: {e}")
        return False

def process_directory(directory):
    processed_files = []
    not_processed_count = 0

    for filename in os.listdir(directory):
        if filename.endswith(".svg"):
            svg_file_path = os.path.join(directory, filename)
            if remove_width_height(svg_file_path):
                processed_files.append(filename)
            else:
                not_processed_count += 1

    return processed_files, not_processed_count

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python clear_svg_dimensions.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    processed_files, not_processed_count = process_directory(directory_path)
    
    print(f"Total SVG files processed: {len(processed_files)}")
    if processed_files:
        print("Processed files:")
        for file in processed_files:
            print(f" - {file}")
    print(f"Total SVG files not processed: {not_processed_count}")
