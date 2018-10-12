currency_str_value= input("请输入带单位的货币金额(CNY/USD):")
if currency_str_value[-1] in ["Y"]:
       USD = int((eval(currency_str_value[0:-3]) /6.829))
       print("人名币{}转换为美元是：{}$".format(currency_str_value[0:-3],USD))
elif currency_str_value[-1] in ["D"]:
       CNY = int(eval(currency_str_value[0:-3])*6.829)
       print("美元{}转换为人名币是：{}￥".format(currency_str_value[0:-3],CNY))
else:
       print("输入格式错误")
