def	approximate_size(size, is_a_kilobyte_1024_bytes=False):
	"""
	"""
	SUFFIXS = {1000: ["KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"],
						1024:  ["KiB", "MiB", "GiB", "TiB", "PiB", "EiB", "ZiB", "YB"]}
	if size < 0:
		raise("size coundn't below zero")
		
	multiple = 1024 if is_a_kilobyte_1024_bytes else 1000
	
	for suffix in SUFFIXS[multiple]:
		size /= multiple
		if size < multiple:
			return "{0:.1f} {1}".format(size, suffix)
	
	raise ValueError("number too large")
	
if __name__ == "__main__":
	print(approximate_size(10000010000, True))
	print(approximate_size(10000000000, False))