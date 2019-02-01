#Importing libraries
import bs4
import requests
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#Making the Search Request Ready
s=input("Enter a keyword::")
s.replace(" ","+")
try:
    #Google Search Query
    res=requests.get("https://www.google.com/search?q="+s+"&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiIgLS97M7fAhVFeisKHYflAkwQ_AUIDigB&biw=1920&bih=585")
    
    #Using bs4 to find the first image in the page content
    soup=bs4.BeautifulSoup(res.text,"lxml")
    links=soup.find_all("img")
    
    #Showing result in form of image using matplotlib
    f=open("1.jpg","wb")
    f.write(requests.get(links[0]['src']).content)
    f.close()
    img=mpimg.imread("1.jpg")
    imgplot = plt.imshow(img)
    plt.show()
except:
    print("Some Glitch Occured,Try Again!!!")