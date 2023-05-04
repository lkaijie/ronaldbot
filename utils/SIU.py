import asyncio


class RonaldoHimself():
    def __init__(self):
        pass


    async def SIUUUUUUUUU(self, string) -> bool:
        arr = ["s","i","u"]
        index = []
        string = list(string.lower())
        value = 0
        SIUUUUUUUUU = False
        for x in range(len(string)):
            if value == 3:
                break
            if string[x] == arr[value]:
                value += 1
                index.append(x)
        if value == len(arr):
            SIUUUUUUUUU = True
        else:
            pass
        for x in index:
            string[x] = string[x].capitalize()
        string = "".join(string)
        try:
            string = await self.add_spaces(string)
        except:
            pass
        # if SIUUUUUUUUU:
        #     pass
        return SIUUUUUUUUU, index, string
    
    async def add_spaces(self,s):
        result = s[0]
        for i in range(1, len(s)):
            if s[i].isupper() and s[i-1].islower():
                result += '  '
            elif s[i].islower() and s[i-1].isupper():
                result += '  '
            result += s[i]
        return result

if __name__ == "__main__":
    # print("False: "+(SIUUUUUUUUU("iubwef"))[0])
    # print("True: "+(SIUUUUUUUUU("swiuegfiowihegfu"))[0])
    # a = SIUUUUUUUUU("swiuegfiowihegfu")
    # print(a[1])
    
    cr7 = RonaldoHimself()
    test = asyncio.run(cr7.SIUUUUUUUUU("swiuegfiowihegfu"))
    print(test)
    # print(cr7.SIUUUUUUUUU("swiuegfiowihegfu"))