color = {'black' : 'k', 'green':'g', 'red':'r'};
ls = {'solid' : '-', 'dashed' : '--', 'dashed dot' : '-.'};
marker = {'point' : '.', 'circle' : 'o', 'triangle_up' : '^'};
lst = [color, ls, marker];

for i in range(len(lst)):
    for k,v in lst[i].items():
        print(k, v);
