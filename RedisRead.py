import redis

myHostname = raw_input("Enter the Host Name: ") 
myPassword = raw_input("Enter the Password: ")

r = redis.StrictRedis(host=myHostname, port=6380,password=myPassword,ssl=True)

result = r.ping()
if (str(result)=="false"):
    print("Check HostName & Password")

loop=True
while loop :
    Choice=raw_input("\n**Select from the options:**\n\tA.Client List\n\tB.Enter Key\n\tQ.Quit\n")

    if((str(Choice)=="A")|(str(Choice)=="a")):
        result = r.client_list()
        print("CLIENT LIST returned :\n ") 
        for c in result:
            print("\t ID : " + c['id'] + ", Addr : " + c['addr'] + ", Name : " + c['name'])

    elif ((str(Choice)=="B")|(str(Choice)=="b")):
        key=raw_input("Enter the Key: ")
        try:
            result=r.get(key)
            print("The Fetched Values are: " + result.decode("utf-8") )
        except:
            print("\nAn error occured. Check Key again.\n")

    elif ((str(Choice)=="Q")|(str(Choice)=="q")):
        loop=False

    else:
        print("Wrong Option\n")

print("\n.")
print("...")
print("......")
