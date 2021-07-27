import re
file=open("data_corey.txt",mode='r')
myfile=open("data_phone.json",mode='r')

mytext=file.read()

myjson=myfile.read()

#print("----------------------------------------------------")
phone_num=r"\d{3}-\d{3}-\d{4}"
results=re.findall(phone_num,mytext)
#for i in results:
    #print(i)

#print("----------------------------------------------------")
end_7=r"\d{3}-\d{3}-\d{3}7"
res=re.findall(end_7,mytext)

#print("THERE ARE NUMBERS WITH ENDING 7 :")
#for r in res:
    #print( r)
#print("----------------------------------------------------")
email=r"([A-Za-z]+@[A-Za-z]+\.(net|com))"
r=re.findall(email,mytext)
#for rs in r:
    #print(rs)

cell_phone_in_e164=r"\d{13}"
res1=re.findall(cell_phone_in_e164,myjson)
#for n in res1:
    #print(n)

cell_phone=r"\(\d{3}\)\s\d{3}-\d{4}"
res2=re.findall(cell_phone,myjson)
for m in res2:
    print(m)


#print("----------------------------------------------------")

print(f"Total amount of phone numbers: {str(len(results))}")

print(f"Total amount of phone numbers with ending 7: {str(len(res))}")

print(f"Total amount of emails: {str(len(r))}")

print(f"Total amount of phone numbers with 13 digits: {str(len(res1))}")
file.close()
myfile.close()
