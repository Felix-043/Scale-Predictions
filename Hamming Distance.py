import jellyfish

def hamming_distance(s1, s2):
  return jellyfish.hamming_distance(s1, s2)

# Example usage
string1 = "hello"
string2 = "hallo"
print("Hamming Distance:", hamming_distance(string1, string2))