start_msg = '''|---欢迎进入球员查询程序---|
|---1、 查询球员资料---|
|---2、 插入新的球员---|
|---3、 删除已有球员---|
|---4、 退出查询程序---|'''

print(start_msg)

support_num = ['1', '2', '3', '4', '?']
AddresBook = {'kobe':'24', 'jordan':'23', 'james':'23', 'wade':'3', 'rose':'1', 'curry':'30'} #定义原始通讯录

# def main(run_time):
while 1:
	temp = input("请输入指令代码:")
	if temp not in support_num:
		print("<输入的指令错误，请按照提示输入>")
		continue

	if temp == '?':
		print(start_msg)
		continue

	if temp == '4':
		print("|---感谢使用球员查询程序---|")
		break

	name = input("请输入球员姓名:")

	if temp == '1':
		if name in AddresBook:
			print(name, ':', AddresBook[name])
			continue
		else:
			print("该球员不存在！")

	if temp == '2':
		if name in AddresBook:
			print("您输入的姓名已存在-->>", name, ':', AddresBook[name])
			isEdit = input("是否修改球员资料(Y/N）:")
			if isEdit == 'Y':
				userphone = input("请输入球员号码：")
				AddresBook[name] = userphone
				print("球员资料修改成功")
				continue
			else:
				continue
		else:
			userphone = input("请输入球员号码：")
			AddresBook[name] = userphone
			print("球员加入成功！")
			continue

	if temp == '3':
		if name in AddresBook:
			del AddresBook[name]
			print("删除成功！")
			continue
		else:
			print("球员不存在")