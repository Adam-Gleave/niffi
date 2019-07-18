import argparse
import pyffi.formats.nif as nif
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "pattern",
        help="pattern to replace in texture paths",
        type=str
    )
    parser.add_argument(
        "replacement",
        help="replacement for \"pattern\"",
        type=str
    )
    parser.add_argument(
        "--file",
        help=".nif file to process",
        type=str
    )
    parser.add_argument(
        "--dir",
        help="process all files in given directory",
        type=str
    )
    args = parser.parse_args()

    if args.file and args.dir:
        exit("ERROR: Cannot process both a file and a directory.")
    elif not args.file and not args.dir:
        exit("ERROR: No .nif files provided.")
    elif args.file:
        process_file(args, args.file)
    else:
        process_directory(args)


def process_file(args, file):
    try:
        stream = open(file, "rb")
    except:
        exit("ERROR: Cannot find specified .nif file \"{}\"".format(file))

    data = nif.NifFormat.Data()
    data.inspect(stream)

    if data.version != 0x14020007:
        exit("Not a Skyrim .nif file!")

    print("Reading {} into memory...".format(file))
    data.read(stream)
    count = 0
    for root in data.roots:
        for block in root.tree():
            if isinstance(block, nif.NifFormat.BSShaderTextureSet):
                for i, tex in enumerate(block.textures):
                    string = tex.decode()
                    if len(string) > 0:
                        if args.pattern not in string:
                            print("\tPattern not found in \"{}\"!".format(string))
                        else:
                            old = string
                            string = string.replace(args.pattern, args.replacement)
                            block.textures.set_basic_item(i, string.encode("utf-8"))
                            print("\t{} => {}".format(old, string))
                            count += 1

    print("Successfully replaced {} texture paths.".format(count))
    stream.close()
    stream = open(file, "wb")
    data.write(stream)
    stream.close()


def process_directory(args):
    print("Searching for .nif files in \"{}\"".format(args.dir))
    files = []
    for file in os.listdir(args.dir):
        if file.endswith(".nif"):
            files.append(file)
            print("\tFound \"{}\"!".format(file))

    if not files:
        exit("ERROR: No .nif files found in specified directory.")
    else:
        print("Successfully found {} .nif files in directory.".format(len(files)))
        full_filenames = list(map(lambda filename: os.path.join(args.dir, filename), files))
        print(full_filenames)

        for file in full_filenames:
            process_file(args, file)


if __name__ == "__main__":
    main()
