s = input()
p = input()

new_s = s + s
# print(new_s)
for i in range(len(new_s)):
    if new_s[i] == p[0]:
        # print(new_s[i],i,p,new_s[i:i+len(p)])
        if p == new_s[i:i+len(p)]:
            print("Yes")
            exit()

print("No")