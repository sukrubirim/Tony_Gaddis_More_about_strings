def counts_Ts():
    count=0 
    my_string=input("Enter a stirng: ") 
    for ch in my_string: 
        if ch=="T" or ch=="t": 
            count+=1 
    print(f"The letter T appears {count} times.") 

def checkpoint():
    name="Julia" 
    for ch in name: 
        print(ch) 

def str_slice(): 
    full_name="Patty Lynn Smith" 
    first_name=full_name[:5] 
    middle_name=full_name[6:10] 
    last_name=full_name[11:] 
    print(first_name,middle_name,last_name,sep=" ") 

def login(first,last,id_number): 
    set1=first[:3] 
    set2=last[:3] 
    set3=id_number[-3:] 
    login_name=set1+set2+set3 
    return login_name 

def main(): 
    import a1 
    first=input("Enter your first name: ") 
    second=input("Enter your last name: ") 
    id_number=input("Enter your id number: ") 
    pasword=a1.login(first,second,id_number)
    print("Your system login name is: ",end="") 
    print(pasword)
    return pasword

def testing_string(): 
    user_string=input("Enter a string: ") 
    print("This is what I found about string: ") 
    test_list=["user_string.isalnum()","user_string.isdigit()","user_string.isalpha()","user_string.isspace()","user_string.islower()","user_string.isupper()"] 
    test_results=["is alphanumeric","digits","alphabetic characters","whitespace characters","lowercase","uppercase"] 
    for case in test_list: 
        if eval(case): 
            if test_list.index(case) in [0]: 
                print(f'The string is {test_results[test_list.index(case)]}.') 
            elif test_list.index(case) in [1,2,3]: 
                print(f'The string contains only {test_results[test_list.index(case)]}.') 
            elif test_list.index(case) in [4,5]: 
                print(f'The letters in the string are all {test_results[test_list.index(case)]}.')

def valid_password():
    import a1
    password=a1.main()
    correct_length=False
    has_uppercase=False
    has_lowercase=False
    has_digit=False
    if len(password)>=7:
        correct_length=True
        for ch in password:
            if ch.isupper():
                has_uppercase=True
            if ch.islower():
                has_lowercase=True
            if ch.isdigit():
                has_digit=True
    if correct_length and has_uppercase and has_lowercase and has_digit:
        print("That password is valid.")
    else:
        print("That password is not valid.")
        valid_password()
        
def repetition_operator():
    for count in range(1,19):
        if count<=9:
            print("Z"*count)
        elif count>=10:
            print("Z"*(19-count))

def x_x():
    csv_file=open("test_scores.csv","r")
    lines=csv_file.readlines()
    csv_file.close()    
    return_list=[]
    for index in range(len(lines)):
        lines[index]=lines[index].rstrip("\n")
    i=lines[0]
    if "," in i:
        j=","
    else:
        j=";"
    for line in lines:
        line=line.split(j)
        return_list+=line
    csv_file=open("test_scores.csv","w")
    count=0
    for item in return_list:
        count+=1
        if count not in list(range(5,30,5)):
            csv_file.write(str(item)+";")
        else:
            csv_file.write(str(item)+"\n")
    csv_file.close()
        
def test_averages():
    cvs_file=open("test_scores.csv","r")
    lines=cvs_file.readlines()
    cvs_file.close()
    for line in lines:
        tokens=line.split(";")
        total=0.0
        for token in tokens:
            total+=float(token)
        average=total/len(tokens)
        print(f"Average: {average}")

def check_points():
    my_string="Deep learning is important for AI."
    if "d" in my_string.lower():
        print("The string 'd' was found.")
    else:
        print("The string 'd' was not found.")
    big="strings"
    little=big.upper()
    print(little)
    my_string="apbr316269"
    if my_string.isalnum():
        print("Digit")
    else:
        print("No digit.")
    ch = 'a'
    ch2 = ch.upper()
    print(ch, ch2)
    again="r"
    while again.lower() in ["r","q"]:
        again=input("Do you want to repeat the program or quit? (R/Q) ")
    var = '$'
    print(var.upper())
    my_string="AbnbdCdjkeDefGHJ"
    uppercase_count=0
    for ch in my_string:
        if ch.isupper():
            uppercase_count+=1
    print(uppercase_count)    
    days="Monday Tuesday Wednesday"
    print(days.split(" "))
    values="one$two$three$four"
    print(values.split("$"))
    choice="y"
    if choice.lower()=="y":
        print("That worked.")
    string_1="Abcde fgh ivy z"
    string_count_1=0
    string_count_2=0
    string_count_3=0
    for ch in string_1:
        if ch==" ":
            string_count_1+=1
        if ch.isalnum():
            string_count_2+=1
        if ch.islower():
            string_count_3+=1
    print(string_count_1)
    print(string_count_2)
    print(string_count_3)
    string_2="https://youtube.com"
    def begin_https(string_2):
        if string_2.startswith("https"):
            print("This string start with 'https'.")
    begin_https(string_2)
    string_3="Tradational text textures changes after times."
    t_index_list=[]
    total_ch_count_list=[]
    index_count=0
    for ch in string_3:
        if ch.lower()=="t":
            t_index_list.append(index_count)
        index_count+=1
    for index in t_index_list:
        total_ch_count=0
        count=0
        max_value=len(string_3)
        min_value=0
        while not max_value-count==index:
            print(string_3[index:max_value-count])    
            total_ch_count+=1
            count+=1
        count=0
        while not min_value+count==index:
            print(string_3[min_value+count:index+1])
            total_ch_count+=1
            count+=1
        total_ch_count_list.append(total_ch_count)
        print()
    print(t_index_list,total_ch_count_list,sep=" ")
    def backwards(my_string):
        print(my_string)
        print(my_string[::-1])
        print(my_string[:3])
        print(my_string[-3:])
    backwards(my_string)
    levels="Beginner, Average, Advanced, Expert"
    print(levels.split(", "))
    
  


















check_points()




























