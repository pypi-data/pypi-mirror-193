
from abc import ABC, abstractmethod



class ProxyRotator:
    
    def __init__(self, size: int):
        self._front = None
        self._rear = None
        self._size = size
    
    async def next(self):
        self.rotate()
        return self._front

    def rotate(self):
        pass
    
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def terminate(self):
        pass
        


class EC2ProxyRotator:
    pass



# this -> aws -> proxy server (nginx)





# - generalize th
# - cycle in (base)
# - cycle out (base)
# - start (base, inherit)
# - terminate (base, inherit)
# - next
# - rotate



# limit number of containers
# rotate until completely full
# then rotate out one and replace it with another
# offer options to grow and shrink the ProxyQueue,
# so you dont have to stop all containers 

# maybe set up a script in ec2 nginx that can hit my
# proxy rotator and that changes the running list o
# active proxies

# and then my app can hit the container


# initialize
#     - 

