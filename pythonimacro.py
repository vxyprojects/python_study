
import os
os.system('ls')
os.system('"C:\Program Files\iOpus\iMacros\iMacros.exe" -macro FillForm.iim')
# os.system('ls')
# iMacros.exe 찾아서 실행 시키면 어떻게  나오는지 확인 해본다

# import win32com.client
# def Hello():
#  import win32com.client
#  w=win32com.client.Dispatch("imacros")
#  w.iimInit("", 1)
#  w.iimPlay("Demo\\FillForm")
# if __name__=='__main__':
#  Hello()
# import os
# os.system('"C:\Program Files\iOpus\iMacros\iMacros.exe" -macro FillForm.iim')



# f=open('frame.iim','w');
# f.write('VERSION BUILD=844 RECORDER=CR'+'\n')
# f.write('TAG POS=1 TYPE=SPAN ATTR=TXT:조경애'+'\n')
# f.write('TAG POS=1 TYPE=SPAN ATTR=TXT:조보영'+'\n')

# VERSION BUILD=844 RECORDER=CR
# TAG POS=1 TYPE=SPAN ATTR=TXT:조경애
# TAG POS=1 TYPE=SPAN ATTR=TXT:조보영


	# f.write('URL GOTO=about:home'+'\n')
	# f.write('URL GOTO=https://kr.edit.sdb.yahoo.com/verify_adult?.done=http%3A%2F%2Fkr.news.yahoo.com%2Fservice%2Fcartoon%2Fshellview2.htm%3Flinkid%3Dseries_cartoon%26sidx%3D10617%26widx%3D106%26page%3D2%26seq%3D%26wdate%3D20100406%26wtitle%3D%25B3%25AB%25C0%25E5%25BA%25D2%25C0%25D4'+'\n')
	# f.write('TAG POS=1 TYPE=INPUT:TEXT FORM=NAME:pgForm ATTR=ID:username CONTENT='+userid+'\n')
	# f.write('TAG POS=1 TYPE=INPUT:TEXT FORM=NAME:pgForm ATTR=ID:snumber1 CONTENT='+snum1+'\n')
	# f.write('SET !ENCRYPTION NO'+'\n')
	# f.write('TAG POS=1 TYPE=INPUT:PASSWORD FORM=NAME:pgForm ATTR=ID:snumber2 CONTENT='+snum2+'\n')
	# f.write('TAG POS=1 TYPE=INPUT:BUTTON FORM=ID:pgForm ATTR=ID:confirmBtn'+'\n')
	# f.write('WAIT SECONDS=5'+'\n')

	# for pg in pglink:
	# 	f.write("URL GOTO="+pg[1]+'\n')
	# 	f.write("SAVEAS TYPE=PNG FOLDER=C:\Z\ FILE="+pg[0]+'\n')
	# 	f.write("WAIT SECONDS=3\n\n")

