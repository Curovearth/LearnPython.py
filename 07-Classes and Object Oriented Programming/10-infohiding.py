class infoHiding():
    def __init__(self):
        self.visible = 'Look at me'
        self.__alsoVisisble__ = 'Look at me too'
        self.__invisible = 'Don\'t look at me directly'

    def printVisible(self):
        print(self.visible)
    def printInvisible(self):
        print(self.__invisible)
    def __printInvisible(self):
        print(self.__invisible)
    def __printInvisible__(self):
        print(self.__invisible)

s = infoHiding()
s.printInvisible()      # Don't look at me directly
s.printVisible()        # Look at me
s.__printInvisible()    # AttributeError: 'infoHiding' object has no attribute '__printInvisible'
s.__printInvisible__()  # Don't look at me directly