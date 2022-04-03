from colorama import init, Fore, Back, Style
init(autoreset=True)    #  初始化，并且设置颜色设置自动恢复
class Colored(object):
    def magenta(self, s):
        return Style.BRIGHT+Fore.MAGENTA+s+Fore.RESET+Style.RESET_ALL
    def green(self, s):
        return Style.BRIGHT+Fore.GREEN+s+Fore.RESET+Style.RESET_ALL
    def white(self, s):
        return Fore.WHITE+s+Fore.RESET+Style.RESET_ALL
    def cyan(self, s):
        return Style.BRIGHT+Fore.CYAN+s+Fore.RESET+Style.RESET_ALL
    def ccyan(self, s):
        return Fore.CYAN+s+Fore.RESET+Style.RESET_ALL
    def yellow(self, s):
        return Style.BRIGHT+Fore.YELLOW+s+Fore.RESET+Style.RESET_ALL
    def red(self, s):
        return Style.BRIGHT+Fore.RED+s+Fore.RESET+Style.RESET_ALL
    def purple(self, s): 
        return(Style.BRIGHT+Fore.BLUE + str(s) + Fore.RESET+Style.RESET_ALL)
    def yeinfo(self):
        return Style.BRIGHT+Fore.YELLOW+"[INFO]"+Fore.RESET+Style.RESET_ALL
    def rewarn(self):
        return Style.BRIGHT+Fore.RED+"[WARN]"+Fore.RESET+Style.RESET_ALL



color = Colored()
if __name__ == "__main__":
	print(color.magenta("i_need_you"))
	print(color.green("i_need_you"))
	print(color.white("i_need_you"))
	print(color.cyan("i_need_you"))
	print(color.ccyan("i_need_you"))
	print(color.yellow("i_need_you"))
	print(color.red("i_need_you"))
	print(color.purple("i_need_you"))
	print(color.yeinfo())
	print(color.rewarn())
