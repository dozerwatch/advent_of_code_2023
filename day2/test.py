s= "Name1=Value1;Name2=Value2;Name3=Value3"
print(dict(item.split("=") for item in s.split(";")))