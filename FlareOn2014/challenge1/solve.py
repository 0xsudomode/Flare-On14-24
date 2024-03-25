#!/usr/bin/python

# Documentation : https://pan-unit42.github.io/dotnetfile/
from dotnetfile import DotNetPE

file_path = "./challenge1.exe"
pe_file =  DotNetPE(file_path)

flag = ""

for resource_dict in pe_file.get_resources() :
    # Print the contents of each dictionary
    for key, value in resource_dict.items():
          # Filter dat_secret among all other resources
          if resource_dict.get("Name") == "rev_challenge_1.dat_secret.encode":
                dat_secret = resource_dict.get("Data")
                for b in dat_secret:
                    flag += chr(((b >> 4 | (int(b) << 4 & 240)) ^ 41))
                print(flag)
                break