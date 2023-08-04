import java.util.Scanner;
public class Subnetting {
    public static String toBinary(String address) {
        String[] octets = address.split("\\.");
        StringBuilder binary = new StringBuilder();
        for (String octet : octets) {
            int decimal = Integer.parseInt(octet);
            binary.append(String.format("%08d", Integer.parseInt(Integer.toBinaryString(decimal))));
        }

        return binary.toString();
    }

    public static String toAddress(String binary) {
        StringBuilder address = new StringBuilder();
        for (int i = 0; i < 32; i += 8) {
            int decimal = Integer.parseInt(binary.substring(i, i + 8), 2);
            address.append(decimal).append(".");
        }
        return address.substring(0, address.length() - 1);
    }

    public static String and(String binary1, String binary2) {
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < 32; i++) {
            char bit1 = binary1.charAt(i);
            char bit2 = binary2.charAt(i);
            if (bit1 == '1' && bit2 == '1') {
                result.append('1');
            } else {
                result.append('0');
            }
        }
        return result.toString();
    }

    public static String or(String binary1, String binary2) {
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < 32; i++) {
            char bit1 = binary1.charAt(i);
            char bit2 = binary2.charAt(i);
            if (bit1 == '0' && bit2 == '0') {
                result.append('0');
            }
            else {
                result.append('1');
            }
        }
        return result.toString();
    }

    public static String not(String binary) {
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < 32; i++) {
            char bit = binary.charAt(i);
            if (bit == '0') {
                result.append('1');
            }
            else {
                result.append('0');
            }
        }
        return result.toString();
    }

    public static String addOne(String binary) {
        StringBuilder result = new StringBuilder(binary);
        int carry = 1;
        for (int i = 31; i >= 0; i--) {
            char bit = result.charAt(i);
            if (bit == '0' && carry == 1) {
                result.setCharAt(i, '1');
                carry = 0;
                break;
            }
            else if (bit == '1' && carry == 1) {
                result.setCharAt(i, '0');
                carry = 1;
            }
        }
        return result.toString();
    }

    public static String subtractOne(String binary) {
        StringBuilder result = new StringBuilder(binary);
        int borrow = 0;
        for (int i = 31; i >= 0; i--) {
            char bit = result.charAt(i);
            if (bit == '1' && borrow == 1) {
                result.setCharAt(i, '0');
                borrow = 0;
                break;
            }
            else if (bit == '0' && borrow == 1) {
                result.setCharAt(i, '1');
                borrow = 1;
            }
        }
        return result.toString();
    }

 

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the IP address: ");
        String ip_address = scanner.next();
        System.out.print("Enter the number of subnets: ");
        int num_subnets = scanner.nextInt();

        String ip_address_bin = toBinary(ip_address);
        String subnet_mask_bin;

        char first_bit = ip_address_bin.charAt(0);
        char second_bit = ip_address_bin.charAt(1);
        char third_bit = ip_address_bin.charAt(2);
        char fourth_bit = ip_address_bin.charAt(3);

        if (first_bit == '0') {
            subnet_mask_bin = "11111111000000000000000000000000";
        }
        else if (first_bit == '1' && second_bit == '0') {
            subnet_mask_bin = "11111111111111110000000000000000";
        }
        else if (first_bit == '1' && second_bit == '1' && third_bit == '0') {
            subnet_mask_bin = "11111111111111111111111100000000";
        }
        else {
            System.out.println("Invalid IP address class.");
            return;
        }

        int network_prefix = subnet_mask_bin.indexOf('0');
        int host_bits = 32 - network_prefix;

        for (int i = 0; i < num_subnets; i++) {
            System.out.print("Enter the number of hosts for subnet " + (i + 1) + ": ");
            int num_hosts = scanner.nextInt();
            int subnet_bits = host_bits - (int) Math.ceil(Math.log(num_hosts + 2) / Math.log(2));
            subnet_mask_bin = "1".repeat(network_prefix + subnet_bits) + "0".repeat(host_bits - subnet_bits);
            String subnet_mask = toAddress(subnet_mask_bin);
            String network_address_bin = ip_address_bin.substring(0, network_prefix + subnet_bits) + "0".repeat(host_bits - subnet_bits);
            String network_address = toAddress(network_address_bin);
            String broadcast_address_bin = ip_address_bin.substring(0, network_prefix + subnet_bits) + "1".repeat(host_bits - subnet_bits);
            String broadcast_address = toAddress(broadcast_address_bin);
            System.out.println("Subnet " + (i + 1) + ":");
            System.out.println("Subnet mask: " + subnet_mask);
            System.out.println("Network address: " + network_address);
            System.out.println("Usable IP addresses: " + network_address
+ " - " + toAddress(subtractOne(broadcast_address_bin)));
            System.out.println();
            ip_address_bin = or(network_address_bin,not(subnet_mask_bin));
            ip_address_bin = addOne(ip_address_bin);
        }
    }
}

