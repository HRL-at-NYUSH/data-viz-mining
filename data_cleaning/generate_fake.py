def proc(a):
    percent = 0.05
    i = 0
    import random
    while i<len(a)*percent:
        p = random.randint(0,len(a)-1)
        while a[p]==' ':
            p = random.randint(0,len(a)-1)
        letter = chr(random.randint(97,97+25))
        a = a[0:p]+letter+a[p+1:]
        i+=1

    a = a.split(' ')
    t = random.randint(0,len(a)-1)
    a.insert(t,str(random.randint(0,100)))
    a = ' '.join(a)

    p = random.randint(0,3)
    if p>0:
        s = a[0].lower()
        s2 = a[1].lower()
        a = s2+s+a[2:]
    return(a)


with open('jobrecords.txt','r',encoding='utf-8') as f:
    a = f.readlines()
with open('group.txt','r',encoding='utf-8') as f:
    b = f.readlines()
i = 0
with open('out.txt','w',encoding='utf-8') as f:
    f.write('\n')
while i<=10:#len(a)-1:
    job_name = a[i]
    job_name_index = job_name.split('#')[0]
    job_name_name = job_name.split('#')[1].replace(',',' of the')
    proc1 = proc(job_name_name.replace('\n',''))
    first = job_name_index[0]
    second = job_name_index[0:2]
    third = job_name_index[0:3]
    fourth = job_name_index
    string =proc1+'\t'+job_name_name.replace('\n','')+'\t'
    for group in b:
        if 'Major Group '+first+":" in group:
            string +=(group.replace('\n','').split(':')[1].lower())
        elif 'Sub-Major Group '+second+':' in group:
            string = string +'\t'+(group.replace('\n','').split(':')[1].lower())
        elif 'Minor Group '+third+':'  in group:
            string = string +'\t'+(group.replace('\n','').split(':')[1].lower())
        elif 'Unit Group '+fourth+':'  in group:
            string = string +'\t'+(group.replace('\n','').split(':')[1].lower())
    string = string+'\n'
    with open('out.txt','a',encoding='utf-8') as f:
        f.write(string)
    i+=1




