
#----------------------------------
#----------------------------------
#            Imports
#----------------------------------
#----------------------------------
import decimal
import math
from decimal import Decimal

#----------------------------------
#----------------------------------
#            Vectors
#----------------------------------
#----------------------------------

class RG_Vector2D:
    
    # ----------------------------------
    #            Variables:
    # ----------------------------------
    _length:Decimal = Decimal(0.0);
    X:Decimal = Decimal(0.0);
    Y:Decimal = Decimal(0.0);
    
    # ----------------------------------
    #             Base Functions:
    # ----------------------------------
    # Constructor
    def __init__(self, x:Decimal = Decimal(0.0), y:Decimal = Decimal(0.0)) -> None:
        
        # Initializing X and Y.
        self.X = Decimal(x);
        self.Y = Decimal(y);
        
        # Initializing the length.
        self.GetLength();
        pass;
        
    # To String
    def __str__(self) -> str:
        return "Vector 2D: (X: "+str(self.X) + ", Y: " + str(self.Y) + ")"
    
    # Equals
    def __eq__(self, other) -> bool:
        if(not type(other) is RG_Vector2D): return False;
        return other.X == self.X and other.Y ==  self.Y;
    
    #------------------------------------
    #             Functions:
    # -----------------------------------
    
    def ToVector(self):
        return self
    
    def ToVelocity(self):
        return RG_Velocity2D(self.X, self.Y)
    
    def GetLength(self) -> Decimal:
        # Get length squared
        LengthSqr = self.GetlengthSqr();

        # Check if anything changedS
        if(self._length * self._length == LengthSqr):
            return self._length;

        # Otherwise complete the square rooting of the length and store the result.
        self._length = Decimal.sqrt(Decimal(LengthSqr));
        return self._length;

    def GetlengthSqr(self) -> Decimal:
        return self.X * self.X + self.Y * self.Y;

    def SetLength(self, newLength):
        length = self.GetLength();
        if(newLength == length):
            return;
        if(length == 0):
            raise Exception("Cannot set the length of the 0 vector or a velocity with the speed of 0 to any other value than 0.")
        self.NormalizeOpt(length);
        h = self * newLength;
        self.X = h.X;
        self.Y = h.Y;
        self._length = h._length;
        pass;

    def Normalize(self):
        length = self.GetLength();
        if(length == 0):
            raise Exception("Cannot normalize the 0 vector or a velocity with the speed of 0.")
        h = self / length;
        self.X = h.X;
        self.Y = h.Y;
        pass;

    def NormalizeOpt(self, length):
        if(length == 0):
            raise Exception("Cannot normalize the 0 vector or a velocity with the speed of 0.")
        h = self / length;
        self.X = h.X;
        self.Y = h.Y;
        pass
    
    def DotProduct(self, other):
        return other.X * self.X + other.Y * self.Y
    
    # ----------------------------------
    #       Operator Overloading:
    # ----------------------------------
    # Plus: +
    def __add__(self, Right):
        
        self.Y = Decimal(self.Y)
        self.X = Decimal(self.X)
        
        # Get Type.
        tp = type(Right);
        
        # If point then return point
        if(tp is RG_Point2D or tp is RG_Position2D):
            x = self.X + Decimal(Right.X);
            y = self.Y + Decimal(Right.Y);
            return RG_Point2D(x, y);
        
        # If vector then return vector.
        elif(tp is RG_Vector2D or tp is RG_Velocity2D):
            x = self.X + Decimal(Right.X);
            y = self.Y + Decimal(Right.Y);
            return RG_Vector2D(x, y);
        
        # Otherwise it is not a compatible correct type so a type error will be raised:
        raise TypeError("You can only add vectors with Points or other vectors (with the same number of dimensions)."+str(tp));
    
    # Subtract: -
    def __sub__(self, Right):
        
        self.Y = Decimal(self.Y)
        self.X = Decimal(self.X)
        
        # Get Type.
        tp = type(Right);
        
        # If point then return point
        if(tp is RG_Point2D):
            x = self.X - Decimal(Right.X);
            y = self.Y - Decimal(Right.Y);
            return RG_Point2D(x, y);
        
        # If vector then return vector.
        elif(tp is RG_Vector2D):
            x = self.X - Decimal(Right.X);
            y = self.Y - Decimal(Right.Y);
            return RG_Vector2D(x, y);
        
        # Otherwise it is not a compatible correct type so a type error will be raised:
        raise TypeError("You can only take away vectors with Points or other vectors (with the same number of dimensions).");
    
    # Multiply: *
    def __mul__(self, Right):
        
        
        self.Y = Decimal(self.Y)
        self.X = Decimal(self.X)
        
        # Get Type.
        tp = type(Right);
        # If num then do num multiplication
        if(tp is float or tp is int ):
            x = self.X * Decimal(Right);
            y = self.Y * Decimal(Right);
            return RG_Vector2D(x, y);
        if(tp is Decimal ):
            x = self.X * Right;
            y = self.Y * Right;
            return RG_Vector2D(x, y);
        
        # If vector then do vector multiplication
        elif(tp is RG_Vector2D):
            x = self.X * Decimal(Right.X);
            y = self.Y * Decimal(Right.Y);
            return RG_Vector2D(x, y);
        
        # Otherwise it is not a compatible correct type so a type error will be raised:
        raise TypeError("You can only multiply vectors by intigers, floats, Decimal, and other vectors (with the same number of dimensions)."+str(tp));
    
    # Divide: /
    def __truediv__(self, Right):
        
        
        self.Y = Decimal(self.Y)
        self.X = Decimal(self.X)
        
        # Get Type.
        tp = type(Right);
        
        # If num then do num devision
        if(tp is float or tp is int or tp is decimal.Decimal):
            x = self.X / Decimal(Right);
            y = self.Y / Decimal(Right);
            return RG_Vector2D(x, y);
        
        # If vector then do vector division
        elif(tp is RG_Vector2D):
            x = self.X / Decimal(Right.X);
            y = self.Y / Decimal(Right.Y);
            return RG_Vector2D(x, y);
        
        # Otherwise it is not a compatible correct type so a type error will be raised:
        raise TypeError("You can only divide vectors by intigers, floats, Decimal, and other vectors (with the same number of dimensions).");
    
    # Floor Divide: //
    def __floordiv__(self, Right):
        
        self.Y = Decimal(self.Y)
        self.X = Decimal(self.X)
        # Get Type.
        tp = type(Right);
        
        # If num then do num floor division
        if(tp is float or tp is int or tp is decimal.Decimal):
            x = self.X // Decimal(Right);
            y = self.Y // Decimal(Right);
            return RG_Vector2D(x, y);
        
        # If vector then do vector floor division
        elif(tp is RG_Vector2D):
            x = self.X // Decimal(Right.X);
            y = self.Y // Decimal(Right.Y);
            return RG_Vector2D(x, y);
        
        # Otherwise it is not a compatible correct type so a type error will be raised:
        raise TypeError("You can only floor divide vectors by integers, floats, Decimal, and other vectors (with the same number of dimensions).");
    
    # Modulus: %
    def __mod__(self, Right):
        
        self.Y = Decimal(self.Y)
        self.X = Decimal(self.X)
        # Get Type.
        tp = type(Right);
        
        # If num then do num modulus
        if(tp is float or tp is int or tp is decimal.Decimal):
            x = self.X % Decimal(Right);
            y = self.Y % Decimal(Right);
            return RG_Vector2D(x, y);
        
        # If vector then do vector modulus
        elif(tp is RG_Vector2D):
            x = self.X % Decimal(Right.X);
            y = self.Y % Decimal(Right.Y);
            return RG_Vector2D(x, y);
        
        # Otherwise it is not a compatible correct type so a type error will be raised:
        raise TypeError("You can only modulus vectors by integers, floats, Decimal and other vectors (with the same number of dimensions).");
    
    pass;

class RG_Velocity2D(RG_Vector2D):

    # ----------------------------------
    #           Base Functions:
    # ----------------------------------
    # Constructor
    def __init__(self, x:Decimal = Decimal(0.0), y:Decimal = Decimal(0.0)):
        super().__init__(x, y)
        pass;
    
    # To String
    def __str__(self)  -> str:
        return "Velocity: (X: "+str(self.X) + ", Y: " + str(self.Y) + ")"
    
    # Equals
    def __eq__(self, other:RG_Vector2D) -> bool:
        return other.X == self.X and other.Y ==  self.Y;
    
    # ----------------------------------
    #             Wrappers:
    # ----------------------------------
    def SetSpeed(self, speed):
        self.SetLength(Decimal(speed));

    def GetSpeed(self):
        return float(self.GetLength());
    
    def ToVector(self):
        return RG_Vector2D(self.X, self.Y);
    
    def ToVelocity(self):
        return self
    
    def __add__(self, Right):
        t = type(Right)
        if(t is RG_Velocity2D):
            Right = Right.ToVector()
        if(t is RG_Position2D):
            Right = Right.ToPoint()
        vec = super().__add__(Right)
        if (t is RG_Position2D):
            return RG_Position2D(vec.X,vec.Y)
        if (t is RG_Point2D):
            return RG_Point2D(vec.X,vec.Y)
        
        return RG_Velocity2D(vec.X,vec.Y)
    
    def __sub__(self, Right):
        t = type(Right)
        if(t is RG_Velocity2D):
            Right = Right.ToVector();
        if(t is RG_Position2D):
            Right = Right.ToPoint();
        vec = super().__sub__(Right)
        if (t is RG_Position2D):
            return RG_Position2D(vec.X,vec.Y)
        if (t is RG_Point2D):
            return RG_Point2D(vec.X,vec.Y)
        
        return RG_Velocity2D(vec.X,vec.Y)
    
    def __mul__(self, Right):
        vec = super().__mul__(Right)
        return RG_Velocity2D(vec.X,vec.Y)
    
    def __truediv__(self, Right):
        vec = super().__truediv__(Right)
        return RG_Velocity2D(vec.X,vec.Y)
    
    def __floordiv__(self, Right):
        vec = super().__floordiv__(Right)
        return RG_Velocity2D(vec.X,vec.Y)
    
    def __mod__(self, Right):
        vec = super().__mod__(Right)
        return RG_Velocity2D(vec.X,vec.Y)
    
    pass;


#----------------------------------
#----------------------------------
#            Points
#----------------------------------
#----------------------------------

class RG_Point2D:
    
    # ----------------------------------
    #            Variables:
    # ----------------------------------
    X:Decimal = Decimal(0.0);
    Y:Decimal = Decimal(0.0);
    
    # ----------------------------------
    #          Base Functions:
    # ----------------------------------
    # Constructor
    def __init__(self, x:Decimal = 0.0, y:Decimal = 0.0) -> None:
        self.X = Decimal(x);
        self.Y = Decimal(y);
        pass;
    
    # To String
    def __str__(self)  -> str:
        return "Point: (X: "+str(self.X) + ", Y: " + str(self.Y) + ")"
    
    # Equals
    def __eq__(self, other) -> bool:
        if(not type(other) is RG_Point2D): return False;
        return other.X == self.X and other.Y ==  self.Y;
    
    
    def ToPosition(self):
        return RG_Position2D(self.X, self.Y);
    
    def ToPoint(self):
        return self;
    
    # ----------------------------------
    #       Operator Overloading:
    # ----------------------------------
    # Plus: +
    def __add__(self, Right):
        
        self.Y = Decimal(self.Y)
        self.X = Decimal(self.X)
        
        # If not vector then throw error
        if(not (type(Right) is RG_Vector2D or type(Right) is RG_Velocity2D)):
            raise TypeError("You can only add vectors to points (with the same number of dimensions)."+str(type(Right)));
        
        # Otherwise complete the addition
        x = self.X + Decimal(Right.X);
        y = self.Y + Decimal(Right.Y);
        return RG_Point2D(x, y);
    
    # Subtract: -
    def __sub__(self, Right):
        t = type(Right)
        self.Y = Decimal(self.Y)
        self.X = Decimal(self.X)
        # If not point or vec then throw error
        
        if(t is RG_Point2D):
            x = self.X - Decimal(Right.X);
            y = self.Y - Decimal(Right.Y);
            return RG_Vector2D(x, y);
        
        elif(t is RG_Vector2D):
            x = self.X - Decimal(Right.X);
            y = self.Y - Decimal(Right.Y);
            return RG_Point2D(x, y);
        
        else:
            raise TypeError("You can only subtract points and vectors from other points (with the same number of dimensions).");
        
        # Otherwise complete the subtraction
    
    pass;

class RG_Position2D(RG_Point2D):

    # ----------------------------------
    #          Base Functions:
    # ----------------------------------
    # Constructor
    def __init__(self, x: Decimal = Decimal(0.0), y: Decimal = Decimal(0.0)) -> None:
        super().__init__(x, y)
        pass;
    
    # To String
    def __str__(self) -> str:
        return "Position: (X: "+str(self.X) + ", Y: " + str(self.Y) + ")"
    
    # Equals
    def __eq__(self, other:RG_Point2D) -> bool:
        return other.X == self.X and other.Y ==  self.Y;
    
    # ----------------------------------
    #             Functions:
    # ----------------------------------
    
    def ToPosition(self):
        return self;
    
    def ToPoint(self):
        return RG_Point2D(self.X, self.Y);
    
    def Move(self, velocity:RG_Velocity2D):
        newPos = velocity + self;
        self.X = newPos.X;
        self.Y = newPos.Y;
        
    def VectorTo(self, other) -> RG_Vector2D:
        return other - self;
    
        
    def __add__(self, Right):
        t = type(Right)
        if(t is RG_Velocity2D):
            Right = Right.ToVector();
        vec = super().__add__(Right)
        return RG_Position2D(vec.X,vec.Y)
            
    def __sub__(self, Right):
        t = type(Right)
        if(t is RG_Velocity2D):
            Right = Right.ToVector();
        if(t is RG_Position2D):
            Right = Right.ToPoint();
        vec = super().__sub__(Right)
        if (t is RG_Position2D):
            return RG_Vector2D(vec.X,vec.Y)
        if (t is RG_Point2D):
            return RG_Vector2D(vec.X,vec.Y)
        
        return RG_Position2D(vec.X,vec.Y)
 
        
    pass;

import random;

#Random
def RandomInt(min:int = 0, max:int = 100):
    random.seed();
    return random.randint(min,max);

def RandomFloat(min:int = -1, max:int = 1):
    random.seed();
    if(min < 0 and max > 0):
        val = random.random() * 2 -1;
    elif(max < 1):
        val = random.random() * -1;
    else:
        val = random.random();
    if(not(min < -1 or max > 1)): return val;
    intval = RandomInt(min,max);
    return intval + val;
class ref:
    
    Value = "Not Initialized"
    
    def __init__(self, value) -> None:
        self.Value = value;
        pass
    
    pass;
from ctypes import *
import time



class RG_Counter:
    
    def __init__(self, trigger, recurring = False) -> None:
        self._trigger = trigger;
        self._recurring = recurring;
        self._count = 0;
        pass
    
    @property
    def Finished():
        pass;
    
    @Finished.getter
    def Finished(self):
        if(self._count == -1):return False;
        
        self._count += 1;
        
        if(self._count == self._trigger): 
            
            if(not self._recurring): 
                self._count = -1;
                return True;
            
            self._count = 0;
            return True;
        
        return False; 
           
    pass;

class RG_Timer:
    def __init__(self,mainScript, done = None, trigger:int = 1) -> None:
        self.Done = done;
        self.MainScript = mainScript;
        self._trigger = trigger;
        self.Count = 0
        self._id = 0
        pass
    
    def Tick(self,deltaTime):
        self.Count += deltaTime * self.MainScript.MainPhysics.Interval;
        if(self.Count >= self._trigger and self.Done != None):
            self.Done();
            self.UnSubscribe()
        pass;
    
    def Reset(self):
        self.Count = 0
        pass;
    
    def Subscribe(self):
        self.MainScript.MainPhysics.Add(self);
        pass;
    
    def UnSubscribe(self):
        self.MainScript.MainPhysics.Remove(self);
        del self;
        pass;
    
    pass;


def IsDefined():
    global py
    try:
        a = py
    except:
        return False
    return True

def TimeInit():
    if(IsDefined()):
        return
    global tim;
    global py;
    try:
        import os
        data_path = os.path.join(os.path.dirname(__file__), 'RGame', 'Time.dll')
        tim = cdll.LoadLibrary(data_path)
        tim.Pause.argtypes = [c_double];
        #tim.PauseUntil.argtypes = [c_void_p]
        tim.Del_CRG_TimePoint.argtypes = [c_void_p]
        tim.CRG_TimePoint_Difference.argtypes = [c_void_p,c_void_p]
        tim.CRG_TimePoint_Difference.restype = c_double
        tim.CRG_TimePoint_Increament.argtypes = [c_void_p,c_double]
        tim.CRG_TimePoint_Decreament.argtypes = [c_void_p,c_double]
        tim.CRG_Now.restype = c_void_p
        py = False
    except Exception as e:
        tim = None
        py = True
        switchWarning = RG_FileExistsWarning(*e.args, "The Time.dll could not be loaded so automatically switching form C++ to Python code for time module")
        Log(switchWarning.Message, switchWarning.Value, LogLevel.WARNING)
    pass;


def Pause(length):
    global tim;
    global py;
    if(length <= 0):return;
    if(py):
        time.sleep(length)
        return
    tim.Pause(length);
    pass;


class RG_TimePoint:
    Tis = None
    pTis = None
    def Now(self):
        if not (IsDefined()):
            TimeInit()
        global tim
        global py
        if(py):
            self.pTis = time.perf_counter_ns()/1000000000
            return
        self.Tis = tim.CRG_Now()
        
    def Diff(self):
        global tim
        global py
        if(py): return time.perf_counter_ns()/1000000000 - self.pTis
        return tim.CRG_TimePoint_Difference(tim.CRG_Now(), self.Tis)
    
    def __init__(self):
        self.Now()
    
    def __del__(self):
        global tim
        global py
        if(py):return
        tim.Del_CRG_TimePoint(self.Tis)
        
    def __sub__(self, other):
        global tim
        global py
        if(py):
            if(other is RG_TimePoint):
                return self.pTis - other.pTis
            self.pTis -= other
            return
        if(other is RG_TimePoint):
            return tim.CRG_TimePoint_Difference(self.Tis, other.Tis)
        tim.CRG_TimePoint_Decreament(self.Tis, other)
        
    def __add__(self, other):
        global tim
        global py
        if(py):
            self.pTis += other
            return
        tim.CRG_TimePoint_Increament(self.Tis, other)
import random

def RGBtoColor(r:int, g:int, b:int):
    return "#%02x%02x%02x" % (r, g, b);

def RandomColor():
    random.seed()
    return "#%02x%02x%02x" % (random.randint(0,255), random.randint(0,255), random.randint(0,255));

def GetTypeStr(thing):
    return thing.__class__.__name__
    
    


class RG_Exception(Exception):
    
    Message:str = None
    
    def __init__(self, message = None) -> None:
        self.Message = message
        pass
    pass

class RG_Warning(RG_Exception):
    
    pass

class RG_TypeError(TypeError,RG_Exception):
    Message:str = "An error has ocurred."
    Value = None
    
    def __init__(self, value = None, message = None) -> None:
        self.Message = message
        self.Value = value
        pass
    pass

class RG_TypeWarning(TypeError,RG_Warning):
    Message:str = "An error has ocurred."
    Value = None
    
    def __init__(self, value = None, message = None) -> None:
        self.Message = message
        self.Value = value
        pass
    pass

class RG_ValueError(ValueError,RG_Exception):
    Message:str = "An error has ocurred."
    Value = None
    
    def __init__(self, value = None, message = None) -> None:
        self.Message = message
        self.Value = value
        pass
    pass

class RG_FileExistsError(FileExistsError,RG_Exception):
    Message:str = "An error has ocurred."
    Value = None
    
    def __init__(self, value = None, message = None) -> None:
        self.Message = message
        self.Value = value
        pass
    pass

class RG_FileExistsWarning(FileExistsError,RG_Warning):
    Message:str = "An error has ocurred."
    Value = None
    
    def __init__(self, value = None, message = None) -> None:
        self.Message = message
        self.Value = value
        pass
    pass

class RG_AccessError(RG_Exception):
    Message:str = "An error has ocurred."
    Value = None
    
    def __init__(self, value = None, message = None) -> None:
        self.Message = message
        self.Value = value
        pass
    pass

class RG_AccessWarning(RG_Warning):
    Message:str = "An error has ocurred."
    Value = None
    
    def __init__(self, value = None, message = None) -> None:
        self.Message = message
        self.Value = value
        pass
    pass

from enum import Enum
import traceback

class LogLevel(Enum):
    FATAL = 5
    ERROR = 4
    WARNING = 3
    MESSAGE = 2
    DEBUG = 1
    pass

def Log(message:str, value = None, level:LogLevel = LogLevel.DEBUG):
    match level:
        case LogLevel.FATAL:
            LogFatal(message, value)
            
        case LogLevel.ERROR:
            LogError(message, value)
            
        case LogLevel.WARNING:
            LogWarning(message, value)
            
        case LogLevel.MESSAGE:
            LogMessage(message)
            
        case LogLevel.DEBUG:
            LogDebug(message, value)
        case _:
            LogMessage(message)

def LogFatal(message, value = None):
    print()
    print(f" {GetConsoleStyle(0,7,1)}>-------------------------Error-------------------------<{EndStyle()}")
    print()
    print(f" > Level: {GetConsoleStyle(0,7,1)}Fatal{EndStyle()}")
    if not (value is None):
        print(" > Value of cause: ", value)
    print(" > Message:")
    print(GetConsoleStyle(0,1,0))
    print(message + EndStyle())
    print()
    print(" > Where the problem ocurred:")
    print()
    traceback.print_exc()
    print()
    print(f" {GetConsoleStyle(0,7,1)}>-------------------------------------------------------<{EndStyle()}")
    print()
    
    pass

def LogError(message, value = None):
    
    print()
    print(f" {GetConsoleStyle(0,1)}>-------------------------Error-------------------------<{EndStyle()}")
    print()
    print(f" > Level: {GetConsoleStyle(0,1)}Error{EndStyle()}")
    if not (value is None):
        print(" > Value of cause: ", value)
    print(" > Message:")
    print(GetConsoleStyle(3,1))
    print(message,EndStyle())
    print()
    print(" > Where the problem ocurred:")
    print()
    traceback.print_exc()
    print()
    print(f" {GetConsoleStyle(0,1)}>-------------------------------------------------------<{EndStyle()}")
    print()
    
    pass

def LogWarning(message, value = None):
    
    print()
    print(f" {GetConsoleStyle(0,3)}>------------------------Warning------------------------<{EndStyle()}")
    print()
    print(f" > Level: {GetConsoleStyle(0,3)}Warning{EndStyle()}")
    if not (value is None):
        print(" > Value of cause: ", value)
    print(" > Message:")
    print(GetConsoleStyle(3,3))
    print(message,EndStyle())
    print()
    print(" > Where the problem ocurred:")
    print()
    traceback.print_exc()
    print()
    print(f" {GetConsoleStyle(0,3)}>-------------------------------------------------------<{EndStyle()}")
    print()
    
    pass

def LogMessage(message):
    
    print()
    print(f" >------------------------Message------------------------<")
    print(" > Message:")
    print(GetConsoleStyle(3,0))
    print(message,EndStyle())
    print()
    print(" >-------------------------------------------------------<")
    print()
    
    pass


def LogDebug(message, value = None):
    
    print()
    print(f" {GetConsoleStyle(0,4)}>------------------------Debug------------------------<{EndStyle()}")
    print()
    if not (value is None):
        print(" > Value: ", value)
    print(" > Message:")
    print(GetConsoleStyle(3,4))
    print(message,EndStyle())
    print()
    print(" > Where the message ocurred:")
    print()
    traceback.print_exc()
    print()
    print(f" {GetConsoleStyle(0,4)}>-------------------------------------------------------<{EndStyle()}")
    print()
    
    pass

def GetConsoleStyle(style:int = None, color:int = None, background:int = None):
    
    if (style is None):
        style = 0
    elif not (type(style) is int):
        raise RG_TypeError(style,
                             " The argument 'style' for function 'SDL.GetConsoleStyle' must only have int inputs.")
    elif (style < 0 or style > 5):
        raise RG_ValueError(style,
                             " The argument 'style' for function 'SDL.GetConsoleStyle' must only be from 0 - 5\n To see the styles available call 'PrintConsoleStyles' (any where)")
            
    if (color is None):
        color = 7
    elif not (type(color) is int):
        raise RG_TypeError(color,
                             " The argument 'color' for function 'SDL.GetConsoleStyle' must only have int inputs.")
    elif (color < 0 or color > 7):
        raise RG_ValueError(color,
                             " The argument 'color' for function 'SDL.GetConsoleStyle' must only be from 0 - 7\n To see the colors available call 'PrintConsoleStyles' (any where)")
        
    if (background is None):
        background = 0
    elif not (type(background) is int):
        raise RG_TypeError(background,
                             " The argument 'background' for function 'SDL.GetConsoleStyle' must only have int inputs.")
    elif (background < 0 or background > 7):
        raise RG_ValueError(background,
                             " The argument 'background' for function 'SDL.GetConsoleStyle' must only be from 0 - 7\n To see the background colors available call 'PrintConsoleStyles' (any where)")
    
    escape = "\033["
    color += 30
    background += 40
    return escape + str(style) + ";" + str(color) + ";" + str(background) + "m"

def EndStyle():
    return "\033[0;37;40m"

def PrintConsoleStyles():
    print(f" {GetConsoleStyle(4)}Styles:{EndStyle()}" +"        "+ f"{GetConsoleStyle(0,6)}Colors:{EndStyle()}" + "    " + f"{GetConsoleStyle(0,0,3)}Background:{EndStyle()}")
    print(EndStyle())
    print(" "+GetConsoleStyle(0)+"Normal:    0"+EndStyle() +"  "+ f"{GetConsoleStyle(0,0,7)}Black:  0{EndStyle()}"+"  "+ f"{GetConsoleStyle(0,7,0)}Black:  0{EndStyle()}")
    print(" "+GetConsoleStyle(1)+"Bold:       1"+EndStyle() +"  "+ f"{GetConsoleStyle(0,1,0)}Red:    1{EndStyle()}"+"  "+ f"{GetConsoleStyle(0,7,1)}Red:    1{EndStyle()}")
    print(" "+GetConsoleStyle(2)+"Light:      2"+EndStyle() +"  "+ f"{GetConsoleStyle(0,2,0)}Green:  2{EndStyle()}"+"  "+ f"{GetConsoleStyle(0,7,2)}Green:  2{EndStyle()}")
    print(" "+GetConsoleStyle(3)+"Italicized: 3"+EndStyle() +"  "+ f"{GetConsoleStyle(0,3,0)}Yellow: 3{EndStyle()}"+"  "+ f"{GetConsoleStyle(0,7,3)}Yellow: 3{EndStyle()}")
    print(" "+GetConsoleStyle(4)+"Underlined: 4"+EndStyle() +"  "+ f"{GetConsoleStyle(0,4,0)}Blue:   4{EndStyle()}"+"  "+ f"{GetConsoleStyle(0,7,4)}Blue:   4{EndStyle()}")
    print(" "+GetConsoleStyle(5)+"Blink:      5"+EndStyle() +"  "+ f"{GetConsoleStyle(0,5,0)}Purple: 5{EndStyle()}"+"  "+ f"{GetConsoleStyle(0,7,5)}Purple: 5{EndStyle()}")
    print(GetConsoleStyle(0)+"              "+EndStyle() +"  "+ f"{GetConsoleStyle(0,6,0)}Cyan:   6{EndStyle()}"+"  "+ f"{GetConsoleStyle(0,7,6)}Cyan:   1{EndStyle()}")
    print(GetConsoleStyle(0)+"              "+EndStyle() +"  "+ f"{GetConsoleStyle(0,7,0)}White:  7{EndStyle()}"+"  "+ f"{GetConsoleStyle(0,0,7)}White:  1{EndStyle()}")
    pass
class RG_MainScript:
    
    def tick(self, deltatime:float):
        pass
    
    def PhysicsTick(self, deltatime:float):
        pass
    
    def Render(self):
        pass
    
class RG_Script:
    _id:int = 0
import abc

class RG_Physics(metaclass = abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'Start') and 
                callable(subclass.Start) and 
                hasattr(subclass, 'End') and 
                callable(subclass.End) and
                hasattr(subclass, 'Add') and 
                callable(subclass.Add) and
                hasattr(subclass, 'Exists') and 
                callable(subclass.Exists) and
                hasattr(subclass, 'End') and 
                callable(subclass.End) and
                hasattr(subclass, 'Remove') and 
                callable(subclass.Remove) and
                hasattr(subclass, 'Interval') and 
                hasattr(subclass, 'FailedTickFailsafe') and 
                hasattr(subclass, 'Running') and 
                hasattr(subclass, 'Counter') and 
                hasattr(subclass, 'DeltaTime') and 
                hasattr(subclass, 'FailedTickCount') or 
                NotImplemented)
    
    _interval:float = None
    _failedTickCount:int = None
    _failedTickFailsafe:ref = None
    
    @abc.abstractmethod
    def Start(self) -> None:
        pass
    
    @abc.abstractmethod
    def End(self) -> None:
        pass
    
    @abc.abstractmethod
    def Add(self, script:RG_Script) -> None:
        pass
    
    @abc.abstractmethod
    def Exists(self, script:RG_Script) -> bool:
        return False
    
    @abc.abstractmethod
    def Remove(self, script:RG_Script) -> None:
        pass
    
    @property
    @abc.abstractmethod
    def Interval(self) -> float:
        return self._interval
    
    @Interval.setter
    @abc.abstractmethod
    def Interval(self, newValue:float) -> None:
        self._interval= newValue
        
    @property
    @abc.abstractmethod
    def FailedTickFailsafe(self) -> int:
        return self._failedTickFailsafe.Value
    
    @FailedTickFailsafe.setter
    @abc.abstractmethod
    def FailedTickFailsafe(self, newValue:int) -> None:
        self._failedTickFailsafe.Value = newValue
        
    @property
    @abc.abstractmethod    
    def Running(self) -> bool:
        return self.C_Physics.CRG_Physics_Running(self.Tis)
    
    @property
    @abc.abstractmethod
    def Counter(self) -> int:
        return self.C_Physics.CRG_Physics_GetCounter(self.Tis)
    
    @property
    @abc.abstractmethod
    def DeltaTime(self) -> float:
        return self.C_Physics.CRG_Physics_GetDeltaTime(self.Tis)
    
    @property
    @abc.abstractmethod
    def FailedTickCount(self) -> int:
        return self._failedTickCount
    
    @FailedTickCount.setter
    @abc.abstractmethod
    def FailedTickCount(self, newValue:int) -> int:
        self._failedTickCount = newValue
from threading import Thread
from ctypes import*


class RG_CppPhysics(RG_Physics):
    _tis = None
    _scrCounter = 0
    _interval = 0
    _failedTickFailsafe = ref(3)
    _failedTickCount = 0
    _referenceKeeper = {}
    
    def __init__(self, mainScript:RG_MainScript, interval:float) -> None:
        self._mainScript = mainScript
        mainScriptTick = self._mainScript.tick
        
        import os
        data_path = os.path.join(os.path.dirname(__file__), 'RGame', 'Physics.dll')
        self.C_Physics = cdll.LoadLibrary(data_path)
        
        self._interval = interval
        
        self.MainScriptTick = CFUNCTYPE(None,c_double)(mainScriptTick);
        
        self.C_Physics.New_CRG_Physics.argtypes = [CFUNCTYPE(None,c_double),c_double,c_char_p];
        self.C_Physics.New_CRG_Physics.restype = c_void_p;
        
        self.C_Physics.Del_CRG_Physics.argtypes = [c_void_p];
        self.C_Physics.Del_CRG_Physics.restype = None;
        
        self.C_Physics.CRG_Physics_Start.argtypes = [c_void_p];
        self.C_Physics.CRG_Physics_Start.restype = None;
        
        self.C_Physics.CRG_Physics_End.argtypes = [c_void_p];
        self.C_Physics.CRG_Physics_End.restype = None;
        
        self.C_Physics.CRG_Physics_SetInterval.argtypes = [c_void_p, c_double];
        self.C_Physics.CRG_Physics_SetInterval.restype = None;
        
        self.C_Physics.CRG_Physics_Add.argtypes = [c_void_p,CFUNCTYPE(None,c_double)];
        self.C_Physics.CRG_Physics_Add.restype = None;
        
        self.C_Physics.CRG_Physics_Remove.argtypes = [c_void_p,CFUNCTYPE(None,c_double)];
        self.C_Physics.CRG_Physics_Remove.restype = None;
        
        self.C_Physics.CRG_Physics_Exists.argtypes = [c_void_p,CFUNCTYPE(None,c_double)];
        self.C_Physics.CRG_Physics_Exists.restype = c_bool;
        
        self.C_Physics.CRG_Physics_Running.argtypes = [c_void_p];
        self.C_Physics.CRG_Physics_Running.restype = c_bool;
        
        
        self.C_Physics.CRG_Physics_GetCounter.argtypes = [c_void_p];
        self.C_Physics.CRG_Physics_GetCounter.restype =  c_longlong;
        
        self.C_Physics.CRG_Physics_GetDeltaTime.argtypes = [c_void_p];
        self.C_Physics.CRG_Physics_GetDeltaTime.restype =  c_double;
        
        name = "MainPhysicsThread"
        self._tis = self.C_Physics.New_CRG_Physics(self.MainScriptTick,interval,c_char_p(name.encode('utf-8')))
        
        pass;
    
    def __del__(self):
        if(self._tis == None):return
        self.End()
        self.C_Physics.Del_CRG_Physics(self._tis)
        del self._tis
        del self._referenceKeeper
        del self.C_Physics
        
    def Start(self):
        try:
            self.t = Thread(target=self.waiter, name="PhyThread")
            self.t.start()
        except Exception as e:
            print(e)
        pass;
    
    def waiter(self):
        while not self._mainScript.Started: pass
        self.C_Physics.CRG_Physics_Start(self._tis)
    
    def End(self):
        self.C_Physics.CRG_Physics_End(self._tis);
        pass;
    
    def Add(self, script:RG_Script):
        script._id = self._scrCounter
        self._scrCounter += 1
        self._referenceKeeper[script._id] = CFUNCTYPE(None,c_double)(script.Tick)
        self.C_Physics.CRG_Physics_Add(self._tis, self._referenceKeeper[script._id])
    
    def Exists(self, script:RG_Script) -> bool:
        return script._id in self._referenceKeeper
    
    def Remove(self, script:RG_Script):
        try:
            self.C_Physics.CRG_Physics_Remove(self._tis, self._referenceKeeper[script._id]);
        except Exception as e:
            if(e.args[0] != "invalid command name \".!canvas\""):
                return
            else: raise e

        del self._referenceKeeper[script._id];
        pass;
    
    
    @property
    def Interval(self):
        return self._interval;
    
    @Interval.setter
    def Interval(self,newValue):
        self.C_Physics.CRG_Physics_SetInterval(self._tis,newValue);
        self._interval = newValue
        pass
    
    @property
    def FailedTickFailsafe(self) -> int:
        return self._failedTickFailsafe.Value
    
    @FailedTickFailsafe.setter
    def FailedTickFailsafe(self, newValue:int) -> None:
        self._failedTickFailsafe.Value = newValue
        
    @property  
    def Running(self):
        return self.C_Physics.CRG_Physics_Running(self._tis)
    
    @property
    def Counter(self):
        return self.C_Physics.CRG_Physics_GetCounter(self._tis);
    
    @property
    def DeltaTime(self):
        return self.C_Physics.CRG_Physics_GetDeltaTime(self._tis);
    
    @property
    def DeltaTime(self):
        return self.C_Physics.CRG_Physics_GetDeltaTime(self._tis);
    
    @property
    def FailedTickCount(self) -> int:
        return self._failedTickCount
    
    @FailedTickCount.setter
    def FailedTickCount(self, newValue:int) -> int:
        self._failedTickCount = newValue
from threading import Thread;
import time
from multiprocessing import*

class RG_PyPhysics(RG_Physics):
    _mainScript:RG_MainScript = None
    _interval:float = None
    _referenceKeeper = None
    _running:bool = False
    _counter:int = None
    _timePoint:int = None
    _waitLimit:int = None
    _failedTickCount:int = None
    _failedTickFailsafe:ref = None
    
    def __init__(self, mainScript:RG_MainScript, interval:float) -> None:
        self._mainScript = mainScript
        self._interval = interval
        self._referenceKeeper = []
        self._failedTickFailsafe = ref(3)
    
    def Start(self):
        self._pyThread = Thread(target=self.doStart)
        self._pyThread.start()
        
    def doStart(self):
        self._running = True
        self._counter = 0
        self._timePoint = time.perf_counter_ns()
        self._waitLimit = time.perf_counter_ns() - self._timePoint
        self._failedTickCount = 0
        while not self._mainScript.Started: pass
        while self._running:
            self.doTick()
    
    def doTick(self):
        self._counter += 1
        
        self._mainScript.tick(self.DeltaTime)
        for obj in self._referenceKeeper:
            obj(self.DeltaTime)
        
        self._timePoint = time.perf_counter_ns()
        if(self._interval*(1-self.DeltaTime) > self._waitLimit/1000000000) : 
            Pause(self._interval*(1-self.DeltaTime))
    
    def End(self):
        self._running = False
    
    def Add(self, script:RG_Script):
        self._referenceKeeper.append(script.Tick)
    
    def Remove(self, script):
        if(len(self._referenceKeeper) == 0): return
        self._referenceKeeper.remove(script.Tick)
    
    def Exists(self, script) -> bool:
        return 0 < self._referenceKeeper.count(script.PhysicsTick)
    
    @property
    def Interval(self) -> float:
        return self._interval
    
    @Interval.setter
    def Interval(self, newValue:float):
        self._interval = newValue
    
    @property
    def FailedTickFailsafe(self) -> int:
        return self._failedTickFailsafe.Value
    
    @FailedTickFailsafe.setter
    def FailedTickFailsafe(self, newValue:int) -> None:
        self._failedTickFailsafe.Value = newValue
    
    @property
    def Running(self) -> bool:
        return self._running
    
    @property
    def Counter(self) -> int:
        return self._counter
    
    @property
    def DeltaTime(self) -> float:
        if(self._interval == 0): return time.perf_counter_ns()-self._timePoint
        return (time.perf_counter_ns()-self._timePoint)/(self._interval*1000000000)
    
    @property
    def FailedTickCount(self) -> int:
        return self._failedTickCount
    
    @FailedTickCount.setter
    def FailedTickCount(self, newValue:int) -> int:
        self._failedTickCount = newValue
import enum

@enum.unique
class RG_PhysicsMode(enum.Enum):
    CPP = 0
    PYTHON = 1
    pass

class RG_MainPhysics(RG_Physics):
    _physicsMode:int = None
    _PyPhysics:RG_Physics = None
    _CppPhysics:RG_Physics = None
    _started:bool = False
    _autoSet:bool = False
    
    @property
    def PhysicsMode(self) -> RG_PhysicsMode:
        return self._physicsMode
    
    @PhysicsMode.setter
    def PhysicsMode(self, newValue:RG_PhysicsMode) -> None:
        if self._autoSet and newValue != RG_PhysicsMode.PYTHON:
            switchWarning = RG_TypeWarning(newValue, "The value has already automatically been (due to some error) set to python mode permanently.")
            Log(switchWarning.Message, switchWarning.Value, LogLevel.WARNING)
            return
        if self._started:
            raise RG_AccessError(newValue, "You cannot change the Physics mode after starting the simulation.")
        self._physicsMode = newValue
                
    
    def getPhysics(self) -> RG_Physics:
        match self.PhysicsMode:
            case RG_PhysicsMode.PYTHON:
                return self._PyPhysics
            case RG_PhysicsMode.CPP:
                return self._CppPhysics
            case _:
                accessError = RG_AccessError(None,
                                        "You probably accessed a private member of RG_MainPhysics (set a private member to None/called the private function getPhysics too early)!")
                raise accessError
    
    def __init__(self, mainScript:RG_MainScript, interval:float) -> None:
        
        if self.PhysicsMode == None: 
            self.PhysicsMode = RG_PhysicsMode.CPP
            
        self._PyPhysics = RG_PyPhysics(mainScript, interval)
        
        try:
            self._CppPhysics = RG_CppPhysics(mainScript, interval)
        except Exception as e:
            switchWarning = RG_FileExistsWarning(*e.args, "The Physics.dll could not be loaded so automatically setting physics mode permanently to Python")
            Log(switchWarning.Message, switchWarning.Value, LogLevel.WARNING)
            self.PhysicsMode = RG_PhysicsMode.PYTHON 
            self._autoSet = True

    def Start(self) -> None:
        if self._started: return
        self._started = True
        self.getPhysics().Start()
        
    def End(self) -> None:
        self.getPhysics().End()
    
    def Add(self, script:RG_Script) -> None:
        self.getPhysics().Add(script)
        
    def Exists(self, script: RG_Script) -> bool:
        return self.getPhysics().Exists(script)
    
    def Remove(self, script: RG_Script) -> None:
        self.getPhysics().Remove(script)
    
    @property
    def Interval(self) -> float:
        return self.getPhysics().Interval
    
    @Interval.setter
    def Interval(self, newValue:float) -> None:
        self.getPhysics().Interval = newValue
        
    @property
    def FailedTickFailsafe(self) -> int:
        return self.getPhysics().FailedTickFailsafe
    
    @FailedTickFailsafe.setter
    def FailedTickFailsafe(self, newValue:int) -> None:
        self.getPhysics().FailedTickFailsafe = newValue
        
    @property
    def Running(self) -> bool:
        return self.getPhysics().Running
    
    @property
    def Counter(self) -> int:
        return self.getPhysics().Counter
    
    @property
    def DeltaTime(self) -> float:
        return self.getPhysics().DeltaTime
    
    @property
    def FailedTickCount(self) -> int:
        return self.getPhysics().FailedTickCount
    
    @FailedTickCount.setter
    def FailedTickCount(self, newValue:int) -> int:
        self.getPhysics().FailedTickCount = newValue
from decimal import Decimal

class RG_Size:
    
    _width:Decimal = 100;
    _height:Decimal = 100;
    
    @property
    def Width(self):
        return self._width;
    
    @Width.setter
    def Width(self,newVal): 
        self._width = Decimal(newVal);
        pass;
    
    @property
    def Height(self):
        return self._height;
    
    @Height.setter
    def Height(self,newVal): 
        self._height = Decimal(newVal);
        pass
    
    def __init__(self, width:Decimal | float = None, height:Decimal | float = None) -> None:
        
        # width
        if (width is None):
            width = Decimal(25)
        elif not ((type(width) is Decimal) or (type(width) is int)):
            if(type(width) is float):
                LogWarning(" Possible loss of data (converting 'float' to 'Decimal').\n For the argument 'width'(first argument) of the class 'RG_Size'")
                width = Decimal(width)
            else:
                raise RG_TypeError(width,
                                " 'RG_Size' must have a 'Decimal' as the argument 'width' (first argument).")
                            
        # height
        if (height is None):
            height = Decimal(25)
        elif not ((type(height) is Decimal) or (type(height) is int)):
            if(type(height) is float):
                LogWarning(" Possible loss of data (converting 'float' to 'Decimal').\n For the argument 'height'(second argument) of the class 'RG_Size'")
                height = Decimal(height)
            else:
                raise RG_TypeError(height,
                                " 'RG_Size' must have a 'Decimal' as the argument 'height' (second argument).")
            
        self.Width = width
        self.Height = height
        pass
    
    def __eq__(self, other) -> bool:
        if(not type(other) is RG_Size): return False;
        return self.Width == other.Width and self.Height == other.Height;
    
    def __str__(self) -> str:
        return "Size: (Width: " + str(self.Width) + ", Height: " + str(self.Height) + ")";
    
    pass;
class RG_SizeSquare(RG_Size):
    
    @property
    def Side(self):
        return self.Width
    
    @Side.setter
    def Side(self,newVal): 
        self.Width = Decimal(newVal);
        self.Height = Decimal(newVal);
        pass;
    
    def __init__(self, side:Decimal | float = None) -> None:
        #side
        if (side is None):
            side = Decimal(25)
        elif not ((type(side) is Decimal) or (type(side) is int)):
            if(type(side) is float):
                LogWarning(" Possible loss of data (converting 'float' to 'Decimal').\n For the argument 'side'(second argument) of the class 'RG_Size'")
                side = Decimal(side)
            else:
                raise RG_TypeError(side,
                                " 'RG_SizeSquare' must have a 'Decimal' as the argument 'side' (second argument).")
        self.Side = side
        pass
    
    def __eq__(self, other) -> bool:
        if(not type(other) is RG_SizeSquare): return False;
        return self.Side == other.Side
    
    def __str__(self) -> str:
        return "Square Size: (Size: " + str(self.RadiusX) + ")";
    
    pass;

class RG_SizeEllipse(RG_Size):
    
    @property
    def RadiusX(self):
        return self.Width / 2
    
    @RadiusX.setter
    def RadiusX(self,newVal): 
        self.Width = Decimal(newVal)*2
        pass;
    
    @property
    def RadiusY(self):
        return self.Height / 2
    
    @RadiusY.setter
    def RadiusY(self,newVal): 
        self.Height = Decimal(newVal)*2
        pass;
    
    
    def __init__(self, radiusX:Decimal | float = None, radiusY:Decimal | float = None) -> None:
        # radius X
        if (radiusX is None):
            radiusX = Decimal(25)
        elif not ((type(radiusX) is Decimal) or (type(radiusX) is int)):
            if(type(radiusX) is float):
                LogWarning(" Possible loss of data (converting 'float' to 'Decimal').\n For the argument 'radiusX'(first argument) of the class 'RG_Size'")
                radiusX = Decimal(radiusX)
            else:
                raise RG_TypeError(radiusX,
                                " 'RG_SizeEllipse' must have a 'Decimal' as the argument 'radiusX' (first argument).")
                     
        self.RadiusX = radiusX;
               
        # radius Y
        if (radiusY is None):
            radiusY = Decimal(25)
        elif not ((type(radiusY) is Decimal) or (type(radiusY) is int)):
            if(type(radiusY) is float):
                LogWarning(" Possible loss of data (converting 'float' to 'Decimal').\n For the argument 'radiusY'(second argument) of the class 'RG_Size'")
                radiusY = Decimal(radiusY)
            else:
                raise RG_TypeError(radiusY,
                                " 'RG_Size' must have a 'Decimal' as the argument 'radiusY' (second argument).")
                
        self.RadiusY = radiusY;
        pass
    
    def __eq__(self, other) -> bool:
        if(not type(other) is RG_SizeEllipse): return False;
        return self.Width == other.Width and self.Height == other.Height;
    
    def __str__(self) -> str:
        return "Ellipse Size: (RadiusX: " + str(self.RadiusX) + ", RadiusY: " + str(self.RadiusY) + ")";
    
    pass;

class RG_SizeCircle(RG_SizeEllipse):
    
    @property
    def Radius(self):
        return self.RadiusX;
    
    @Radius.setter
    def Radius(self,newVal): 
        self.RadiusX = Decimal(newVal);
        self.RadiusY = Decimal(newVal);
        pass;
    
    
    def __init__(self, radius:Decimal | float = None) -> None:
        # radius 
        if (radius is None):
            radius = Decimal(25)
        elif not ((type(radius) is Decimal) or (type(radius) is int)):
            if(type(radius) is float):
                LogWarning(" Possible loss of data (converting 'float' to 'Decimal').\n For the argument 'radius'(second argument) of the class 'RG_Size'")
                radiusY = Decimal(radius)
            else:
                raise RG_TypeError(radius,
                                " 'RG_SizeCircle' must have a 'Decimal' as the argument 'radius' (second argument).")
        self.Radius = radius;
        pass
    
    def __eq__(self, other) -> bool:
        if(not type(other) is RG_SizeCircle): return False;
        return self.Radius == other.Radius;
    
    def __str__(self) -> str:
        return "Circle Size: (Radius: " + str(self.Radius) + ")";
    
    pass;
from tkinter import*

#----------------------------------
#----------------------------------
#            Appearance
#----------------------------------
#----------------------------------        
class RG_AppearanceType:
    # ----------------------------------
    #            Variables:
    # ----------------------------------
    _ended = True
    _created:bool = False;
    @property
    def Created(self):
        return self._created;
    
    @Created.setter
    def Created(self,new):
        raise ValueError("Created is readonly.")
    
    _canvasID:str = "";
    OffSet:RG_Vector2D = RG_Vector2D(0,0);
    _visible = True;
    
    @property
    def Visible(self):
        return self._visible
    
    @Visible.setter
    def Visible(self, new):
        if not (type(new) is bool): raise TypeError("Cannot set visible to a value that is not bool: " + str(new))
        if(new):
            self.Show()
        else:
            self.Hide()
    
    Dimensions:object = None;
        
    def __init__(self, canvas:Canvas, spritePosition:RG_Position2D) -> None:
        self._screen:Canvas = canvas;
        self.CreateGraphics(spritePosition)
        pass;
    
    def __del__(self):
        self.DeleteGraphics()
    
    # ----------------------------------
    #            Functions:
    # ----------------------------------
    def CreateGraphics(self):
        if(self.Created):return;
        self._visible = True;
        self._created = True;
        self._canvasID = self._createGfx( RG_Position2D(0,0) );
        
        pass;
    
    def _createGfx(self, spritePosition:RG_Position2D) -> str:
        
        pass;
    
    def _configureGfx(self):
        
        pass;
    
    
    def DeleteGraphics(self):
        if not (self.Created): return;
        self._created = False;
        self._visible = False;
        try:
            self._screen.delete(self._canvasID);
        except Exception as e:
            if(e.args[0] == "invalid command name \".!canvas\""):
                return
            else:
                raise e
            
        self._canvasID = "";
        pass;
    
    def Hide(self):
        try:
            self._screen.itemconfigure(self._canvasID, state = "hidden");
        except Exception as e:
            if(e.args[0] == "invalid command name \".!canvas\""):
                return
            else:
                raise e
        self._visible = False;
        pass;
    
    def Show(self):
        self._screen.itemconfigure(self._canvasID, state = "normal");
        self._visible = True;
        pass;
    
    def MoveTo(self,x,y):
        try:
            self._screen.moveto(self._canvasID, int(x-self.OffSet.X), (int(self._screen.winfo_height()-y+self.OffSet.Y-self.Dimensions.Height)));
        except Exception as e:
            if(e.args[0] == "invalid command name \".!canvas\""):
                return
            else:
                raise e
        
    def Render(self):
        if(not self.Created): self.CreateGraphics()
        if(not self.Visible): return;
        self._configureGfx()
        pass;
    
    
    pass;
from tkinter import*
import tkinter.font as tkFont
import os 
import math

#----------------------------------
#----------------------------------
#            Appearance
#----------------------------------
#----------------------------------        

class RG_App_Label(RG_AppearanceType):
    
    def GetFontTypes() -> tuple:
        return tkFont.families()
    
    # ----------------------------------
    #          Base Functions:
    # ----------------------------------
    # Constructor
    def __init__(self, screen:Canvas = None, text:str = None, fontType:str = None, fontSize:int = None, fontColor:str = None, bold:bool = None, italic:bool = None, underline:bool = None, overstrike:bool = None, offset:RG_Vector2D = None) -> None:
        
        #-----------defaults-----------
        # screen
        if not (type(screen) is Canvas):
            raise RG_TypeError(screen,
                                " An 'RG_App_Label' must have 'self.MainWindow.Screen' as the argument 'screen' (first argument).")
        
        self._screen = screen
        
        # text
        if (text is None):
            text = "Label text."
        elif not (type(text) is str):
            raise RG_TypeError(text,
                                " 'RG_App_Label' must have a string as the argument 'text' (second argument).")
            
        self.Text = text
        
        # fontType 
        if (fontType is None):
            fontType = "Calibri"
        elif not (type(fontType ) is str):
            raise RG_TypeError(fontType ,
                                " 'RG_App_Label' must have a string as the argument 'fontType' (third argument).")
        elif not (fontType in tkFont.families()):
            raise RG_ValueError(fontType,
                            " 'RG_App_Label' the argument 'fontType' (third argument) must be a font that exists.")
        
        self.FontType = fontType
        
        # fontSize
        if (fontSize is None):
            fontSize  = 12
        elif not (type(fontSize ) is int):
            raise RG_TypeError(fontSize ,
                                " 'RG_App_Label' must have an int as the argument 'fontSize' (fourth argument).")
        
        self.FontSize = fontSize
        
        # fontColor        
        if (fontColor is None):
            fontColor  = "Black"
        elif not (type(fontColor ) is str):
            raise RG_TypeError(fontColor ,
                                " 'RG_App_Label' must have a str as the argument 'fontColor' (fifth argument).")
        
        self.Color = fontColor
        
        # Bold      
        if (bold is None):
            bold = False
        elif not (type(bold) is bool):
            raise RG_TypeError(bold ,
                                " 'RG_App_Label' must have a bool as the argument 'bold' (sixth argument).")
        
        self.Weight = bold
        
        # Italic     
        if (italic is None):
            italic = False
        elif not (type(italic) is bool):
            raise RG_TypeError(italic,
                                " 'RG_App_Label' must have a bool as the argument 'italic' (seventh argument).")
            
        self.Slant = italic
        
        # Underline     
        if (underline is None):
            underline = False
        elif not (type(underline) is bool):
            raise RG_TypeError(underline,
                                " 'RG_App_Label' must have a bool as the argument 'underline' (eighth argument).")
            
        self.Underline = underline
        
        # Overstrike     
        if (overstrike is None):
            overstrike = False
        elif not (type(overstrike) is bool):
            raise RG_TypeError(overstrike,
                                " 'RG_App_Label' must have a bool as the argument 'overstrike' (ninth argument).")
            
        self.Overstrike = overstrike
        
        #offset
        if (offset is None):
            offset = RG_Vector2D()
        elif not (type(offset) is RG_Vector2D):
            raise RG_TypeError(offset,
                                " 'RG_App_Label' must have an RG_Vector2D as the argument 'offset' (last argument).")
        
        self.OffSet = offset
        pass
    
    # To String
    def __str__(self) -> str:
        return "Label: (ShapeID: " + str(self._canvasID) + ", Text: " + str(self.Text) + ", FontType: " + str(self.FontType) + ", FontColor: " + str(self.FontColor) + ")";
    
    # ----------------------------------
    #            Functions:
    # ----------------------------------
    
    def MoveTo(self, x, y):
        self._screen.moveto(self._canvasID, int(x-self.OffSet.X), (int(self._screen.winfo_height()-y+self.OffSet.Y)));
    
    def _createGfx(self, spritePosition:RG_Position2D):
        absolutePosition = spritePosition + self.OffSet
        if(self.Weight):
            weight = "bold"
        else:
            weight = "normal"
        if(self.Slant):
            slant = "italic"
        else:
            slant = "roman"
        font = tkFont.Font(
            family = str(self.FontType),
            size = self.FontSize, 
            weight = weight,
            slant = slant,
            underline = self.Underline,
            overstrike = self.Overstrike)
        try:
            ID = self._screen.create_text(
                absolutePosition.X, absolutePosition.Y, 
                fill=self.Color,
                font=font,
                text= self.Text
                )
        except Exception as e:
            LogError(" Could not create a label.")
        return ID;
    
    def _configureGfx(self):
        if(self.Weight):
            weight = "bold"
        else:
            weight = "normal"
        if(self.Slant):
            slant = "italic"
        else:
            slant = "roman"
        font = tkFont.Font(
            family = str(self.FontType),
            size = self.FontSize, 
            weight = weight,
            slant = slant,
            underline = self.Underline,
            overstrike = self.Overstrike)
        self._screen.itemconfigure(self._canvasID,
                fill=self.Color,
                font=font,
                text= self.Text)
        pass
    
    pass

class RG_App_Shape(RG_AppearanceType):
    
    # ----------------------------------
    #            Variables:
    # ----------------------------------
    Color:str = "Black";
    Dimensions:RG_Size = RG_Size(50,50);
    
    # ----------------------------------
    #          Base Functions:
    # ----------------------------------
    # Constructor
    def __init__(self,screen:Canvas, dimensions:RG_Size  = None, color:str = None, outlineColor:str = None, outlineWidth:int = None, offset:RG_Vector2D = None) -> None:
        #-----------defaults-----------
        # screen
        if not (type(screen) is Canvas):
            raise RG_TypeError(screen,
                                " An 'RG_App_Shape' must have 'self.MainWindow.Screen' as the argument 'screen' (first argument).")
        
        self._screen = screen
        
        # dim
        if (dimensions is None):
            dimensions  = RG_Size()
        elif not (issubclass(type(dimensions ),RG_Size) or type(dimensions ) is RG_Size):
            raise RG_TypeError(dimensions ,
                                " 'RG_App_Shape' must have a RG_Size as the argument 'dimensions' (second argument).")
        
        self.Dimensions = dimensions
        
        # Color        
        if (color is None):
            color  = "Black"
        elif not (type(color ) is str):
            raise RG_TypeError(color ,
                                " 'RG_App_Shape' must have a str as the argument 'color' (third argument).")
        
        self.Color = color
        
        # outlineColor    
        if (outlineColor is None):
            outlineColor  = "Black"
        elif not (type(outlineColor ) is str):
            raise RG_TypeError(outlineColor ,
                                " 'RG_App_Ellipse' must have a str as the argument 'outlineColor' (fifth argument).")
        
        self.OutlineColor = outlineColor
        
        # outlineWidth        
        if (outlineWidth is None):
            outlineWidth  = 0
        elif not (type(outlineWidth ) is int):
            raise RG_TypeError(outlineWidth ,
                                " 'RG_App_Ellipse' must have an int as the argument 'outlineWidth' (sixth argument).")
        
        self.OutlineWidth = outlineWidth
        
        #offset
        if (offset is None):
            offset = RG_Vector2D()
        elif not (type(offset) is RG_Vector2D):
            raise RG_TypeError(offset,
                                " 'RG_App_Shape' must have an RG_Vector2D as the argument 'offset' (last argument).")
        
        self.OffSet = offset
        pass;
    
    # To String
    def __str__(self) -> str:
        return "Shape: (ShapeID: " + str(self._canvasID) + ", Dimensions: " + str(self.Dimensions) + ", Color: " + str(self.Color) + ", OffSet: " + str(self.OffSet) + ")";
    
    # ----------------------------------
    #            Functions:
    # ----------------------------------
    def _createGfx(self, spritePosition:RG_Position2D):
        
        absolutePosition = spritePosition + self.OffSet;
        ID = self._screen.create_rectangle(
            absolutePosition.X, self._screen.winfo_height()-absolutePosition.Y, 
            absolutePosition.X + self.Dimensions.Width, (self._screen.winfo_height()-absolutePosition.Y) - self.Dimensions.Height,
            fill=self.Color,outline=self.OutlineColor,width=self.OutlineWidth
            );
        return ID;
    
    def _configureGfx(self):
        pos = self._screen.coords(self._canvasID)
        
        self._screen.coords(self._canvasID,
            pos[0],pos[1],
            pos[0] + float(self.Dimensions.Width), pos[1] + float(self.Dimensions.Height))
        
        self._screen.itemconfigure(self._canvasID,
            fill=self.Color,outline=self.OutlineColor,width=self.OutlineWidth)
        pass;
        
    pass;
    
class RG_App_Rectangle(RG_App_Shape):
    pass;

class RG_App_Line(RG_App_Shape):
    # ----------------------------------
    #            Variables:
    # ----------------------------------
    Color:str = "Black";
    
    # ----------------------------------
    #          Base Functions:
    # ----------------------------------
    # Constructor
    def __init__(self,screen:Canvas, points:list[RG_Vector2D] = None, color:str = None, width:int = None, smooth:bool = None, resolution:int = None, offset:RG_Vector2D = None) -> None:
        #-----------defaults-----------
        # screen
        if not (type(screen) is Canvas):
            raise RG_TypeError(screen,
                                " An 'RG_App_Line' must have 'self.MainWindow.Screen' as the argument 'screen' (first argument).")
        
        self._screen = screen
        
        # dim
        if (points is None):
            points  = [RG_Vector2D(25,25)]
        elif not (type(points ) is list):
            raise RG_TypeError(points ,
                                " 'RG_App_Line' must have a list of RG_Vector2Ds as the argument 'points' (second argument).")
        
        self.Points2 = points
        
        # Color        
        if (color is None):
            color  = "Black"
        elif not (type(color ) is str):
            raise RG_TypeError(color ,
                                " 'RG_App_Line' must have a str as the argument 'color' (third argument).")
        
        self.Color = color
        
        # Width        
        if (width is None):
            width  = 1
        elif not (type(width ) is int):
            raise RG_TypeError(width ,
                                " 'RG_App_Line' must have a int as the argument 'width' (fourth argument).")
        
        self.Width = width
        
        # Smooth        
        if (smooth is None):
            smooth  = False
        elif not (type(smooth ) is bool):
            raise RG_TypeError(smooth ,
                                " 'RG_App_Line' must have a bool as the argument 'smooth' (fifth argument).")
        
        self.Smooth = smooth
        
        # Resolution        
        if (resolution is None):
            resolution = 12
        elif not (type(resolution ) is int):
            raise RG_TypeError(resolution ,
                                " 'RG_App_Line' must have a int as the argument 'resolution' (sixth argument).")
        
        self.Resolution = resolution
        
        #offset
        if (offset is None):
            offset = RG_Vector2D()
        elif not (type(offset) is RG_Vector2D):
            raise RG_TypeError(offset,
                                " 'RG_App_Line' must have an RG_Vector2D as the argument 'offset' (last argument).")
        
        self.OffSet = offset
        pass;
    
    # To String
    def __str__(self) -> str:
        return "Line: (ShapeID: " + str(self._canvasID) + ", Color: " + str(self.Color) + ", OffSet: " + str(self.OffSet) + ")";
    
    # ----------------------------------
    #            Functions:
    # ----------------------------------
    def _createGfx(self, spritePosition:RG_Position2D):
        
        absolutePosition = spritePosition + self.OffSet;
        res = [absolutePosition.X, self._screen.winfo_height()-absolutePosition.Y]
        for point in self.Points2:
            res.append(absolutePosition.X + point.X)
            res.append(self._screen.winfo_height() - (absolutePosition.Y + point.Y))
        ID = self._screen.create_line(
            *res,
            fill=self.Color,width =self.Width, smooth=self.Smooth, splinesteps=self.Resolution
            );
        return ID;
    
    def _configureGfx(self):
        pos = self._screen.coords(self._canvasID)
        
        res = [pos[0], pos[1]]
        for point in self.Points2:
            res.append(pos[0] + float(point.X))
            res.append(pos[1] - float(point.Y))
            
        self._screen.coords(self._canvasID,
            *res)
        self._screen.itemconfigure(self._canvasID,
            fill=self.Color,width =self.Width, smooth=self.Smooth, splinesteps=self.Resolution)
        pass;
    
    def MoveTo(self,x,y):
        res = [x,self._screen.winfo_height()-int(y)]
        for point in self.Points2:
            res.append(x + int(point.X))
            res.append(self._screen.winfo_height() - int(y) - int(point.Y))
            
        self._screen.coords(self._canvasID,
            *res)
        pass
    pass;

class RG_App_Polygon(RG_App_Shape):
    # ----------------------------------
    #            Variables:
    # ----------------------------------
    Color:str = "Black";
    Rotation = 0
    # ----------------------------------
    #          Base Functions:
    # ----------------------------------
    # Constructor
    def __init__(self,screen:Canvas, points:list[RG_Vector2D] = None, color:str = None, outlineColor:str = None, outlineWidth:int = None, smooth:bool = None, resolution:int = None, offset:RG_Vector2D = None) -> None:
        #-----------defaults-----------
        # screen
        if not (type(screen) is Canvas):
            raise RG_TypeError(screen,
                                " An 'RG_App_Polygon' must have 'self.MainWindow.Screen' as the argument 'screen' (first argument).")
        
        self._screen = screen
        
        # dim
        if (points is None):
            points  = [RG_Vector2D(25,25)]
        elif not (type(points ) is list):
            raise RG_TypeError(points ,
                                " 'RG_App_Polygon' must have a list of RG_Vector2Ds as the argument 'points' (second argument).")
        
        self.Points2 = points
        
        # Color        
        if (color is None):
            color  = "Black"
        elif not (type(color ) is str):
            raise RG_TypeError(color ,
                                " 'RG_App_Polygon' must have a str as the argument 'color' (third argument).")
        
        self.Color = color
        
        
        # outlineColor    
        if (outlineColor is None):
            outlineColor  = "Black"
        elif not (type(outlineColor ) is str):
            raise RG_TypeError(outlineColor ,
                                " 'RG_App_Polygon' must have a str as the argument 'outlineColor' (fifth argument).")
        
        self.OutlineColor = outlineColor
        
        # outlineWidth        
        if (outlineWidth is None):
            outlineWidth  = 0
        elif not (type(outlineWidth ) is int):
            raise RG_TypeError(outlineWidth ,
                                " 'RG_App_Polygon' must have an int as the argument 'outlineWidth' (sixth argument).")
        
        self.OutlineWidth = outlineWidth
                
        # Smooth        
        if (smooth is None):
            smooth  = False
        elif not (type(smooth ) is bool):
            raise RG_TypeError(smooth ,
                                " 'RG_App_Polygon' must have a bool as the argument 'smooth' (fifth argument).")
        
        self.Smooth = smooth
        
        # Resolution        
        if (resolution is None):
            resolution = 12
        elif not (type(resolution ) is int):
            raise RG_TypeError(resolution ,
                                " 'RG_App_Polygon' must have a int as the argument 'resolution' (sixth argument).")
        
        self.Resolution = resolution
        
        #offset
        if (offset is None):
            offset = RG_Vector2D()
        elif not (type(offset) is RG_Vector2D):
            raise RG_TypeError(offset,
                                " 'RG_App_Polygon' must have an RG_Vector2D as the argument 'offset' (last argument).")
        
        self.OffSet = offset
        pass;
    
    # To String
    def __str__(self) -> str:
        return "Polygon: (ShapeID: " + str(self._canvasID) + ", Color: " + str(self.Color) + ", OffSet: " + str(self.OffSet) + ")";
    
    # ----------------------------------
    #            Functions:
    # ----------------------------------
    def _createGfx(self, spritePosition:RG_Position2D):
        
        absolutePosition = spritePosition + self.OffSet;
        res = [absolutePosition.X, self._screen.winfo_height()-absolutePosition.Y]
        c = Decimal(math.cos(self.Rotation))
        s = Decimal(math.sin(self.Rotation))
        for point in self.Points2:
            temp = RG_Vector2D()
            temp.X = point.X * c - point.Y * s
            temp.Y = point.X * s + point.Y * c
            res.append(absolutePosition.X + point.X)
            res.append(self._screen.winfo_height() - (absolutePosition.Y + point.Y))
        ID = self._screen.create_polygon(
            *res,
            fill=self.Color,width =self.OutlineWidth, outline= self.OutlineColor , smooth=self.Smooth, splinesteps=self.Resolution, 
            );
        return ID;
    
    def _configureGfx(self):
        pos = self._screen.coords(self._canvasID)
        
        self._screen.itemconfigure(self._canvasID,
            fill=self.Color,width =self.OutlineWidth, outline= self.OutlineColor, smooth=self.Smooth, splinesteps=self.Resolution)
        pass;
    
    def MoveTo(self,x,y):
        res = [x,self._screen.winfo_height()-int(y)]
        c = Decimal(math.cos(self.Rotation))
        s = Decimal(math.sin(self.Rotation))
        for point in self.Points2:
            temp = RG_Vector2D()
            temp.X = point.X * c - point.Y * s
            temp.Y = point.X * s + point.Y * c
            res.append(x + int(temp.X))
            res.append(self._screen.winfo_height() - int(y) - int(temp.Y))
            
        self._screen.coords(self._canvasID,
            *res)
        pass
    
    def Rotate(self, angle:float, centre:RG_Point2D, spritePosition:RG_Position2D, clockwise=True):
        coef = -1
        if not (clockwise):
            coef = 1
        c = Decimal(math.cos(angle*coef))
        s = Decimal(math.sin(angle*coef))
        spritePosition.X -= centre.X
        spritePosition.Y -= centre.Y
        x = spritePosition.X * c - spritePosition.Y * s
        y = spritePosition.X * s + spritePosition.Y * c
        spritePosition.X = x
        spritePosition.Y = y
        spritePosition.X += centre.X
        spritePosition.Y += centre.Y
        self.Rotation += angle*coef
        return spritePosition
    pass

class RG_App_Ellipse(RG_App_Shape):
    
    # ----------------------------------
    #          Base Functions:
    # ----------------------------------
    # Constructor
    def __init__(self,screen:Canvas, radiusX:Decimal | float = None, radiusY:Decimal | float = None, color:str = None, outlineColor:str = None, outlineWidth:int = None, offset: RG_Vector2D = None) -> None:
        #-----------defaults-----------
        # screen
        if not (type(screen) is Canvas):
            raise RG_TypeError(screen,
                                " An 'RG_App_Ellipse' must have 'self.MainWindow.Screen' as the argument 'screen' (first argument).")
        
        self._screen = screen
        
        # dim
        self.Dimensions = RG_SizeEllipse(radiusX,radiusY)
        
        # Color        
        if (color is None):
            color  = "Black"
        elif not (type(color ) is str):
            raise RG_TypeError(color ,
                                " 'RG_App_Ellipse' must have a str as the argument 'color' (fourth argument).")
        
        self.Color = color
        
        # outlineColor    
        if (outlineColor is None):
            outlineColor  = "Black"
        elif not (type(outlineColor ) is str):
            raise RG_TypeError(outlineColor ,
                                " 'RG_App_Ellipse' must have a str as the argument 'outlineColor' (fifth argument).")
        
        self.OutlineColor = outlineColor
        
        # outlineWidth        
        if (outlineWidth is None):
            outlineWidth  = 0
        elif not (type(outlineWidth ) is int):
            raise RG_TypeError(outlineWidth ,
                                " 'RG_App_Ellipse' must have an int as the argument 'outlineWidth' (sixth argument).")
        
        self.OutlineWidth = outlineWidth
        
        #offset
        if (offset is None):
            offset = RG_Vector2D()
        elif not (type(offset) is RG_Vector2D):
            raise RG_TypeError(offset,
                                " 'RG_App_Ellipse' must have an RG_Vector2D as the argument 'offset' (last argument).")
        
        self.OffSet = offset
        pass;
    
    # To String
    def __str__(self) -> str:
        return "Ellipse: (ShapeID: " + str(self._canvasID) + ", Dimensions: " + str(self.Dimensions) + ", Color: " + str(self.Color) + ", OffSet: " + str(self.OffSet) + ")";

    # ----------------------------------
    #            Functions:
    # ----------------------------------
    def _createGfx(self, spritePosition: RG_Position2D) -> str:
        absolutePosition = spritePosition + self.OffSet;
        ID = self._screen.create_oval(
            absolutePosition.X, (self._screen.winfo_height()-absolutePosition.Y), 
            absolutePosition.X + Decimal(self.Dimensions.Width), (self._screen.winfo_height()-absolutePosition.Y) - Decimal(self.Dimensions.Width),
            fill=self.Color,outline=self.OutlineColor,width=self.OutlineWidth
            );
        return ID;
    
    def _configureGfx(self):
        pos = self._screen.coords(self._canvasID)
        
        self._screen.coords(self._canvasID,
            pos[0],pos[1],
            pos[0] + float(self.Dimensions.Width), pos[1] + float(self.Dimensions.Height),)
        
        self._screen.itemconfigure(self._canvasID,
            fill=self.Color,outline=self.OutlineColor,width=self.OutlineWidth)
        pass;
    
    pass;
    
class RG_App_Circle(RG_App_Ellipse):
    
    # ----------------------------------
    #          Base Functions:
    # ----------------------------------
    # Constructor
    def __init__(self,screen:Canvas, radius:Decimal | float = None, color: str = None, outlineColor:str = None, outlineWidth:int = None, offset: RG_Vector2D = None) -> None:
        #-----------defaults-----------
        # screen
        if not (type(screen) is Canvas):
            raise RG_TypeError(screen,
                                " An 'RG_App_Circle' must have 'self.MainWindow.Screen' as the argument 'screen' (first argument).")
        
        self._screen = screen
        
        # dim
        self.Dimensions = RG_SizeCircle(radius)
        
        # Color        
        if (color is None):
            color  = "Black"
        elif not (type(color ) is str):
            raise RG_TypeError(color ,
                                " 'RG_App_Circle' must have a str as the argument 'color' (third argument).")
        
        self.Color = color
        
        # outlineColor    
        if (outlineColor is None):
            outlineColor  = "Black"
        elif not (type(outlineColor ) is str):
            raise RG_TypeError(outlineColor ,
                                " 'RG_App_Ellipse' must have an int as the argument 'outlineColor' (fifth argument).")
        
        self.OutlineColor = outlineColor
        
        # outlineWidth        
        if (outlineWidth is None):
            outlineWidth  = 0
        elif not (type(outlineWidth ) is int):
            raise RG_TypeError(outlineWidth ,
                                " 'RG_App_Ellipse' must have a str as the argument 'outlineWidth' (sixth argument).")
        
        self.OutlineWidth = outlineWidth
        
        #offset
        if (offset is None):
            offset = RG_Vector2D()
        elif not (type(offset) is RG_Vector2D):
            raise RG_TypeError(offset,
                                " 'RG_App_Circle' must have an RG_Vector2D as the argument 'offset' (last argument).")
        
        self.OffSet = offset
        pass;
    
    pass;


import os
class RG_App_Shader(RG_AppearanceType):
    
    _location:str = "RGame\\RGamePic.png"
    
    @property
    def Location(self):
        return self._location
    
    @Location.setter
    def Location(self, fileLocation):
        if (fileLocation is None):
            data_path = os.path.join(os.path.dirname(__file__), 'RGame', 'RGamePic.png')
            fileLocation = data_path
        elif not (type(fileLocation) is str):
            raise RG_TypeError(fileLocation ,
                                " 'RG_App_Shader' must have a string as the parameter 'fileLocation'.")
        elif not (os.path.exists(fileLocation)):
            raise RG_FileExistsError(fileLocation,
                            " 'RG_App_Shader' the parameter 'fileLocation' must be a file that exists.")
        self._location = fileLocation
        self.Image = PhotoImage(file = self.Location)
        self.Dimensions = RG_Size(self.Image.width(),self.Image.height())

    
    
    def __init__(self,screen:Canvas, fileLocation:str = None, offset: RG_Vector2D = None) -> None:
        #-----------defaults-----------
        # screen
        if not (type(screen) is Canvas):
            raise RG_TypeError(screen,
                                " An 'RG_App_Shader' must have 'self.MainWindow.Screen' as the argument 'screen' (first argument).")
        self._screen = screen
        
        self.Location = fileLocation
        
        #offset
        if (offset is None):
            offset = RG_Vector2D()
        elif not (type(offset) is RG_Vector2D):
            raise RG_TypeError(offset,
                                " 'RG_App_Shader' must have an RG_Vector2D as the argument 'offset' (last argument).")
        self.OffSet = offset
        pass;
    
    # To String
    def __str__(self) -> str:
        return "Shader: (ShaderID: " + str(self._canvasID) + ", File Location: " + str(self.Location) + ", OffSet: " + str(self.OffSet) + ")";

    # ----------------------------------
    #            Functions:
    # ----------------------------------
    def _createGfx(self, spritePosition: RG_Position2D) -> str:
        absolutePosition = spritePosition + self.OffSet;
        ID = self._screen.create_image(
            absolutePosition.X, (self._screen.winfo_height()-absolutePosition.Y),
            image=self.Image
            );
        return ID;
    
    
    
    def _configureGfx(self):
        
        self._screen.itemconfigure(self._canvasID,
            image=self.Image)
        pass;
    
    def Resize(self, x, y):
        xst = str(x)
        if not ("." in xst):
            xz = x
            xs = 1
        else:
            decs = xst.split(".")[1]
            xs = 10**len(decs)
            xz = xs*x
        yst = str(y)
        if not ("." in yst):
            yz = y
            ys = 1
        else:
            decs = yst.split(".")[1]
            ys = 10**len(decs)
            yz = ys*y
        self.Image = self.Image.zoom(int(xz),int(yz))
        self.Image = self.Image.subsample(int(xs),int(ys))
        self._screen.itemconfigure(self._canvasID,
            image=self.Image)
        pass;
    
    pass;
from tkinter import*
from threading import*
from multiprocessing import*
from concurrent.futures import ThreadPoolExecutor

class RG_RenderingManager:

    # Variables
    # window
    Window:Tk = None;
    Screen:Canvas = None;
    
    #Frame rate
    FrameRate:ref = ref(24);
    _pause:float = 1/FrameRate.Value;
    
    #Running
    BlockRender:bool = False;
    Run:bool = True
    FailedRenderCount:int = 0;
        
    Ended = False;
    Exceptions = []
    

    # Constructor (Where it starts)
    def __init__(self, mainScript, window:Tk, frameRate:ref = ref(30), scripts:ref = ref([]), failedRenderFailsafe:ref = ref(10), width:int=600, height:int=400, backGround:ref = ref("Black"), appearances:ref = ref([])):
        
        print("Main\\Init\\MainWindow> Started  | creating -> Render");
        
        print("\nMain\\Init\\MainWindow\\Render> Started  | creating -> General Values");
        try:
            self._mainScript = mainScript;
            self.Window = window;
            self._renderList = scripts;
            self._appearances = appearances;
            self._width = width;
            self._height = height;
            self._backGround = backGround;
            self._failedRenderFailsafe = failedRenderFailsafe;
        except Exception as e:
            print("Failed initializing general input variables.\n\n");
            raise e;
        print("Main\\Init\\MainWindow\\Render> Finished | creating -> General Values");
        
        print("Main\\Init\\MainWindow\\Render> Started  | setting -> Frame Rate ");
        try:
            self.FrameRate = frameRate;
            self._oldFrameRate = self.FrameRate.Value;
            self._pause = 1/frameRate.Value;
        except Exception as e:
            print("Failed to initialize frame rate.\n\n");
            raise e;
        print("Main\\Init\\MainWindow\\Render> Finished | setting -> Frame Rate ");
        
        print("Main\\Init\\MainWindow\\Render> Started  | creating -> Canvas");
        try:
            self.Screen = Canvas(self.Window, width = width, height = height, bg = backGround);
        except Exception as e:
            print("Failed to create Canvas.\n\n");
            raise e;
        print("Main\\Init\\MainWindow\\Render> Finished | creating -> Canvas");
        
        print("Main\\Init\\MainWindow\\Render> Started  | printing -> Canvas");
        try:
            self.Screen.pack();
        except Exception as e:
            print("Failed to put Canvas on window.\n\n");
            raise e;
        print("Main\\Init\\MainWindow\\Render> Finished | printing -> Canvas");
        
        print("\nMain\\Init\\MainWindow> Finished | creating -> Render");
        self.timer = RG_Timer(self._mainScript)
        self.executor = ThreadPoolExecutor(cpu_count())

    def StartRendering(self, width:int=600, height:int=400, backGround:ref = ref("Black")):
        
        print("Main\\Start up\\MainWindow> Started  | configuring -> Canvas");
        self.Screen.config(width = width, height = height, bg = backGround);
        print("Main\\Start up\\MainWindow> Finished | configuring -> Canvas");
        print("Main\\Start up\\MainWindow> Starting | Render");
        
        try:
            self.p = Thread(target = self.StartRender);
            self.p.start()
            self.Window.protocol("WM_DELETE_WINDOW", self.End);
            self.Window.mainloop()
        except Exception as e:
            print("Failed to start the rendering.\n\n");
            raise e;

        pass;
    
    
    #Render
    def StartRender(self):
        print("Main\\Start up\\MainWindow> Started  | Render");
        print("\nMain\\Start up> Started  | MainWindow");
        print("\nMain> Finished  | Start up\n");
        self._mainScript.Started = True;
        self.Render();
    
    def Render(self):
        self.timer.Subscribe()
        while self.Run:
            try:
                if(self.Ended) : return;
                Pause(self._pause-self.timer.Count);
                self.timer.Reset()
                self.DoRender()
            except Exception as e:
                if self.HandleExp(e): return
        pass;
    
    def HandleExp(self,e):
        if(self.Ended) : return True;
        print("Failed Render.");
        if(not self.Run): return True;
        if(issubclass(type(e),RG_Exception)):
            LogError(e.Message,e.Value)
            pass
        elif(len(e.args)>0):LogError(e.args[0])
        else:LogError("There was an exception raised without a message.")
        self.FailedRenderCount += 1;
        if(self.FailedRenderCount == self._failedRenderFailsafe.Value): 
            text = f" > Max Failed Render count surpassed. Current failsafe: {self._failedRenderFailsafe.Value}.\n > The error:\n\n"
            
            if(issubclass(type(e),RG_Exception)):
                LogFatal(text + e.Message,e.Value)
                pass
            elif(len(e.args)>0):LogFatal(text + e.args[0])
            else:LogFatal(text + "There was an exception raised without a message.")
            self.End()
    
    def DoRender(self):
        if(self.Ended) : return;
        if(self._oldFrameRate != self.FrameRate.Value):
            self._oldFrameRate = self.FrameRate.Value
            self._pause = 1/self.FrameRate.Value
        self._mainScript.render()
        self.DoRend()
        self.executor.map(self.Display, self._appearances.Value)
        for e in self.Exceptions:
            raise e
    
    def DoRend(self):
        if(self.Ended) : return
        for Src in self._renderList.Value:
            Src.Render()
            pass

    def Display(self,Src):
        try:
            Src.Appearance.Render()
        except Exception as e:
            self.Exceptions.append(e)
    
    def End(self):
        if(self.Ended) : return;
        self.Ended  = True;
        self.Run = False;
        print("\nMain> Started  | Ending .")
        print("Main\\Ending> Started  | ending  -> physics.")
        self._mainScript.MainPhysics.End();
        while self._mainScript.MainPhysics.Running:pass
        print("Main\\Ending> Finished | ending  -> physics.")
        print("Main> Finished | Ending.")
        self.Window.destroy()

    async def des(self):
        pass
    pass;
from enum import Enum
from tkinter import*
from concurrent.futures import ThreadPoolExecutor

class RG_WindowMode(Enum):
    TKINTER = 0
    PYGAME = 0

class RG_MainWindow:
    WindowTitle:str = "RGame"
    WindowHeight:int = 500
    WindowWidth:int = 800
    WindowBackground:str = "White"
    WindowIcon:str = None
    FrameRate:ref = ref(30);
    FailedRenderFailsafe:ref = ref(3)
    RenderingManager:RG_RenderingManager = None
    SpriteRender:ref = ref([])
    Appearances:ref = ref([])
    Activate:bool = True
    
    
    def __init__(self, mainScr, frameRate = ref(30)):
        if(mainScr == None) : return;
        self.MainScript = mainScr;
        self.FrameRate = frameRate;
        print("Main\\Init\\MainWindow> Started  | creating -> Window");
        self.Window = Tk()
        print("Main\\Init\\MainWindow> Finished | creating -> Window");
        print("Main\\Init\\MainWindow> Started  | creating -> Rendering");
        try:
            self.RenderingManager = RG_RenderingManager(
                self.MainScript, self.Window,
                self.FrameRate, self.SpriteRender, self.FailedRenderFailsafe,
                self.WindowWidth, self.WindowHeight, self.WindowBackground,
                self.Appearances
                )
        except Exception as e:
            print("Failed to initialize RenderingManager.\n\n")
            raise e;
        print("Main\\Init\\MainWindow> Finished | creating -> Rendering");
        self.Mouse = RG_Mouse(self.RenderingManager.HandleExp,self.WindowHeight)
        self.Mouse.bindEvents(self.Window)
    
    
    
    def Start(self):
        print("Main\\Start up> starting | MainWindow")
        if(not self.Activate):
            print("Main\\Start up\\MainWindow> Report   | MainWindow.Activate is set to False so window will not start)");
            
            self.Window.after(1,self.Window.destroy)
            mainloop()
            print("Main> Finished | Start up");
            return;
        
        self.CreateWindow()
        
        
        self.RenderingManager.StartRendering(self.WindowWidth, self.WindowHeight, self.WindowBackground);
        pass;
    
    
    
    def CreateWindow(self):
        print("\nMain\\Start up\\MainWindow> Started  | configuring -> Window\n");
        print("Main\\Start up\\MainWindow\\configuring> Started  | setting  -> Title");
        self.Window.title(self.WindowTitle);
        print("Main\\Start up\\MainWindow\\configuring> Finished | setting  -> Title");
        #photo = PhotoImage(file = self.WindowIcon);
        #self.MainWindow.iconphoto(False, photo);
        print("Main\\Start up\\MainWindow\\configuring> Started  | setting  -> Icon");
        if(self.WindowIcon != None):
            self.Window.iconbitmap(self.WindowIcon);
        print("Main\\Start up\\MainWindow\\configuring> Finished | setting  -> Icon");
        print("Main\\Start up\\MainWindow\\configuring> Started  | setting  -> Max Size (will be separate to min in a future update)");
        self.Window.maxsize(self.WindowWidth,self.WindowHeight);
        print("Main\\Start up\\MainWindow\\configuring> Finished | setting  -> Max Size");
        print("Main\\Start up\\MainWindow\\configuring> Started  | setting  -> Min Size");
        self.Window.minsize(self.WindowWidth,self.WindowHeight);
        print("Main\\Start up\\MainWindow\\configuring> Finished | setting  -> Min Size");
        print("\nMain\\Start up\\MainWindow> Finished | configuring -> Window");
        pass;
    
    
    
    def Add(self, script:RG_Script): 
        self.SpriteRender.Value.append(script)
        self.Appearances.Value.append(script)
        pass;
    
    def Exists(self, script:RG_Script): 
        return 0 < self.SpriteRender.Value.count(script)
    
    def Remove(self, script): 
        if(len(self.SpriteRender.Value) == 0): return
        self.SpriteRender.Value.remove(script)
        self.Appearances.Value.remove(script)
        pass;
    
    def Bind(self,BindKey, Bind):
        self.Window.bind(BindKey,Bind)
    
    
    
    
            
        
    @property
    def Screen(self):
        return self.RenderingManager.Screen
    
class RG_Mouse:
    
    def __init__(self, handleExp, height):
        self.winH = height
        self._handleExp = handleExp
        self.executor = ThreadPoolExecutor()
    
    Left = False
    Middle = False
    Right = False
    ScrollDelta = 0
    DoubleClickDelta = 0.5
    DoubleClickTimePoint = RG_TimePoint()
    OnSecondClick = False
    DragDeltaMovement = 3
    Drag = False
    
    def BindLeftDown(self, bind):
        self._leftDown.append(bind)
        
    def BindLeftUp(self, bind):
        self._leftUp.append(bind)
        
    def BindMiddleDown(self, bind):
        self._middleDown.append(bind)
        
    def BindMiddleUp(self, bind):
        self._middleUp.append(bind)
        
    def BindRightDown(self, bind):
        self._rightDown.append(bind)
        
    def BindRightUp(self, bind):
        self._rightUp.append(bind)
        
    def BindDoubleClick(self, bind):
        self._doubleClick.append(bind)
        
    def BindMove(self, bind):
        self._move.append(bind)
        
    def BindDrag(self, bind):
        self._drag.append(bind)
        
    def BindScroll(self, bind):
        self._scroll.append(bind)
    
    def bindEvents(self, window):
        window.bind("<1>",self.leftDown)
        window.bind("<ButtonRelease-1>",self.leftUp)
        window.bind("<2>",self.middleDown)
        window.bind("<ButtonRelease-2>",self.middleUp)
        window.bind("<3>",self.rightDown)
        window.bind("<ButtonRelease-3>",self.rightUp)
        window.bind("<Motion>",self.move)
        window.bind("<MouseWheel>",self.scroll)
    
    _leftDown:list = []
    def leftDown(self, args):
        self.Left = True
        for func in self._leftDown:
            try: 
                if(func(args)):
                    break
            except Exception as e:
                if(self._handleExp(e)): return
            
    _doubleClick:list = []
    def doubleClick(self, args):
        if not (self.OnSecondClick):
            self.OnSecondClick = True
            self.DoubleClickTimePoint.Now()
            return
        self.OnSecondClick = False
        
        if (self.DoubleClickTimePoint.Diff() > self.DoubleClickDelta):
            return
        
        for func in self._doubleClick:
            try: 
                if(func(args)):
                    break
            except Exception as e:
                if(self._handleExp(e)): return
    
    _leftUp:list = []
    def leftUp(self, args):
        self.Left = False
        self.Drag = False
        self.executor.submit(self.doubleClick, args)
        for func in self._leftUp:
            try: 
                if(func(args)):
                    break
            except Exception as e:
                if(self._handleExp(e)): return
            
    _middleDown:list = []
    def middleDown(self, args):
        self.Middle = True
        for func in self._middleDown:
            try: 
                if(func(args)):
                    break
            except Exception as e:
                if(self._handleExp(e)): return
    
    _middleUp:list = []
    def middleUp(self, args):
        self.Middle = False
        for func in self._middleUp:
            try: 
                if(func(args)):
                    break
            except Exception as e:
                if(self._handleExp(e)): return
            
    _rightDown:list = []
    def rightDown(self, args):
        self.Right = True
        for func in self._rightDown:
            try: 
                if(func(args)):
                    break
            except Exception as e:
                if(self._handleExp(e)): return
    
    _rightUp:list = []
    def rightUp(self, args):
        self.Right = False
        for func in self._rightUp:
            try: 
                if(func(args)):
                    break
            except Exception as e:
                if(self._handleExp(e)): return
                
    _drag:list = []
    LastPos = RG_Position2D()
    Position = RG_Position2D()
    DeltaMovement = RG_Vector2D()
    def drag(self, args):
        if not (self.Left): return
        if not(self.Drag):
            if not (self.DeltaMovement.GetlengthSqr() > self.DragDeltaMovement*self.DragDeltaMovement): return
        self.Drag = True
        for func in self._drag:
            try: 
                if(func(args)):
                    break
            except Exception as e:
                if(self._handleExp(e)): return
                
    _move:list = []
    def move(self, args):
        self.LastPos = self.Position
        self.Position = RG_Position2D(args.x, self.winH-args.y)
        self.DeltaMovement = self.LastPos.VectorTo(self.Position)
        self.drag(args)
        for func in self._move:
            try: 
                if(func(args)):
                    break
            except Exception as e:
                if(self._handleExp(e)): return
    
    _scroll:list = []
    def scroll(self, args):
        self.ScrollDelta += args.delta
        for func in self._scroll:
            try: 
                if(func(args)):
                    break
            except Exception as e:
                if(self._handleExp(e)): return
#MainScr class
class RG_Script:
    Activated = False;
    Velocity:RG_Velocity2D = RG_Velocity2D(0,0);
    Position:RG_Position2D = RG_Position2D(0,0);
    Name:str = "Script";
    _id = 0;
    rending = True;

    
    def __init__(self,mainScript, position:RG_Position2D = None, velocity:RG_Velocity2D = None, appearance:RG_AppearanceType = None, name:str = "Script") -> None:
        
        self.Before();
        
        #mainScript
        self.MainScript = mainScript;
        
        #pos
        if (position is None):
            position = RG_Position2D()
        elif not (type(position) is RG_Position2D):
            raise RG_TypeError(position,
                                " 'RG_Script' must have an RG_Position2D as the argument 'position' (second argument).")
        self.Position = position;
        
        #vel
        if (velocity is None):
            velocity = RG_Velocity2D()
        elif not (type(velocity) is RG_Velocity2D):
            raise RG_TypeError(velocity,
                                " 'RG_Script' must have an RG_Velocity2D as the argument 'velocity' (third argument).")
        self.Velocity = velocity;
        
        self.MainWindow = self.MainScript.MainWindow;
        #appearance
        if (appearance is None):
            appearance = None
        elif not issubclass(type(appearance), RG_AppearanceType):
            raise RG_TypeError(appearance,
                                " 'RG_Script' must have an RG_AppearanceType the argument 'appearance' (fourth argument).")
        self.Appearance = appearance;
        
        #name
        if (name is None):
            name = "script"
        elif not (type(name) is str):
            raise RG_TypeError(name,
                                " 'RG_Script' must have a string as the argument 'name' (last argument).")
        self.Name = name;
        
        self.ScreenWidth = self.MainWindow.WindowWidth;
        self.ScreenHeight = self.MainWindow.WindowHeight;
        self.MainPhysics = self.MainScript.MainPhysics;
        self.Start();
        self.Activate()
        pass
    
    def MoveTo(self,x,y):
        self.Position.X = x;
        self.Position.Y = y;
        if not (self.Appearance is None):
            self.Appearance.MoveTo(x,y)
        pass;
    
    def Activate(self):
        if(self.Activated): return
        self.Activated = True;
        if not (self.Appearance is None):
            self.Appearance.Show();
        self.MainWindow.Add(self);
        self.MainPhysics.Add(self);
        pass;
    
    def Deactivate(self):
        if not (self.Activated): return
        self.Activated = False;
        self.MainPhysics.Remove(self);
        if not (self.Appearance is None):
            self.Appearance.Hide();
        self.MainWindow.Remove(self);
        self.rending = False;
        pass;
    
    
    # ----------------------------------
    #          Bounce:
    # ----------------------------------
    
    def Bounce(self):
        pos = self.Position - self.Appearance.OffSet;
        bounced = False;
        if(pos.X < 0 ): 
            self.Position.X += 0 - pos.X;
            self.Velocity.X *= -1;
            bounced = True;

        if(pos.X + self.Appearance.Dimensions.Width >  self.ScreenWidth): 
            self.Position.X += (self.ScreenWidth - self.Appearance.Dimensions.Width)-pos.X;
            self.Velocity.X *= -1;
            bounced = True;

        if(pos.Y < 0): 
            self.Position.Y += 0 - pos.Y;
            self.Velocity.Y *= -1;
            bounced = True;

        if( self.Appearance.Dimensions.Height + pos.Y >  self.ScreenHeight): 
            self.Position.Y += (self.ScreenHeight - self.Appearance.Dimensions.Height)-pos.Y;
            self.Velocity.Y *= -1;
            bounced = True;

        return bounced;
    
    # axial bounce
    def BounceY(self):
        pos = self.Position + self.Appearance.OffSet;
        bounced = False;
        
        if(pos.Y < 0): 
            self.Position.Y = self.Appearance.OffSet.Y;
            self.Velocity.Y *= -1;
            bounced = True;

        if(pos.Y >=  self.ScreenHeight - self.Appearance.Dimensions.Height): 
            self.Position.Y = self.ScreenHeight + self.Appearance.Dimensions.Height + self.Appearance.OffSet.Y;
            self.Velocity.Y *= -1;
            bounced = True;
        
        return bounced;
    
    def BounceX(self):
        pos = self.Position+ self.Appearance.OffSet;
        bounced = False;
        
        if(pos.X < 0 ): 
            self.Position.X = self.Appearance.OffSet.X;
            self.Velocity.X *= -1;
            bounced = True;

        if(pos.X >=  self.ScreenWidth - self.Appearance.Dimensions.Width): 
            self.Position.X = self.ScreenWidth - self.Appearance.Dimensions.Width + self.Appearance.OffSet.X;
            self.Velocity.X *= -1;
            bounced = True;
        
        return bounced;
    
    # sides bounce
    def BounceRight(self):
        pos = self.Position + self.Appearance.OffSet;
        bounced = False;
        
        if(pos.X >=  self.ScreenWidth - self.Appearance.Dimensions.Width): 
            self.Position.X = self.ScreenWidth - self.Appearance.Dimensions.Width + self.Appearance.OffSet.X;
            self.Velocity.X *= -1;
            bounced = True;

        
        return bounced;
    
    def BounceLeft(self):
        
        pos = self.Position + self.Appearance.OffSet;
        bounced = False;
        
        if(pos.X < 0 ): 
            self.Position.X = self.Appearance.OffSet.X;
            self.Velocity.X *= -1;
            bounced = True;

        
        return bounced;
    
    def BounceBottom(self):
        pos = self.Position + self.Appearance.OffSet;
        bounced = False;

        if(pos.Y >=  self.ScreenHeight - self.Appearance.Dimensions.Height): 
            self.Position.Y = self.ScreenHeight - self.Appearance.Dimensions.Height + self.Appearance.OffSet.Y;
            self.Velocity.Y *= -1;
            bounced = True;

        
        return bounced;
    
    def BounceTop(self):
        pos = self.Position + self.Appearance.OffSet;
        bounced = False;
        
        if(pos.Y < 0): 
            self.Position.Y = self.Appearance.OffSet.Y;
            self.Velocity.Y *= -1;
            bounced = True;
            
        
        return bounced;
    
    
    def Before(self):
        pass;
    
    def Start(self):
        pass;
    
    def Tick(self,deltaTime):
        if not (self.MainWindow.RenderingManager.Run):return
        if not (self.MainPhysics.Running):return
        vel =  self.Velocity*deltaTime;
        self.Position.Move(vel);
        try:
            self.PhysicsTick(self.MainPhysics.DeltaTime)
        except Exception as e:
            if(issubclass(type(e),RG_Exception)):
                LogError(e.Message,e.Value)
                pass
            else:LogError(e.args[0])
            self.MainPhysics.FailedTickCount  += 1;
            if(self.MainPhysics.FailedTickCount == self.MainPhysics.FailedTickFailsafe): 
                text = f" > Max Failed PhysicsTick count surpassed. Current failsafe: {self.MainPhysics.FailedTickFailsafe}.\n > The error:\n\n"
                if(issubclass(type(e),RG_Exception)):
                    LogFatal(text + e.Message,e.Value)
                    pass
                else:LogFatal(text + e.args[0])
                self.MainWindow.RenderingManager.End()
        if self.MainWindow.RenderingManager.Run:
            self.MoveTo(self.Position.X,self.Position.Y)
        pass;
    
    def PhysicsTick(self,deltaTime):
        
        pass;
            
    def Render(self):
        if not (self.Appearance is None):
            self.Appearance.Render()
        pass;
    
    pass;

class RG_Circle(RG_Script):

    def __init__(self, mainScript, position: RG_Position2D = None, velocity: RG_Velocity2D = None, radius:float = None, color:str = None, OffSet:RG_Vector2D = None, name: str = None ) -> None:
        super().__init__(mainScript, position=position, velocity=velocity, appearance=RG_App_Circle(mainScript.MainWindow.Screen, radius, color,OffSet ), name=name)
        
class RG_Ellipse(RG_Script):

    def __init__(self, mainScript, position: RG_Position2D = None, velocity: RG_Velocity2D = None, radiusX:float = None, radiusY:float = None, color:str = None, OffSet:RG_Vector2D = None, name: str = None ) -> None:
        super().__init__(mainScript, position=position, velocity=velocity, appearance=RG_App_Ellipse(mainScript.MainWindow.Screen, radiusX, radiusY, color,offset=OffSet  ), name=name)

class RG_Rectangle(RG_Script):

    def __init__(self, mainScript, position: RG_Position2D = None, velocity: RG_Velocity2D = None, width:float = None, height:float = None, color:str = None, OffSet:RG_Vector2D = None, name: str = None) -> None:
        super().__init__(mainScript, position=position, velocity=velocity, appearance=RG_App_Rectangle(mainScript.MainWindow.Screen, RG_Size(width, height), color ,offset=OffSet ), name=name)

class RG_Line(RG_Script):

    def __init__(self, mainScript, position: RG_Position2D = None, velocity: RG_Velocity2D = None, points:list[RG_Vector2D] = None, color:str = None, width:int = None, smooth:bool = None, resolution:int = None, Offset:RG_Vector2D = None, name: str = None ) -> None:
        super().__init__(mainScript, position=position, velocity=velocity, appearance=RG_App_Line(mainScript.MainWindow.Screen, points, color, width, smooth, resolution, Offset), name=name)
        
class RG_Label(RG_Script):

    def __init__(self, mainScript, position: RG_Position2D = None, velocity: RG_Velocity2D = None, text:str = None, fontType:str = None, fontSize:int = None, fontColor:str = None, bold:bool = None, italic:bool = None, underline:bool = None, overstrike:bool = None, Offset:RG_Vector2D = None, name: str = None ) -> None:
        super().__init__(mainScript, position=position, velocity=velocity, appearance=RG_App_Label(mainScript.MainWindow.Screen, text, fontType, fontSize,fontColor, bold, italic, underline, overstrike, Offset), name=name)

class RG_Image(RG_Script):

    def __init__(self, mainScript, position: RG_Position2D = None, velocity: RG_Velocity2D = None, fileLocation:str = None, OffSet:RG_Vector2D = None, name: str = None ) -> None:
        super().__init__(mainScript, position=position, velocity=velocity, appearance=RG_App_Shader(screen = mainScript.MainWindow.Screen,fileLocation= fileLocation,offset=OffSet ), name=name)
#MainScr class
class RG_MainScript:
    _beforeOverride = False
    _mainOverride = False
    _physicsTickOverride = False
    _renderOverride = False
    
    def __init__(self, before = None, main = None, physicsTick = None, render = None) -> None:
        if not before is None:
            self.Before = before
            self._beforeOverride = True
        if not main is None:
            self.Main = main
            self._mainOverride = True
        if not physicsTick is None:
            self.PhysicsTick = physicsTick
            self._physicsTickOverride = True
        if not render is None:
            self.Render = render
            self._renderOverride = True
        self.Started = False
        self.Stop = False
    
    def StartRGame(self):
        
        TimeInit()
        try:    
            if self._beforeOverride:
                self.Before(self)
            else: self.Before()
        except Exception as e:
            print("In Before - before everything.\n")
            raise e
        
        if(self.Stop):
            return
        self.Started = True
        
        print("Main> Started  | Init ( initialization - where things get first created )")
        self.INIT()
        print("Main> Finished | Init")
        try:    
            if self._mainOverride:
                self.Main(self)
            else: self.Main()
        except Exception as e:
            print("In MainScript Main\n")
            raise e;
        
        print("Main> Started  | Start up ( where physics and rendering are first started )")
        self.Exp = None;
        self.Start();
    
    def INIT(self):
        print()
        # Intervals
        # physics
        self.TickInterval =  0.05;
        print("Main\\Init> Done     | setting  -> Physics Tick Interval.")
        
        # rendering
        self.FrameRate = ref( 10 );
        print("Main\\Init> Done     | setting  -> Frame Rate.")
        
        # Managers
        # physics
        print("Main\\Init> Started  | creating -> Main Physics");
        self.MainPhysics = RG_MainPhysics(self, self.TickInterval);
        print("Main\\Init> Finished | creating -> Main Physics")
        
        # rendering
        print("Main\\Init> Started  | creating -> Main Window");
        self.MainWindow = RG_MainWindow(self, self.FrameRate);
        print("Main\\Init> Finished | creating -> Main Window");
        print()
    
        
        pass;
    
    def Before(self):
        pass;
    
    def Main(self):
        pass;
    
    def Start(self):
        self.MainPhysics.Interval = self.TickInterval;
        print()
        print("Main\\Start up> Starting | Main Physics Tick")
        self.MainPhysics.Start()
        print("Main\\Start up> Started  | Main Physics Tick")
        print("Main\\Start up> Starting | Main Window Rendering")
        self.MainWindow.Start()
        pass;
    
    
    def tick(self, deltatime):
        if not (self.MainPhysics.Running):return
        try:
            
            if self._physicsTickOverride:
                self.PhysicsTick(self, deltatime)
            else: self.PhysicsTick(deltatime)
        except Exception as e:
            if(issubclass(type(e),RG_Exception)):
                LogError(e.Message,e.Value)
                pass
            else:LogError(e.args[0])
            self.MainPhysics.FailedTickCount += 1
            if(self.MainPhysics.FailedTickCount == self.MainPhysics.FailedTickFailsafe): 
                text = f" > Max Failed PhysicsTick count surpassed. Current failsafe: {self.MainPhysics.FailedTickFailsafe}.\n > The error:\n\n"
                if(issubclass(type(e),RG_Exception)):
                    LogFatal(text + e.Message,e.Value)
                    pass
                else:LogFatal(text + e.args[0])
                self.MainWindow.RenderingManager.End()
    
    
    def PhysicsTick(self,deltatime):
        pass
    
    def render(self):
        if self._physicsTickOverride:
            self.Render(self)
        else: self.Render()
        
    def Render(self):
        pass;
    
    def End(self):
        self.MainWindow.RenderingManager.End()
    
    pass;
class Run:
    def __init__(self, main:RG_MainScript) -> None:
        """
        Run is a functor which runs your program with your custom main class

        :param main: Your Main class which derives from RG_MainScript
        """
        
        import os
        os.system("color 00")
        try:
            main.StartRGame()
            print("Started | Main\n")
            if(main.Started):
                main.MainPhysics.End()
        except RG_Exception as e:
            if not (e.Value is None):
                LogFatal(e.Message, e.Value)
            else: 
                LogFatal(e.Message)
        except Exception as e:
            if(len(e.args)>0):
                LogFatal(e.args[0])
        input("\nFinished | Main (press enter to close window): ")
