import argparse
import sys

def format_nftables_set(ips, style='single', comment=None):
    """Format IP addresses into nftables set syntax."""
    formatted = []
    
    if comment:
        formatted.append(f"    # {comment}")
        
    if style == 'single':
        elements = ", ".join(ips)
        formatted.append(f"    elements = {{ {elements} }}")
    elif style == 'multi':
        formatted.append("    elements = {")
        for ip in ips:
            formatted.append(f"        {ip},")
        if ips:  # Remove trailing comma only if there are IPs
            formatted[-1] = formatted[-1].rstrip(',')
        formatted.append("    }")
    
    return '\n'.join(formatted)

def main():
    parser = argparse.ArgumentParser(
        description='Format IPs for nftables sets',
        formatter_class=argparse.RawTextHelpFormatter,
        epilog='''Examples:
  Basic usage:     %(prog)s ips.txt
  Single-line:     %(prog)s ips.txt -s single
  Save to file:    %(prog)s ips.txt -o nftables.conf
  With comment:    %(prog)s ips.txt -c "Trusted devices"'''
    )
    
    # Show help if no arguments provided
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    parser.add_argument('input_file', help='File containing one IP per line')
    parser.add_argument('-o', '--output', help='Output file (default: stdout)')
    parser.add_argument('-s', '--style', choices=['single', 'multi'], 
                      default='multi', help='''Formatting style:
  single = All IPs in one line
  multi  = Each IP on separate line (default)''')
    parser.add_argument('-c', '--comment', help='Add comment above elements')
    
    args = parser.parse_args()
    
    try:
        with open(args.input_file) as f:
            ips = [line.strip() for line in f 
                  if line.strip() and not line.startswith('#')]
    except FileNotFoundError:
        sys.exit(f"Error: Input file '{args.input_file}' not found")

    set_config = f"set whitelist_ips {{\n    type ipv4_addr\n"
    set_config += format_nftables_set(ips, args.style, args.comment)
    set_config += "\n}\n"

    if args.output:
        with open(args.output, 'w') as f:
            f.write(set_config)
        print(f"Configuration saved to {args.output}")
    else:
        print(set_config)

if __name__ == '__main__':
    main()
