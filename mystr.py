def cs():
    a=str(input("enter your servername-"))
    b=str(input("enter your dbname-"))
    c=str(input("enter your username-"))
    d=str(input("enter your password-"))
    return ["servername=%s;dbname=%s;username=%s;password=%s"%(a,b,c,d)]
def main():
    print(cs())
    return
    
