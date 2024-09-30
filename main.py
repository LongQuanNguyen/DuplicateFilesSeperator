import os
import hashlib
import shutil

def hash_file(file_path):
    """Generate a hash for a file."""
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def find_duplicates(directory):
    """Find and move duplicate files in the given directory."""
    if not os.path.isdir(directory):
        print(f"{directory} is not a valid directory./n")
        return

    duplicate_dir = os.path.join(directory, 'DUPLICATE')
    if not os.path.exists(duplicate_dir):
        os.makedirs(duplicate_dir)

    seen_hashes = {}
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_hash = hash_file(file_path)
            if file_hash in seen_hashes:
                shutil.move(file_path, os.path.join(duplicate_dir, filename))
                print(f"Moved duplicate file {filename} to {duplicate_dir}")
            else:
                seen_hashes[file_hash] = file_path

if __name__ == "__main__":
    directory = input("Enter the directory path: ")
    find_duplicates(directory)
    print("\nSeparation completed! Check for the DUPLICATE folder under ", directory)
