root=input("Enter root role Name: ")
print(root)
lv1=[]
lv2=[]
lv3=[]
lv4=[]
lv5=[]
lv=[]
lv1.append(root)
lv6={}
name1=[]
name2=[]
name3=[]
name4=[]
name5=[]
name6=[]
count=0
fromTop=0

while True:
    value=input('''Operations:
        1. Add Sub Role
        2. Display Roles
        3. Delete Role
        4. Add User
        5. Display Users
        6. Display Users and Sub Users
        7. Delete User
        8. Number of users from top
        9. Height of role hierarchy
        10.Common boss of users
    Operation to be performed: ''')



    
    if value=="1":
        sub=input("Enter sub role name: ")
        reporting=input("Enter reporting to role name: ")
        for i in lv1:
            if reporting==i:
                lv2.append(sub)
        for i in lv2:
            if reporting==i:
                lv3.append(sub)
        for i in lv3:
            if reporting==i:
                lv4.append(sub)
        for i in lv4:
            if reporting==i:
                lv5.append(sub)
        
        
        
    elif value=="2":
        lv.extend(lv1)
        lv.extend(lv2)
        lv.extend(lv3)
        lv.extend(lv4)
        lv.extend(lv5)
        for i in lv:
            print(i,end=" ")

        print("")

    elif value=="3":
        delete=input("Enter the role to be deleted: ")
        transform=input("Enter the role to be transformed: ")
        for i in lv1:
            if delete==i:
                lv1.remove(delete)
                lv1.append(transform)
            elif transform==i:
                lv1.remove(transform)
        for i in lv2:
            if delete==i:
                lv2.remove(delete)
                lv2.append(transform)
            elif transform==i:
                lv2.remove(transform)
        for i in lv3:
            if delete==i:
                lv3.remove(delete)
                lv3.append(transform)
            elif transform==i:
                lv3.remove(transform)
        for i in lv4:
            if delete==i:
                lv4.remove(delete)
                lv4.append(transform)
            elif transform==i:
                lv4.remove(transform)
        for i in lv5:
            if delete==i:
                lv5.remove(delete)
                lv5.append(transform)
            elif transform==i:
                lv5.remove(transform)
        
    elif value=="4":
        user=input("Enter User Name: ")
        role=input("Enter Role: ")
        lv6[user]=role
        
    elif value=="5":
        for i in lv6:
            print(i,"-",lv6[i])
    elif value=="6":
        for i in lv6:
            for j in lv1:
                if lv6[i]==j:
                    name1.append(i)
            for k in lv2:
                if lv6[i]==k:
                    name2.append(i)
            for l in lv3:
                if lv6[i]==l:
                    name3.append(i)
            for m in lv4:
                if lv6[i]==m:
                    name4.append(i)
            for n in lv5:
                if lv6[i]==n:
                    name5.append(i)
        
        for o in name1:
            for p in name2:
                if p not in name6:
                    name6.append(p)
            for q in name3:
                if q not in name6:
                    name6.append(q)
            for r in name4:
                if r not in name6:
                    name6.append(r)
            for s in name5:
                if s not in name6:
                    name6.append(s)
        for o in name1:
            print(o,"-",end=" ")
            for i in name6:
                print(i,",",end=" ")
        
        print("")
        name6.clear()
        for o in name2:
            for p in name3:
                if p not in name6:
                    name6.append(p)
            for q in name4:
                if q not in name6:
                    name6.append(q)
            for r in name5:
                if r not in name6:
                    name6.append(r)
        for o in name2:
            print(o,"-",end=" ")
            for i in name6:
                print(i,",",end=" ")
            print("")
        name6.clear()
        for o in name3:
            for p in name4:
                if p not in name6:
                    name6.append(p)
            for q in name5:
                if q not in name6:
                    name6.append(q)
        for o in name3:
            print(o,"-",end=" ")
            for i in name6:
                print(i,",",end=" ")
            print("")
        name6.clear()
        for o in name4:
            for p in name5:
                if p not in name6:
                    name6.append(p)
        for o in name4:
            print(o,"-",end=" ")
            for i in name6:
                print(i,",",end=" ")
            print("")
        name6.clear()
        for o in name5:
            print(o,"-")
            print("")
    elif value=="7":
        deleteuser=input("Enter user to be deleted: ")
        lv6.pop(deleteuser)
        
        name1.clear()
        name2.clear()
        name3.clear()
        name4.clear()
        name5.clear()
        name6.clear()
        for i in lv6:
            for j in lv1:
                if lv6[i]==j:
                    if i not in name1:
                        name1.append(i)
            for k in lv2:
                if lv6[i]==k:
                    if i not in name2:
                        name2.append(i)
            for l in lv3:
                if lv6[i]==l:
                    if i not in name3:
                        name3.append(i)
            for m in lv4:
                if lv6[i]==m:
                    if i not in name4:
                        name4.append(i)
            for n in lv5:
                if lv6[i]==n:
                    if i not in name5:
                        name5.append(i)
        
        name6.clear()
        for o in name1:
            for p in name2:
                if p not in name6:
                    name6.append(p)
            for q in name3:
                if q not in name6:
                    name6.append(q)
            for r in name4:
                if r not in name6:
                    name6.append(r)
            for s in name5:
                if s not in name6:
                    name6.append(s)
        for o in name1:
            print(o,"-",end=" ")
            for i in name6:
                print(i,",",end=" ")
            print("")

        name6.clear()
        for o in name2:
            for p in name3:
                if p not in name6:
                    name6.append(p)
            for q in name4:
                if q not in name6:
                    name6.append(q)
            for r in name5:
                if r not in name6:
                    name6.append(r)
        for o in name2:
            print(o,"-",end=" ")
            for i in name6:
                print(i,",",end=" ")
            print("")
        name6.clear()
        for o in name3:
            for p in name4:
                if p not in name6:
                    name6.append(p)
            for q in name5:
                if q not in name6:
                    name6.append(q)
        for o in name3:
            print(o,"-",end=" ")
            for i in name6:
                print(i,",",end=" ")
            print("")
        name6.clear()
        for o in name4:
            for p in name5:
                if p not in name6:
                    name6.append(p)
        for o in name4:
            print(o,"-",end=" ")
            for i in name6:
                print(i,",",end=" ")
            print("")
        name6.clear()
        for o in name5:
            print(o,"-")
            print("")
        
    elif value=="8":
        level=input("Enter user name: ")
        for i in name1:
            if level==i:
                break
            else:
                fromTop=fromTop+1
                for j in name2:
                    if level==j:
                        break
                    else:
                        fromTop=fromTop+1
                        for k in name3:
                            if level==k:
                                break
                            else:
                                fromTop=fromTop+1
                                for l in name4:
                                    if level==l:
                                        break
                                    else:
                                        fromTop=fromTop+1
                                        for m in name5:
                                            if level==m:
                                                break
                                            else:
                                                fromTop=fromTop+1
                        
                    
        
        print("Number of users from top:",fromTop)
        
    elif value=="9":
        if len(lv1)!=0:
            count=count+1
        if len(lv2)!=0:
            count=count+1
        if len(lv3)!=0:
            count=count+1
        if len(lv4)!=0:
            count=count+1
        if len(lv5)!=0:
            count=count+1
        print("Height -",count)
        
    elif value=="10":
        user1=input("Enter user 1:")
        user2=input("Enter user 2:")
        print("Top most common boss:",name1[0])
    else:
        print("Invalid Input")
        
    
        
            
        
            
           
                    
                
    
