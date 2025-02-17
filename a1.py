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
    print("Your system login name is: ",end="") 
    print(a1.login(first,second,id_number)) 
    
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
testing_string()