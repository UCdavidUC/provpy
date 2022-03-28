import math

def is_in_range(ip_range, ip):
    initial_ip = ip_range[0].split('.')
    end_ip = ip_range[1].split('.')
    current_ip = ip.split('.')
    is_in = True
    for position in range(0,4):
        if (int(current_ip[position]) >= int(initial_ip[position]) and int(current_ip[position]) <= int(end_ip[position])):
            is_in = True
        else:
            return False
    return is_in

def isIP(ip):
    ip_array = ip.split('.')
    decimal = 0
    for i in ip_array:
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

def calculate_range(actual_position, wildcard_bits):
    # Calculate ranges based on wildcard.
    ranges = round(256 / wildcard_bits)
    for element in range(0,ranges - 1):
        # It woing to meet the second condition always **
        if(actual_position > (element * wildcard_bits) and actual_position < ((element + 1) * wildcard_bits)):
            position = element * (wildcard_bits + 1)
            return position
        else:
            return 0

def get_ending_ip(initial_ip, position, addresses):
    ending_ip = []
    read = False
    for octet in range(0,4):
        a = int(initial_ip[octet])
        if (octet == position):
            ending_ip.append(str(a + addresses))
            read = True
        else:
            if (read == False):
                ending_ip.append(str(a))
            else:
                ending_ip.append('255')
    return '.'.join([str(b) for b in ending_ip])

def calculateInitialIP(root, addresses, cidr):
    segments = root.split('.')
    if (addresses < 256):
        wildcard_bits = (2 ** (32 - cidr)) - 1
        if ((int(segments[3]) + wildcard_bits) > 255):
            segments[3] = 255 - wildcard_bits
        else:
            starting_range = calculate_range(int(segments[3]), wildcard_bits)
            segments[3] = starting_range
        wrapper = get_ending_ip(segments, 3, addresses)

    elif (addresses <= (2 ** 16)):
        wildcard_bits = (2 ** (24 - cidr)) - 1
        # Check for overflow.
        if ((int(segments[2]) + wildcard_bits) > 255):
            segments[2] = 255 - wildcard_bits
        else:
            starting_range = calculate_range(int(segments[2]), wildcard_bits)
            segments[2] = starting_range
        segments[3] = 0
        wrapper = get_ending_ip(segments, 2, addresses)

    elif (addresses <= (2 ** 24)):
        # TODO: Complete
        wildcard_bits = (2 ** (16 - cidr)) - 1
        if ((int(segments[1]) + wildcard_bits) > 255):
            segments[1] = 255 - wildcard_bits
        else:
            starting_range = calculate_range(int(segments[1]), wildcard_bits)
            segments[1] = starting_range
        segments[3] = 0
        segments[2] = 0
        wrapper = get_ending_ip(segments, 1, addresses)

    else:
        # TODO: Complete
        wildcard_bits = (2 ** (16 - cidr)) - 1
        if ((int(segments[0]) + wildcard_bits) > 255):
            segments[0] = 255 - wildcard_bits
        else:
            starting_range = calculate_range(int(segments[1]), wildcard_bits)
            segments[0] = starting_range
        segments[3] = 0
        segments[2] = 0
        segments[1] = 0
        wrapper = get_ending_ip(segments, 0, addresses)
    return ['.'.join([str(segment) for segment in segments]), wrapper]

def main(ip, cidr):
    if(isIP(ip)):
        cidr_space = parseCIDR(cidr)
        if(isIP(cidr_space[0]) and int(cidr_space[1]) < 33):
            addresses = calculateAddresses(int(cidr_space[1]))
            range_ips = calculateInitialIP(cidr_space[0], addresses, int(cidr_space[1]))
            result = is_in_range(range_ips, ip)
            print(result)
            return result
        else:
            print('The CIDR format is not correct, it shoul be of the form 0.0.0.0/0')
    else:
        print('The IP format is wrong or it is not defined correctly, it should be of the form 0.0.0.0')

if __name__ == "__main__":
    main('128.224.1.239', '128.224.1.254/28')
