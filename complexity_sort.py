import random
import matplotlib.pyplot as plt

count1=0
count2=0

#INSERTION SORT
def insertion_sort(tab, size ):
  global count1
  for i in range(1,size):
    count1=count1+1
    key=tab[i]
    j = i-1
    count1+=1
    while(j>=0 and tab[j]>key):
      count1=count1+2
      tab[j+1]= tab[j]
      j = j-1
    count1+=1
    tab[j+1]= key


# MERGE SORT

#merge
def merge (tab, start,mid,end):
  global count2

  temp = []
  i=start
  j=mid+1

  count2+=1

  while( i<=mid and j <=end):
    count2+=1
    if(tab[i]<=tab[j]):
      temp.append(tab[i])
      i+=1
      count2+=1
    else:
      temp.append(tab[j])
      j+=1
      count2+=1

  count2+=1
  while (i<=mid):
    temp.append(tab[i])
    i+=1
    count2+=1

  count2+=1
  while (j<=end):
    temp.append(tab[j])
    j+=1
    count2+=1

  l=0
  count2+=2
  for k in range (start,end+1):
    tab[k] =temp[l]
    l+=1
    count2+=1

#merge sort
def merge_sort(tab,start,end):
  global count2
  count2+=1
  if(start<end):
    mid=(start+end)//2
    count2+=1
    merge_sort(tab,start,mid)
    merge_sort(tab,mid+1,end)

    merge(tab,start,mid,end)

#make a random table, sort and return the number of executions.
size = [5,10,100,200,400,800,1000]
count_merge=[]
count_insertion=[]

for i in size:
  tab =[random.randint(1,1000) for _ in range(i)]
  count1=0
  count2=0
  tab_merge= tab.copy()
  tab_insertion= tab.copy()

  insertion_sort(tab_insertion,len(tab_insertion))
  count_insertion.append(count1)

  merge_sort(tab_merge,0,len(tab_merge)-1)
  count_merge.append(count2)

#1st graph
plt.figure()
plt.plot(size,count_insertion,label="insertion sort",color="blue")

plt.plot(size,count_merge,label="merge sort", color="green")

plt.xlabel("size")
plt.ylabel("complexity (number of instructions")

plt.title("complexity comparison")
plt.legend()
plt.grid(True)
plt.savefig("complexity.png")
plt.show()
