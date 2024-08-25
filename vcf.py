import csv

def csv_to_vcf(csv_filename, vcf_filename):
    with open(csv_filename, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')  # Use ';' as the separator
        with open(vcf_filename, mode='w') as vcf_file:
            for row in csv_reader:
                first_name = row['First name']
                prefix_last_name = row.get('Prefix last name', '')
                last_name = row['Last name']
                full_name = f"{first_name} {prefix_last_name} {last_name}".strip()
                
                # For the N field (N:last name;first name;middle name;;), with empty middle name
                n_field = f"{last_name};{first_name};;;"
                
                organization = row['Status']  # The organization to be displayed
                title = "Nyenrode Business University"  # The title (can be adjusted if it should come from CSV)

                vcf_file.write("BEGIN:VCARD\n")
                vcf_file.write("VERSION:3.0\n")
                vcf_file.write("PRODID:-//Apple Inc.//macOS 14.5//EN\n")
                vcf_file.write(f"N:{n_field}\n")
                vcf_file.write(f"FN:{full_name}\n")
                vcf_file.write(f"ORG:{organization};\n")
                vcf_file.write(f"TITLE:{title}\n")
                vcf_file.write(f"EMAIL;type=INTERNET;type=pref:{row['Email']}\n")
                vcf_file.write(f"TEL;type=pref:{row['Mobile phone']}\n")
                vcf_file.write("END:VCARD\n")

# Pre-defined file paths
input_csv = '/Users/juliandehaas/Desktop/NCV.csv'
output_vcf = '/Users/juliandehaas/Desktop/output_vcf.vcf'

# Convert the CSV to VCF
csv_to_vcf(input_csv, output_vcf)

print(f"VCF file saved at {output_vcf}")
