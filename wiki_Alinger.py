import m_c
from optparse import OptionParser, SUPPRESS_HELP , OptionGroup
#4:03...
def main():
	usage = "Usage: %prog [-h] [-r|-t|-l] [[sub_options] arg]"+"\n\nUpdate:15/9/2015.20:35"
	parser = OptionParser(usage,add_help_option=False)
	parser.add_option("-h", "--help", action="help",help="Display Help Menu Again.")
	

	group4 = OptionGroup(parser, "Load-Match(Wiki) Options")
	group4.add_option("-m","--match",dest="match", action="store_true",
					 help="Start Load-Test-Match. ",default=False)
	group4.add_option("--ms",dest="sourcefile_m",default="zh-en/200.test.zh", help="Sourcefile name.[default: %default]")
	group4.add_option("--mt",dest="targetfile_m",default="zh-en/200.test.en", help="Targetfile name.[default: %default]")
	group4.add_option("--mlm",dest="lexical",default="zh-en/zh2e_f", help="Lexical_Model name.[default: %default]")
	#group2.add_option("--tor",dest="order",default="e2f", help="The order of lexical model.[default: %default]")	
	group4.add_option("--mm",dest="model",default="object/model.p", help="maximum entropy model name.[default: %default]")
	group4.add_option("--mh",dest="ok_rate",default=0.95,type="float", help="OK RATE greater than.[default: %default]")
	#group4.add_option("--mw",dest="win_size",default=0.06,type="float", help="Windows size = % of corpus.[default: %default]")
	group4.add_option("--mc",dest="cores",default=12,type="int", help="The amount of cores.[default: %default]")
	group4.add_option("--mo",dest="outputfile_m",default="match/1000.test.match", help="Outputfile name.[default: %default]")
	group4.add_option("--m_sort",dest="m_sort",default=True, action="store_false",help="Disable sort the original file.[default: %default]")
	parser.add_option_group(group4)
	

	
	(options, args) = parser.parse_args()
	
	
	'''
	print 'args',
	print args
	'''
	'''
	print 'options',
	print options
	'''
	tmp_c = int(options.match)
	
	if tmp_c > 1:
		parser.error("you only can pick one of the main actions.")
	elif tmp_c == 0:
		parser.error("you have atleast pick one of the main actions.")
	'''
	if len(args) != 1:
		parser.error("incorrect number of arguments")
	if options.verbose:
		print "reading %s..." % options.filename
	'''
	
	if options.match:
		pre_args =  {'class_file':options.model,'f_sets_file':'no'}
		m_c.load(pre_args)
		match_args = {'zh_dir':options.sourcefile_m,'en_dir':options.targetfile_m,
		'ok_rate':options.ok_rate,'cores':options.cores,'output':options.outputfile_m,'lex_table':options.lexical
		,'sort':options.m_sort}
		#omg i will change it later
		m_c.find_wiki_match(match_args)

if __name__ == "__main__":
	import sys
	try: 
		if sys.argv[1] == None:
			no_arg = True
	except IndexError:
		sys.argv.append('-h')
	
	main()