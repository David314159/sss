from region import Region

region: Region = Region(8, 9)
region.set_val(1, 2, 11)
print(region.get_val(1, 2))
