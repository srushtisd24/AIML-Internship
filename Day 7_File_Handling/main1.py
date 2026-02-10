try:
    file = open("example.txt","r")
    print(file.read())
except Exception as e:
     print(f"Error : {e}")
finally:
    file.close()
    