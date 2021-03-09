def solve(path):
	# pdf-parser
	optional_modules.pdf_parser(path)


	# strings
	optional_modules.strings(path)

	# carving
	optional_modules.carving(path)

	optional_modules.exiftool(path)
	optional_modules.binwalk(path)
	optional_modules.xxd(path)
