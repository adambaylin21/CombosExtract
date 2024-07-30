# -*- coding: utf-8 -*-

from colorama import Fore, Style
import os, time
import tkinter as tk
from tkinter import filedialog

from tqdm import tqdm

def logo():
    os.system('cls')
    logo = """

█▀▄▀█ █▀▀█ █░░█ ░░░ █▀▀▄   ▀█▀ █▀▀ █▀▀ █░░█
█░▀░█ █▄▄█ ▄▀▀▄ ▀▀▀ █░░█   ░█░ █▀▀ █░░ █▀▀█
▀░░░▀ ▀░░▀ ▀░░▀ ░░░ ▀▀▀    ░▀░ ▀▀▀ ▀▀▀ ▀░░▀
        
        Copyright By : Adam Baylin
    """
    print (Fore.GREEN + Style.BRIGHT + logo)

def process_menu():
    menu = """
    [-----------------------------]
        1. Tool Edit Combo.
        2. Thoát Tool.
    [-----------------------------]
"""
    print (Fore.WHITE + Style.BRIGHT + menu)
    choice_user = input(Fore.WHITE + Style.BRIGHT + "- Nhập Lựa Chọn : ")

    if choice_user == '1':
        os.system('cls')
        file_path = chon_file()
        classify_emails(file_path)

    if choice_user == '2':
        quit()
    else:
        process_menu()

def classify_emails(file_path):
    start_time = time.time()
    total_lines = 0
    
    with open(file_path, 'r') as file:
        total_lines = sum(1 for _ in file)
        file.seek(0)  # Quay về đầu file

        os.makedirs("Emails", exist_ok=True)

        # Sử dụng tqdm để hiển thị thanh tiến trình
        with tqdm(total=total_lines, unit=" dòng", desc="Xử lý email") as pbar:
            for line in file:
                try:
                    email, password = line.strip().split(":")
                    domain = email.split("@")[1]

                    file_name = os.path.join("emails", f"{domain}.txt")
                    with open(file_name, 'a') as domain_file:
                        domain_file.write(f"{email}:{password}\n")
                except: pass
                pbar.update(1)  # Cập nhật thanh tiến trình
           
        end_time = time.time()
        print(f"\nXử lý hoàn tất trong {end_time - start_time:.2f} giây")
        print(f"Tổng số email đã xử lý: {total_lines}")

def chon_file():
    root = tk.Tk()
    root.withdraw()  # Ẩn cửa sổ gốc Tkinter
    duong_dan = filedialog.askopenfilename()  # Mở cửa sổ chọn file
    return duong_dan

logo()
process_menu()