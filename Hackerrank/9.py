n = int(input())

#print(bin(n).replace("0b", ""))
binary = bin(n).replace("0b", "")

#print(oct(n).replace("0o", ""))
octal = oct(n).replace("0o", "")

hexa = hex(n).replace("0x", "")
hexa = hexa.upper()

print(n,"\t\t",binary,"\t\t",octal,"\t\t",hexa)
