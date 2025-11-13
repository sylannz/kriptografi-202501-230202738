import math

def entropy(keyspace_size):
    return math.log2(keyspace_size)

def unicity_distance(HK, R=0.75, A=26):
    return HK / (R * math.log2(A))

def brute_force_time(keyspace_size, attempts_per_second=1e6):
    seconds = keyspace_size / attempts_per_second
    days = seconds / (3600*24)
    return days

print("=== Perhitungan Entropy & Unicity Distance ===\n")

HK_caesar = entropy(26)
print("Entropy ruang kunci Caesar =", HK_caesar, "bit")
print("Unicity Distance =", unicity_distance(HK_caesar), "karakter")
print("Estimasi brute force (26 kunci) =", brute_force_time(26), "hari\n")

HK_AES128 = entropy(2**128)
print("Entropy ruang kunci AES-128 =", HK_AES128, "bit")
print("Unicity Distance =", unicity_distance(HK_AES128), "karakter")
print("Estimasi brute force (2^128 kunci) =", brute_force_time(2**128), "hari")