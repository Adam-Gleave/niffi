import pyffi.formats.nif as nif

stream = open("C:\\Users\\adamg\\OneDrive\\Documents\\BS\\NifConverter\\BSIBFarrunLCHouse01.nif", "rb")
data = nif.NifFormat.Data()
data.inspect(stream)

if data.version != 0x14020007:
    exit("Not a Skyrim .nif file!")
else:
    for blocktype in data.header.block_types:
        print(blocktype.decode("ascii"))

data.read(stream)
for root in data.roots:
    for block in root.tree():
        if isinstance(block, nif.NifFormat.BSShaderTextureSet):
            for i, tex in enumerate(block.textures):
                string = tex.decode()
                if len(string) > 0:
                    string = string.replace("A:\\SteamLibrary\\steamapps\\common\\Skyrim\\Data\\Textures\\", "textures\\")
                    print('%s' % (string))
                    block.textures.set_basic_item(i, string.encode("utf-8"))
                    print('%s' % tex.decode())

for root in data.roots:
    for block in root.tree():
        if isinstance(block, nif.NifFormat.BSShaderTextureSet):
            print(block)

stream = open("C:\\Users\\adamg\\OneDrive\\Documents\\BS\\NifConverter\\BSIBFarrunLCHouse01_converted.nif", "+wb")
data.write(stream)
stream.close()
