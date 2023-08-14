def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:   #去除隱藏在記事本裡面的\ufeff編碼
		for line in f:
			lines.append(line.strip())  #.strip() 去除換行符號
	return lines

def convert(lines):
            
	person = None
	allen_word_count = 0  #現在這邊在求2人的對話紀錄字數 貼圖 圖片
	allen_sticker_count = 0
	allen_picture_count = 0
	viki_word_count = 0    
	viki_sticker_count = 0    
	viki_picture_count = 0    
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_picture_count += 1
			else:
				for m in s[2:]:
					allen_word_count += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_picture_count += 1
			else:
				for m in s[2:]:
					viki_word_count += len(m)
	print('Allen說了',allen_word_count, '個字數 ')
	print('傳了', allen_sticker_count, '個貼圖')
	print('傳了', allen_picture_count, '個圖片')
	print('Viki說了', viki_word_count, '個字數')
	print('傳了', viki_sticker_count, '個貼圖')
	print('傳了', viki_picture_count, '個貼圖')


def write_file(filename, lines):
	with open(filename) as f:
		for line in lines:  #for loop 來讀取 lines 清單
			f.write(line + '\n')

			
def main():
	lines = read_file('LINE-viki.txt')
	lines = convert(lines)  # 覆蓋回去lines
	#wire_file('output.txt', lines)  #自由填入輸出的檔名
main()