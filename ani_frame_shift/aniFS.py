import maya.cmds as cmds

class TestWindow():
    def __init__(self):
        self.widgets = {}
        self.name = ['t','r','s','ca']
        self.lName = ['Translate', 'Rotate', 'Scale', 'Custom Attr']
        self.axis = ['X','Y','Z']
        self.e = 0
        self.E = 0
        self.sel = []
        self.UD = []
        self.caList = []
        
    def buildUI(self):
        ## delete UI window if one already exists
        if cmds.window('AniFrameShift', exists=True):
            cmds.deleteUI('AniFrameShift')

        self.widgets["window"] = cmds.window('AniFrameShift',w=450, h =400, mnb=True, mxb=False, rtf=True)
        ## builds UI elements - each attribute category in its own framelayout
        for element in self.name:  
            self.E = self.name.index(element)
            cmds.columnLayout( adjustableColumn=True )
            self.widgets[self.lName[self.E]+'frameLayout']=cmds.frameLayout( l=self.lName[self.E],cll =True)
            cmds.rowColumnLayout(numberOfColumns=3,cal =[1,'left'],columnWidth=[(1, 90), (2, 60)], p=self.widgets[self.lName[self.E]+'frameLayout'])
            ## create XYZ checkboxes for translation/rotation/scale and fields for frame shift values.
            ## once condition is met, creates field for selecting user defined attributes (plus visibility) and shift value frame.
            if (self.E +1) == len(self.name):
                cmds.separator( height=20, style='none' )
                self.caSL=cmds.textScrollList(ams=True, w =250)
                cmds.separator( height=20, style='none' )
                cmds.separator( height=20, style='none' )
                self.widgets['shift' + self.name[self.E].upper()] = cmds.intField('shift' + self.name[self.E], h = 20, w=110)
            else:
                for element in self.axis:
                    self.e = self.axis.index(element)
                    cmds.separator( height=20, style='none' )
                    self.widgets[self.name[self.E] + self.axis[self.e].upper() + 'BOX'] = cmds.checkBox(l= self.axis[self.e])
                    self.widgets['shift' + self.name[self.E] + self.axis[self.e]] = cmds.intField('shift' + self.axis[self.e])
            ## create two radio button sets
            ## 1. shift mode - for shifting frames relative to current frame position or for absolute frame values on timeline. (default - relative)
            ## 2. frame mode - for shifting single keyframes, a range of keyframes or all keyframes for each translate/rotate/scale/user defined (default - single)
            cmds.rowColumnLayout(numberOfColumns=1,cal =[1,'left'], p=self.widgets[self.lName[self.E]+'frameLayout'])
            self.widgets[self.name[self.E]+ 'ShiftType'] = cmds.radioButtonGrp(label='Shift Mode:', labelArray2=['Relative', 'Absolute'], numberOfRadioButtons=2, cc= 'raRadio()', sl =1)
            self.widgets[self.name[self.E]+ 'RadioFrame'] = cmds.radioButtonGrp(label='Frame Mode:', labelArray3=['Single', 'Range', 'All'], numberOfRadioButtons=3, cc= 'ccRadio()', sl =1)
            ## create fields for frame mode
            cmds.rowColumnLayout(numberOfColumns=3,cal =[1,'left'],columnWidth=[(1, 90)], p=self.widgets[self.lName[self.E]+'frameLayout'])
            cmds.separator( height=20, style='none' )
            self.widgets[self.name[self.E]+'RangeA'] = cmds.intField(self.name[self.E]+'rangea')
            self.widgets[self.name[self.E]+'RangeB'] = cmds.intField(self.name[self.E]+'rangeb', en=False)
                       
            cmds.setParent( '..' )
            cmds.setParent( '..' )

            cmds.showWindow(self.widgets["window"])
        else:
            ## create UI buttons
            cmds.separator( height=20, style='none' )
            cmds.rowColumnLayout(numberOfColumns=3)

            cmds.button(l='Shift', w=150, c='appclsBtn()')
            cmds.button(l='Apply', w=150, c='applyBtn()')
            cmds.button(l='Close', w=150, c='closeBtn()')



class Radio():
    ## checks for changes in radio buttons
    ## RTest - enables/disables fields for frame mode. 
    ## RATest - sets shift mode.
    def __init__(self):
        self.ccrEn = 0
        self.testFList=['S','R','A']
        self.testMList = ['R','A']
        self.testQMList = [True,True,True,True] 
    def RTest(self):
        for element in win.name:  
            win.E = win.name.index(element)
            self.frameR = win.widgets[win.name[win.E]+ 'RadioFrame']
            for i in range(len(self.testFList)):
                win.widgets[win.name[win.E]+ 'test'+self.testFList[i]] = cmds.radioButtonGrp(self.frameR, q = True, sl =i+1)
            if self.ccrEn == 1:
                if win.widgets[win.name[win.E]+ 'test'+self.testFList[i]] == 1:
                    self.TimeS()
                if win.widgets[win.name[win.E]+ 'test'+self.testFList[i]] == 2:
                    self.TimeR()
                if win.widgets[win.name[win.E]+ 'test'+self.testFList[i]] == 3:
                    self.TimeA()            
    def RATest(self):
        del self.testQMList[:]
        for element in win.name:  
            win.E = win.name.index(element)
            self.frameM = win.widgets[win.name[win.E]+ 'ShiftType']
            for i in range(len(self.testMList)):
                win.widgets[win.name[win.E]+ 'test'+self.testMList[i]] = cmds.radioButtonGrp(self.frameM, q = True, sl =i+1)        
            if self.ccrEn == 1:
                if win.widgets[win.name[win.E]+ 'test'+self.testMList[i]] == 1:
                    self.testQMList.append(True)
                if win.widgets[win.name[win.E]+ 'test'+self.testMList[i]] == 2:
                    self.testQMList.append(False)
                    
     
    def TimeS(self):
        cmds.intField(win.widgets[win.name[win.E]+'RangeA'], e=True, en=True)
        cmds.intField(win.widgets[win.name[win.E]+'RangeB'], e=True, en=False)        
    def TimeR(self):
        cmds.intField(win.widgets[win.name[win.E]+'RangeA'], e=True, en=True)
        cmds.intField(win.widgets[win.name[win.E]+'RangeB'], e=True, en=True)
    def TimeA(self):
        cmds.intField(win.widgets[win.name[win.E]+'RangeA'], e=True, en=False)
        cmds.intField(win.widgets[win.name[win.E]+'RangeB'], e=True, en=False)              

        
class Apply():
    def __init__(self):
        self.attr = ['.translate','.rotate','.scale']
        self.slQList = []
    def btn(self):
        win.sel = cmds.ls(sl = True)
        self.slQList = cmds.textScrollList(win.caSL, q=True, si=1)
        for i in range(len(win.sel)):
            for element in win.name:
                win.E = win.name.index(element)
                if (win.E +1) == len(win.name):   
                    if self.slQList == None:
                        pass
                    else:
                        win.widgets[win.name[win.E]+'D'] = cmds.intField(win.widgets['shift' + win.name[win.E].upper()], q=True, v=True)
                        for element in self.slQList:
                            self.CA = self.slQList.index(element)
                            win.widgets[win.name[win.E]+'A'] = cmds.intField(win.widgets[win.name[win.E]+'RangeA'], q=True, v=True)
                            win.widgets[win.name[win.E]+'B'] = cmds.intField(win.widgets[win.name[win.E]+'RangeB'], q=True, v=True)
                            if element in win.caList and (win.widgets[win.name[win.E]+'test'+RT.testFList[0]] == 1):
                                cmds.keyframe(self.slQList[self.CA], edit=True,relative=RT.testQMList[win.E], timeChange=win.widgets[win.name[win.E]+'D'],time=(win.widgets[win.name[win.E]+'A'],win.widgets[win.name[win.E]+'A']))
                            if element in win.caList and (win.widgets[win.name[win.E]+'test'+RT.testFList[1]] == 2):
                                if RT.testQMList[win.E] == True:
                                    cmds.keyframe(self.slQList[self.CA], edit=True,relative=RT.testQMList[win.E], timeChange=win.widgets[win.name[win.E]+'D'],time=(win.widgets[win.name[win.E]+'A'],win.widgets[win.name[win.E]+'B']))
                                else:
                                    cmds.cutKey(self.slQList[self.CA])
                                    cmds.pasteKey(self.slQList[self.CA], t = (win.widgets[win.name[win.E]+'D'],win.widgets[win.name[win.E]+'D']))                                      
                            if element in win.caList and (win.widgets[win.name[win.E]+'test'+RT.testFList[2]] == 3):
                                cmds.cutKey(self.slQList[self.CA])
                                cmds.pasteKey(self.slQList[self.CA], to = win.widgets[win.name[win.E]+'D'])
                else:
                    for element in win.axis:
                        win.e = win.axis.index(element)
                        win.widgets[win.name[win.E]+'A'] = cmds.intField(win.widgets[win.name[win.E]+'RangeA'], q=True, v=True)
                        win.widgets[win.name[win.E]+'B'] = cmds.intField(win.widgets[win.name[win.E]+'RangeB'], q=True, v=True)
                        win.widgets[win.name[win.E]+win.axis[win.e].upper()]=cmds.checkBox(win.widgets[win.name[win.E] + win.axis[win.e].upper() + 'BOX'], q=True, v=True)
                        win.widgets[win.name[win.E]+'C'+win.axis[win.e].upper()] = cmds.intField(win.widgets['shift' + win.name[win.E] + win.axis[win.e]], q=True, v=True)
                        if (win.widgets[win.name[win.E]+win.axis[win.e].upper()]) and (win.widgets[win.name[win.E]+'test'+RT.testFList[win.e]] == 1):
                            cmds.keyframe(win.sel[i]+self.attr[win.E]+win.axis[win.e].upper(), edit=True, relative=RT.testQMList[win.E], timeChange=win.widgets[win.name[win.E]+'C'+win.axis[win.e].upper()],time=(win.widgets[win.name[win.E]+'A'],win.widgets[win.name[win.E]+'A']))
                        if (win.widgets[win.name[win.E]+win.axis[win.e].upper()]) and (win.widgets[win.name[win.E]+'test'+RT.testFList[win.e]] == 2):
                            if RT.testQMList[win.E] == True:
                                cmds.keyframe(win.sel[i]+self.attr[win.E]+win.axis[win.e].upper(), edit=True, relative=RT.testQMList[win.E], timeChange=win.widgets[win.name[win.E]+'C'+win.axis[win.e].upper()],time=(win.widgets[win.name[win.E]+'A'],win.widgets[win.name[win.E]+'B']))
                            else:
                                cmds.cutKey(win.sel[i]+self.attr[win.E]+win.axis[win.e].upper(), time=(win.widgets[win.name[win.E]+'A'],win.widgets[win.name[win.E]+'B']))
                                cmds.pasteKey(win.sel[i]+self.attr[win.E]+win.axis[win.e].upper(), t =(win.widgets[win.name[win.E]+'C'+win.axis[win.e].upper()],win.widgets[win.name[win.E]+'C'+win.axis[win.e].upper()]))                                
                        if (win.widgets[win.name[win.E]+win.axis[win.e].upper()]) and (win.widgets[win.name[win.E]+'test'+RT.testFList[win.e]] == 3):
                            if RT.testQMList[win.E] == True:
                                cmds.cutKey(win.sel[i]+self.attr[win.E]+win.axis[win.e].upper())
                                cmds.pasteKey(win.sel[i]+self.attr[win.E]+win.axis[win.e].upper(), to = win.widgets[win.name[win.E]+'C'+win.axis[win.e].upper()])
                            else:
                                cmds.cutKey(win.sel[i]+self.attr[win.E]+win.axis[win.e].upper())
                                cmds.pasteKey(win.sel[i]+self.attr[win.E]+win.axis[win.e].upper(), t =(win.widgets[win.name[win.E]+'C'+win.axis[win.e].upper()],win.widgets[win.name[win.E]+'C'+win.axis[win.e].upper()]))    

                            
        
   
class ScriptJob():
    ## runs every time a change to current selection is made.
    ## 1. makes a list of current selection.
    ## 2. makes a list of all visible, keyable, unlocked user defined attributes.
    ## 3. makes a list of all other visible, keyable, unlocked attributes.
    ## 4. if visibilty is in list it is added as a selectable attr in UI.
    ## 5. if any user defined attr are available they are also added as selectable in UI.
    def __init__(self):
        self.UD =[]
        self.SD = []
        
    def caTest(self):
        cmds.textScrollList(win.caSL,e = True, ra=True)
        del win.sel[:]
        del win.caList[:]
        win.sel[:0]=cmds.ls(sl=True)
        
        for element in win.sel:
            self.e=win.sel.index(element)
            self.UD = cmds.listAttr(win.sel[self.e], v=True, k=True, u=True, ud=True)
            self.SD = cmds.listAttr(win.sel[self.e], v=True, k=True, u=True)
            if self.SD[0] == 'visibility':
                cmds.textScrollList(win.caSL, e=True, append = win.sel[self.e]+'.'+self.SD[0])
                win.caList.append(win.sel[self.e]+'.'+self.SD[0])
            if self.UD == None:
                pass  
            else:
                for u in self.UD:
                    self.U=self.UD.index(u)
                    cmds.textScrollList(win.caSL, e=True, append = win.sel[self.e]+'.'+self.UD[self.U])
                    win.caList.append(win.sel[self.e]+'.'+self.UD[self.U])

                    
def SJTest():
    SJ.caTest()
    
def raRadio():
    RT.ccrEn = 1
    RT.RATest()
                     
def ccRadio():
    RT.ccrEn = 1
    RT.RTest()
    
def applyBtn():
    RT.ccrEn = 0
    RT.RTest()
    AB.btn()    
        
def appclsBtn():
    RT.ccrEn = 0
    RT.RTest()
    AB.btn()
    closeBtn()

def closeBtn():
    if cmds.window('AniFrameShift', exists=True):
        cmds.deleteUI('AniFrameShift')
 
SJ = ScriptJob() 
AB = Apply()
win = TestWindow()
RT = Radio()
win.buildUI()

sjTest = cmds.scriptJob( e= ["SelectionChanged","SJTest()"], parent = win.widgets["window"])   
