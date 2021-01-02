def countAndSay(n):

    def count(n):
        splitted = list(str(n)) 

        val = {}
        for w in splitted:
            if w not in val:
                val[w]=1
            else:
                val[w]+=1
        
        ans = ''
        
        # print("".join([k,v for k,v in val.items()]))


        for k,v in val.items():
            # print()
            ans += str(v)+str(k)

        print(ans)

    count(n)


print('sol',countAndSay(1113213211))