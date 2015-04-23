import maya.cmds as cmds
count = 0
inList = []
keyList = []
nameSpace = []
timeStep = 60
hash = '#'
backslash = '\\'
anList = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','!','@', hash,'$','%','^','&','*','(',')','-','_','=','+','/','?','~','<','>',':',';',',','.']



#check for existing window - delete if one exists.
if cmds.window("UI_flip", exists =True) :
    cmds.deleteUI("UI_flip")

#create window
window = cmds.window("UI_flip", title="Flip Display", w=500, h =150)

cmds.rowColumnLayout()
cmds.separator( height=20, style='none' )

cmds.textField('in_fld', w=500)
cmds.separator( height=20, style='in' )
#show window
cmds.button(l='Set Frames', w=210, h=25, c='btn_start()')
cmds.showWindow(window)


def makekeyList():
    del inList[:]
    del keyList[:]
    inputField=cmds.textField('in_fld', q=True, tx=True)
    inList[:0] = inputField
    
    for element in inList:
        if element in anList:
            keyList.append(anList.index(element))
        
def getnameSpace():
    
    nsInfo = cmds.namespaceInfo(lon=True)
    for name in nsInfo:
        if cmds.objExists(name + ':flip_ring_GEO'):
            nameSpace.append(name)
        print nameSpace
        
   
    
def makekeyFrameS():
    
    count=0
    print count
    timeS = cmds.currentTime(query=True)
    
    for i in keyList:    
        fName = nameSpace[count]
        cmds.setKeyframe(fName+':flip_ring_GEO', attribute='flip', t=timeS, v=0)
        count = count +1
        print count


def makekeyFrameE():
    count=0
    lCount = 0
    kCount = len(keyList) - 1
    timeE = cmds.currentTime(query=True) + (keyList[count]*3)
    
    for i in keyList:    
        fName = nameSpace[count]
        cmds.setKeyframe(fName+':flip_ring_GEO', attribute='flip', t=timeE, v=keyList[count])
        
        if lCount < kCount:
            lCount = lCount+1
            count = count +1
            timeE = cmds.currentTime(query=True) + (keyList[count]*3)
                  
def makekeyFrameH():
    count=0
    timeH = cmds.currentTime(query=True) + (timeStep*3)
    
    for i in keyList:    
        fName = nameSpace[count]
        cmds.setKeyframe(fName+':flip_ring_GEO', attribute='flip', t=timeH, v=keyList[count])
        count = count +1

def makekeyFrameR():
    count=0
    llCount = 0
    kkCount = len(keyList) - 1
    timeR = cmds.currentTime(query=True) + (timeStep*3) + (60-keyList[count])
    
    for i in keyList:    
        fName = nameSpace[count]
        cmds.setKeyframe(fName+':flip_ring_GEO', attribute='flip', t=timeR, v=60)
        
        if llCount < kkCount:
            llCount = llCount+1
            count = count +1
            timeR = cmds.currentTime(query=True) + (timeStep*3) + (60-keyList[count])
            print 'this is timeR:'
            print timeR      
    
    
def setcurrentTime():
    fName = nameSpace[count]
    currTime = cmds.currentTime(query=True) + (timeStep*3) + (60 - min(keyList))   
    cmds.currentTime( currTime +1, edit=True )
    cmds.setKeyframe(fName+':flip_ring_GEO', attribute='flip', t=currTime+1, v=60)
    cmds.currentTime( currTime +2, edit=True )


def btn_start():
    makekeyList()
    makekeyFrameS()
    makekeyFrameE()
    makekeyFrameH()
    makekeyFrameR()
    setcurrentTime()  

getnameSpace() 


