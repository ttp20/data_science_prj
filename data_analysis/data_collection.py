### run this file to get all data from diemthi.hcm.edu.vn
import subprocess

start = 2000001
end = 2085000



file = open("raw_data.txt", "w")

for i in range(start, end+1):
    command = f'curl -F "SoBaoDanh={i}" diemthi.hcm.edu.vn/Home/Show'
    result = subprocess.check_output(command)
    file.write(str(result) + "\n")

    



