def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:   #去除隱藏在記事本裡面的\ufeff編碼
		for line in f:
			lines.append(line.strip())  #.strip() 去除換行符號
	return lines

def convert(lines):

	new_file = []             #建立新清單
	person = None             #這邊先宣告person = None 是為了預防 如果input檔案裏面 第一行不是人名時會直接執行new.append(person) 以致無法執行
	for line in lines:        #lines清單中的每一行line
		if line == 'Allen':   #當line行遇到allen
			person = 'Allen'  #接下來說話的都是allen開頭
			continue  	     
		elif line == 'Tom':   #當line遇到Tom
			person = 'Tom'    #接下來每一句都是Tom
			continue          
			#這邊兩個continue是代表 當遇到人名那一行時不執行new.append那一行 不然就會有 Allen: Allen 跟 Tom: Tom的出現
		if person:      # 這邊代表  當如果是 None 則不執行 跳下一輪for
			new.append(person + ': ' + line)
	retutn(new_file)
def write_file(filename, lines):
	with open(filename) as f:
		for line in lines:  #for loop 來讀取 lines 清單
			f.write(line + '\n')
def main():
	lines = read_file('input.txt')
	lines = convert(lines)  # 覆蓋回去lines
	wire_file('output.txt', lines)  #自由填入輸出的檔名
main()