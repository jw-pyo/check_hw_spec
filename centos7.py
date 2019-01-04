import os

CPUModel = os.popen("grep \"model name\" /proc/cpuinfo | tail -1").read().split(": ")[-1]
physicalCPU = int(os.popen("grep \"physical id\" /proc/cpuinfo | sort -u | wc -l").read())
physicalCoresPerCPU = int(os.popen("grep \"cpu cores\" /proc/cpuinfo | tail -1").read().split(": ")[-1])
totalVirtualCores = int(os.popen("grep -c processor /proc/cpuinfo").read())
totalMemKB = int(os.popen("grep \"MemTotal\" /proc/meminfo").read().split(":")[-1].strip().split("kB")[0])
totalMemMB = totalMemKB / 1024
totalMemGB = totalMemMB / 1024
GPUInfo = os.popen("nvidia-smi").read()

print("CPU Model: {}".format(CPUModel))
print("The number of physical CPU: {}".format(physicalCPU))
print("The number of physical cores per CPU: {}".format(physicalCoresPerCPU))
print("Total physical cores: {}".format(physicalCPU * physicalCoresPerCPU))
print("Total virtual cores: {}".format(totalVirtualCores))
print("Total Memory: {} GB".format(totalMemGB))
print("GPU INFO\n{}".format(GPUInfo))
