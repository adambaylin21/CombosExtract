import os
import glob

# Lấy đường dẫn của thư mục hiện tại (nơi chứa file thực thi)
current_directory = os.path.dirname(os.path.abspath(__file__))

# Tìm tất cả các file .txt trong thư mục hiện tại
txt_files = glob.glob(os.path.join(current_directory, '*.txt'))

# Tên file đầu ra
output_file = 'combined_output.txt'

# Mở file đầu ra để ghi
with open(output_file, 'w', encoding='utf-8') as outfile:
    # Lặp qua từng file .txt
    for txt_file in txt_files:
        # Mở và đọc nội dung của file
        with open(txt_file, 'r', encoding='utf-8', errors='ignore') as infile:
            # Ghi nội dung vào file đầu ra
            outfile.write(infile.read())
            # Không thêm dòng trống giữa các file

print(f"Combined {len(txt_files)} file .txt into {output_file}")
