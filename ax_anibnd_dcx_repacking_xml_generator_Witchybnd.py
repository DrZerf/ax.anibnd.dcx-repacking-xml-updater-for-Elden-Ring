import os
import shutil


def generate_xml_entries(output_file):
    current_dir = input("Enter the path of the folder containing .hkx files \n (E.g.: C:\\Users\\XXX\\Desktop\\Elden_ring_modengine\\mod\\chr\\c0000_a0x-anibnd-dcx\\GR\data\\INTERROOT_win64\\chr\\c0000\\hkx\\a0x_compendium)\n")  
    dcx_folder = None
    folder_path = current_dir  
    compendium_path_uncorrected = folder_path.split("-dcx")[1] if "-dcx" in folder_path else ""
    compendium_path = compendium_path_uncorrected[1:]
    while current_dir:
        if current_dir.endswith("-dcx"):
            dcx_folder = current_dir
            break
        current_dir, tail = os.path.split(current_dir)
    if not dcx_folder:
        print("Error: Make sure the xml_creator is located in the c*x_compendium folder")
        return

    input_xml_path = os.path.join(dcx_folder, "_witchy-bnd4.xml")
    backup_xml_path = os.path.join(dcx_folder, "_witchy-bnd4_backup.xml")

    if os.path.exists(input_xml_path):
        shutil.copy(input_xml_path, backup_xml_path)
        print("Backup of _witchy-bnd4.xml created successfully:")


    with open(input_xml_path, 'r') as input_file:
        first_28_lines = input_file.readlines()[:28]


    with open(output_file, 'w') as f:
        for line in first_28_lines:
            f.write(line)
        for filename in os.listdir(folder_path):
            if filename.endswith('.hkx'):
                f.write(" " * 4 + "</file>\n")
                f.write(" " * 4 + "<file>\n")
                file_id = filename.replace('a', '1').split('_')[0][1:] + filename.split('_')[1].split('.')[0]
                f.write("      <flags>Flag1</flags>\n")
                f.write(" " * 6 + "<id>1{}</id>\n".format(file_id))
                f.write(" " * 6 + "<path>{}</path>\n".format(compendium_path + "\\" + filename))
        f.write("    </file>\n")
        f.write("  </files>\n")
        f.write("</bnd4>")

    os.replace(output_file, input_xml_path)


    print(r"_witchy-bnd4.xml file generated successfully! Have a nice day :)")
    print("\n")

generate_xml_entries('_witchy-bnd4.xml')

print("Press Enter to exit...")
input() 
print("Exiting program...")

