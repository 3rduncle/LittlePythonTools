'''
	http://stackoverflow.com/questions/17977584/how-to-read-data-from-excel-and-write-it-to-text-file-line-by-line
'''
import sys
import xlrd

workbook = xlrd.open_workbook(sys.argv[1])
sh = workbook.sheet_by_index(int(sys.argv[2]))
print >>sys.stderr, sh.nrows
print >>sys.stderr, sh.ncols
for row in range(sh.nrows):
	values = []
	for col in range(sh.ncols):
		value = sh.cell_value(row, col)
		if type(value) == type(u''):
			value = value.encode('utf8')
		else:
			value = str(value)
		if '\n' in value:
			value = value.replace('\n', '\\n')
		values.append(value)
	print '\t'.join(values)
