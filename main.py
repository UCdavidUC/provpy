import math

def isIP(ip):
    ip_array = ip.split('.')
    for i in ip_array:
        print('Evaluating ', i)
        if(int(i) > 255 or int(i) < 0):
            return False
    return True

def calculateAddresses(cidr_space):
    if (cidr_space == 32):
        return 1
    elif (cidr_space == 31):
        return 2
    else:
        return 2 ** (32 - cidr_space)

def parseCIDR(cidr):
    cidr_array = cidr.split('/')
    return cidr_array

def calculateInitialIP(root, addresses, space):
    if (addresses < 256):
        segments = root.split('.')
        segments[3] = 256 - addresses
        return '.'.join([str(segment) for segment in segments])
    elif (addresses < 65536):
        segments = root.split('.')
        wildcard_bits = int(segments[2]) + (2 ** (23 - space))
        if (wildcard_bits > 255):
            wildcard_bits = (int(segments[2]) - (2 ** (24 - space))) + 1
        segments[2] = wildcard_bits
        segments[3] = 0
        return '.'.join([str(segment) for segment in segments])
    elif (addresses < 256):
        segments = root.split('.')
        segments[3] = 256 - addresses
        return '.'.join([str(segment) for segment in segments])
    else:
        segments = root.split('.')
        segments[3] = 256 - addresses
        return '.'.join([str(segment) for segment in segments])

def main(ip, cidr):
    if(isIP(ip)):
        print('Evaluated IP', ip)
        cidr_space = parseCIDR(cidr)
        print('CIDR Address', cidr_space[0])
        print('CIDR Bits', cidr_space[1])
        if(isIP(cidr_space[0]) and int(cidr_space[1]) < 33):
            print('Determining range')
            addresses = calculateAddresses(int(cidr_space[1]))
            print(calculateInitialIP(cidr_space[0], addresses, int(cidr_space[1])))
            print('Address space', addresses)
        else:
            print('The CIDR format is not correct, it shoul be of the form 0.0.0.0/0')
    else:
        print('The IP format is wrong or it is not defined correctly, it should be of the form 0.0.0.0')

if __name__ == "__main__":
    main('192.168.14.255', '192.168.255.255/18')
