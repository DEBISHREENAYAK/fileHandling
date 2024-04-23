if _name_ == '_main_':
    
#type1    
    try:
        f = open('text.txt',"r")
        print(f.readlines())
    except Exception as e:
        print(e)
    finally:
        f.close()
        print('File closed!!')
        
#no memory lickes
#type 2

        try:
            with open('text.txt',"r") as file:
                print(file.readline())
        except Exception as e:
               print(e)
             
#type 3
        try:
            with open('text2.txt',"r") as file1, open('text3.txt',"r") as file2:
                # file1.writelines("helloo")
                # file2.writelines("hiiiii")
                print(file1.readline())
                print(file2.readline())
        except Exception as e:
            print(e)
