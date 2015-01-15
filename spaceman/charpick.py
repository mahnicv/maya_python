import maya.cmds as cmds
from functools import partial

class CharacterPicker():
    
    def __init__(self):
        #clas var
        self.widgets = {}
        
        #namespaceINFO
        nameSpaces=cmds.namespaceInfo(listOnlyNamespaces = True)
        self.namespaces = []
        for name in nameSpaces:
            if cmds.objExists(name + ":M_ALL_CTRL"):
                self.namespaces.append(name)   
            else:
                if cmds.objExists(name + ":pelvis"):
                    self.namespaces.append(name)
   
        #call on build UI method
        self.buildUI()
            
        
            
    def buildUI(self):
        def spaceUI():    
            #create buttons
            imageBG=cmds.internalVar(upd=True) + "icons/space.png"
            imageHead=cmds.internalVar(upd=True) + "icons/head.png"
            imageSpine=cmds.internalVar(upd=True) + "icons/spine.png"
            imagePelvis=cmds.internalVar(upd=True) + "icons/pelvis.png"
            imageCOG=cmds.internalVar(upd=True) + "icons/COG.png"
            imageRknee=cmds.internalVar(upd=True) + "icons/Rknee.png"
            imageLknee=cmds.internalVar(upd=True) + "icons/Lknee.png"
            imageRfoot=cmds.internalVar(upd=True) + "icons/Rfoot.png"
            imageLfoot=cmds.internalVar(upd=True) + "icons/Lfoot.png"
            imageRclav=cmds.internalVar(upd=True) + "icons/Rclav.png"
            imageLclav=cmds.internalVar(upd=True) + "icons/Lclav.png"
            imageRelbow=cmds.internalVar(upd=True) + "icons/Relbow.png"
            imageLelbow=cmds.internalVar(upd=True) + "icons/Lelbow.png"
            imageRarm=cmds.internalVar(upd=True) + "icons/Rarm.png"
            imageLarm=cmds.internalVar(upd=True) + "icons/Larm.png"
            imagePATH=cmds.internalVar(upd=True) + "icons/path.png"
            imageALL=cmds.internalVar(upd=True) + "icons/all.png"
            cmds.image(w=400, h=800, image =imageBG)
            
            
            self.widgets[name + "_headButton"] = cmds.iconTextButton(label="",w=70,h=90, ebg = True, st="iconOnly", image1=imageHead, bgc =[1.0,1.0,0.0])
            cmds.iconTextButton(self.widgets[name + "_headButton"], edit=True, c=partial(self.selectControls, [namespace + "M_head_CTRL"], [(self.widgets[name + "_headButton"],[1.0,1.0,0.0])] ))
            
            self.widgets[name + "_spineButton"] = cmds.iconTextButton(label="",w=108,h=115, ebg = True, st="iconOnly",image1=imageSpine,bgc =[1.0,1.0,0.0])
            cmds.iconTextButton(self.widgets[name + "_spineButton"], edit=True, c=partial(self.selectControls, [namespace + "M_spine_CTRL"], [(self.widgets[name + "_spineButton"],[1.0,1.0,0.0])] ))
            
            self.widgets[name + "_pelvisButton"] = cmds.iconTextButton(label="",w=108,h=20, ebg = True, st="iconOnly",image1=imagePelvis,bgc =[1.0,1.0,0.0])
            cmds.iconTextButton(self.widgets[name + "_pelvisButton"], edit=True, c=partial(self.selectControls, [namespace + "M_pelvis_CTRL"], [(self.widgets[name + "_pelvisButton"],[1.0,1.0,0.0])] ))
            
            self.widgets[name + "_COGButton"] = cmds.iconTextButton(label="",w=70,h=45, ebg = True, st="iconOnly",image1=imageCOG,bgc =[1.0,1.0,0.0])
            cmds.iconTextButton(self.widgets[name + "_COGButton"], edit=True, c=partial(self.selectControls, [namespace + "M_COG_CTRL"], [(self.widgets[name + "_COGButton"],[1.0,1.0,0.0])] ))
            
            self.widgets[name + "_RkneeButton"] = cmds.iconTextButton(label="",w=50,h=50, ebg = True, st="iconOnly",image1=imageRknee, bgc =[1.0,0.0,0.0])
            cmds.iconTextButton(self.widgets[name + "_RkneeButton"], edit=True, c=partial(self.selectControls, [namespace + "R_knee_CTRL"], [(self.widgets[name + "_RkneeButton"],[1.0,0.0,0.0])] ))
            
            self.widgets[name + "_LkneeButton"] = cmds.iconTextButton(label="",w=50,h=50, ebg = True, st="iconOnly",image1=imageLknee, bgc =[0.0,0.0,1.0])
            cmds.iconTextButton(self.widgets[name + "_LkneeButton"], edit=True, c=partial(self.selectControls, [namespace + "L_knee_CTRL"], [(self.widgets[name + "_LkneeButton"],[0.0,0.0,1.0])] ))
            
            self.widgets[name + "_RfootButton"] = cmds.iconTextButton(label="",w=55,h=55, ebg = True, st="iconOnly",image1=imageRfoot, bgc =[1.0,0.0,0.0])
            cmds.iconTextButton(self.widgets[name + "_RfootButton"], edit=True, c=partial(self.selectControls, [namespace + "R_foot_CTRL"], [(self.widgets[name + "_RfootButton"],[1.0,0.0,0.0])] ))
            
            self.widgets[name + "_LfootButton"] = cmds.iconTextButton(label="",w=55,h=55, ebg = True, st="iconOnly",image1=imageLfoot, bgc =[0.0,0.0,1.0])
            cmds.iconTextButton(self.widgets[name + "_LfootButton"], edit=True, c=partial(self.selectControls, [namespace + "L_foot_CTRL"], [(self.widgets[name + "_LfootButton"],[0.0,0.0,1.0])] ))
            
            self.widgets[name + "_RclavButton"] = cmds.iconTextButton(label="",w=55,h=55, ebg = True, st="iconOnly",image1=imageRclav, bgc =[1.0,0.0,0.0])
            cmds.iconTextButton(self.widgets[name + "_RclavButton"], edit=True, c=partial(self.selectControls, [namespace + "R_clav_CTRL"], [(self.widgets[name + "_RclavButton"],[1.0,0.0,0.0])] ))
            
            self.widgets[name + "_LclavButton"] = cmds.iconTextButton(label="",w=55,h=55, ebg = True, st="iconOnly",image1=imageLclav, bgc =[0.0,0.0,1.0])
            cmds.iconTextButton(self.widgets[name + "_LclavButton"], edit=True, c=partial(self.selectControls, [namespace + "L_clav_CTRL"], [(self.widgets[name + "_LclavButton"],[0.0,0.0,1.0])] ))
            
            self.widgets[name + "_RelbowButton"] = cmds.iconTextButton(label="",w=55,h=55, ebg = True, st="iconOnly",image1=imageRelbow, bgc =[1.0,0.0,0.0])
            cmds.iconTextButton(self.widgets[name + "_RelbowButton"], edit=True, c=partial(self.selectControls, [namespace + "R_elbow_CTRL"], [(self.widgets[name + "_RelbowButton"],[1.0,0.0,0.0])] ))
            
            self.widgets[name + "_LelbowButton"] = cmds.iconTextButton(label="",w=55,h=55, ebg = True, st="iconOnly",image1=imageLelbow, bgc =[0.0,0.0,1.0])
            cmds.iconTextButton(self.widgets[name + "_LelbowButton"], edit=True, c=partial(self.selectControls, [namespace + "L_elbow_CTRL"], [(self.widgets[name + "_LelbowButton"],[0.0,0.0,1.0])] ))
            
            self.widgets[name + "_RarmButton"] = cmds.iconTextButton(label="",w=55,h=55, ebg = True, st="iconOnly",image1=imageRarm, bgc =[1.0,0.0,0.0])
            cmds.iconTextButton(self.widgets[name + "_RarmButton"], edit=True, c=partial(self.selectControls, [namespace + "R_arm_CTRL"], [(self.widgets[name + "_RarmButton"],[1.0,0.0,0.0])] ))
            
            self.widgets[name + "_LarmButton"] = cmds.iconTextButton(label="",w=55,h=55, ebg = True, st="iconOnly",image1=imageLarm, bgc =[0.0,0.0,1.0])
            cmds.iconTextButton(self.widgets[name + "_LarmButton"], edit=True, c=partial(self.selectControls, [namespace + "L_arm_CTRL"], [(self.widgets[name + "_LarmButton"],[0.0,0.0,1.0])] ))
            
            self.widgets[name + "_feetButton"] = cmds.iconTextButton(label="",w=150,h=10, ebg = True, st="iconOnly", bgc =[1.0,1.0,0.0])
            cmds.iconTextButton(self.widgets[name + "_feetButton"], edit=True, c=partial(self.selectControls, [namespace + "M_feet_CTRL"], [(self.widgets[name + "_feetButton"],[1.0,1.0,0.0])] ))
            
            self.widgets[name + "_pathButton"] = cmds.iconTextButton(label="",w=70,h=70, ebg = True, st="iconOnly",image1=imagePATH, bgc =[1.0,1.0,0.0])
            cmds.iconTextButton(self.widgets[name + "_pathButton"], edit=True, c=partial(self.selectControls, [namespace + "M_PATH_CTRL"], [(self.widgets[name + "_pathButton"],[1.0,1.0,0.0])] ))
            
            self.widgets[name + "_allButton"] = cmds.iconTextButton(label="",w=70,h=70, ebg = True, st="iconOnly",image1=imageALL, bgc =[1.0,1.0,0.0])
            cmds.iconTextButton(self.widgets[name + "_allButton"], edit=True, c=partial(self.selectControls, [namespace + "M_ALL_CTRL"], [(self.widgets[name + "_allButton"],[1.0,1.0,0.0])] ))
            
            self.widgets[name + "_selectAll"] = cmds.iconTextButton(label="",w=15,h=570, ebg = True, st="iconOnly",bgc =[0.0,1.0,0])
            cmds.iconTextButton(self.widgets[name + "_selectAll"], ebg = True, edit=True, c=partial(self.selectControls, [namespace + "M_head_CTRL", namespace + "M_spine_CTRL", namespace + "M_pelvis_CTRL", namespace + "M_COG_CTRL",namespace + "R_knee_CTRL",namespace + "L_knee_CTRL",namespace + "R_foot_CTRL",namespace + "L_foot_CTRL",namespace + "R_clav_CTRL",namespace + "L_clav_CTRL", namespace + "R_elbow_CTRL",namespace + "L_elbow_CTRL",namespace + "R_arm_CTRL",namespace + "L_arm_CTRL",namespace + "M_feet_CTRL"], [(self.widgets[name + "_headButton"],[1.0,1.0,0.0]), (self.widgets[name + "_spineButton"],[1.0,1.0,0.0]), (self.widgets[name + "_pelvisButton"],[1.0,1.0,0.0]), (self.widgets[name + "_COGButton"],[1.0,1.0,0.0]), (self.widgets[name + "_RkneeButton"],[1.0,0.0,0.0]), (self.widgets[name + "_LkneeButton"],[0.0,0.0,1.0]), (self.widgets[name + "_RfootButton"],[1.0,0.0,0.0]), (self.widgets[name + "_LfootButton"],[0.0,0.0,1.0]),(self.widgets[name + "_RclavButton"],[1.0,0.0,0.0]),(self.widgets[name + "_LclavButton"],[0.0,0.0,1.0]),(self.widgets[name + "_RelbowButton"],[1.0,0.0,0.0]),(self.widgets[name + "_LelbowButton"],[0.0,0.0,1.0]), (self.widgets[name + "_RarmButton"],[1.0,0.0,0.0]),(self.widgets[name + "_LarmButton"],[0.0,0.0,1.0]),(self.widgets[name + "_feetButton"],[1.0,1.0,0.0])        ] ))
            
            #place buttons
            
            cmds.formLayout(self.widgets[name + "_formLayout"], edit = True, af = [(self.widgets[name + "_headButton"], 'left', 162), (self.widgets[name + "_headButton"], 'top', 9)])
            cmds.formLayout(self.widgets[name + "_formLayout"], edit = True, af = [(self.widgets[name + "_spineButton"], 'left', 143), (self.widgets[name + "_spineButton"], 'top', 110)])
            cmds.formLayout(self.widgets[name + "_formLayout"], edit = True, af = [(self.widgets[name + "_pelvisButton"], 'left', 143), (self.widgets[name + "_pelvisButton"], 'top', 230)])
            cmds.formLayout(self.widgets[name + "_formLayout"], edit = True, af = [(self.widgets[name + "_COGButton"], 'left', 162), (self.widgets[name + "_COGButton"], 'top', 262)])
            cmds.formLayout(self.widgets[name + "_formLayout"], edit = True, af = [(self.widgets[name + "_RkneeButton"], 'left', 133), (self.widgets[name + "_RkneeButton"], 'top', 390)])
            cmds.formLayout(self.widgets[name + "_formLayout"], edit = True, af = [(self.widgets[name + "_LkneeButton"], 'left', 211), (self.widgets[name + "_LkneeButton"], 'top', 390)])
            cmds.formLayout(self.widgets[name + "_formLayout"], edit = True, af = [(self.widgets[name + "_RfootButton"], 'left', 128), (self.widgets[name + "_RfootButton"], 'top', 529)])
            cmds.formLayout(self.widgets[name + "_formLayout"], edit = True, af = [(self.widgets[name + "_LfootButton"], 'left', 211), (self.widgets[name + "_LfootButton"], 'top', 529)])
            cmds.formLayout(self.widgets[name + "_formLayout"], edit = True, af = [(self.widgets[name + "_RclavButton"], 'left', 85), (self.widgets[name + "_RclavButton"], 'top', 88)])
            cmds.formLayout(self.widgets[name + "_formLayout"], edit = True, af = [(self.widgets[name + "_LclavButton"], 'left', 252), (self.widgets[name + "_LclavButton"], 'top', 88)])
            cmds.formLayout(self.widgets[name + "_formLayout"], edit = True, af = [(self.widgets[name + "_RelbowButton"], 'left', 70), (self.widgets[name + "_RelbowButton"], 'top', 180)])
            cmds.formLayout(self.widgets[name + "_formLayout"], edit = True, af = [(self.widgets[name + "_LelbowButton"], 'left', 269), (self.widgets[name + "_LelbowButton"], 'top', 180)])
            cmds.formLayout(self.widgets[name + "_formLayout"], edit = True, af = [(self.widgets[name + "_RarmButton"], 'left', 40), (self.widgets[name + "_RarmButton"], 'top', 285)])
            cmds.formLayout(self.widgets[name + "_formLayout"], edit = True, af = [(self.widgets[name + "_LarmButton"], 'left', 300), (self.widgets[name + "_LarmButton"], 'top', 285)])
            cmds.formLayout(self.widgets[name + "_formLayout"], edit = True, af = [(self.widgets[name + "_feetButton"], 'left', 120), (self.widgets[name + "_feetButton"], 'top', 595)])
            cmds.formLayout(self.widgets[name + "_formLayout"], edit = True, af = [(self.widgets[name + "_pathButton"], 'left', 120), (self.widgets[name + "_pathButton"], 'top', 615)])
            cmds.formLayout(self.widgets[name + "_formLayout"], edit = True, af = [(self.widgets[name + "_allButton"], 'left', 200), (self.widgets[name + "_allButton"], 'top', 615)])
            cmds.formLayout(self.widgets[name + "_formLayout"], edit = True, af = [(self.widgets[name + "_selectAll"], 'left', 370), (self.widgets[name + "_selectAll"], 'top', 30)])



            
            
        if cmds.dockControl("characterPicker_dock", exists = True):
            cmds.deleteUI("characterPicker_dock")

        self.widgets["window"] = cmds.window(w=400, h=600, mnb=False, mxb=False)
        self.widgets["mainLayout"] = cmds.columnLayout(w=400, h=600)
        self.widgets["tabLayout"] = cmds.tabLayout()
        for name in self.namespaces:
            
            self.widgets[name + "_formLayout"] = cmds.formLayout(w=400, h=700, parent = self.widgets["tabLayout"])
            
            namespace = name +":"
            
            if name == "spaceman_RIG":
                spaceUI()
                
            cmds.tabLayout(self.widgets["tabLayout"], edit = True, tabLabel = ((self.widgets[name + "_formLayout"], name)))
            cmds.dockControl("characterPicker_dock",  label = "Character Pick", area ="left", allowedArea= "left", content=self.widgets["window"])
        
    def selectControls(self, controls, buttonInfo, *args):
        mods = cmds.getModifiers()
        #shift mod
        if (mods & 1 > 0):
            for i in range (len(controls)):
                cmds.select(controls[i], tgl = True)
                buttonName = buttonInfo [i][0]
                buttonBGC = buttonInfo [i][1]
                
                cmds.iconTextButton(buttonName, ebg = True, st="iconOnly",edit = True, bgc = [1.0,1.0,1.0])
                ++i
                
                #call scriptjob
                self.createSelectionScriptJob(controls[i], buttonName, buttonBGC)
                
        else:    
            cmds.select(clear = True)
            for i in range (len(controls)):
                cmds.select(controls[i], add = True)
                buttonName = buttonInfo [i][0]
                buttonBGC = buttonInfo [i][1]
                
                cmds.iconTextButton(buttonName, ebg = True, st="iconOnly",edit = True, bgc = [1.0,1.0,1.0])
                ++i
                
                #call scriptjob
                self.createSelectionScriptJob(controls[i], buttonName, buttonBGC)    
     
                
                    
    
    def createSelectionScriptJob(self, control, buttonName, buttonBGC):
        scriptJobNum = cmds.scriptJob(event = ["SelectionChanged", partial(self.deselectButton, control, buttonName, buttonBGC)], runOnce=True, parent = self.widgets["window"])
    
    def deselectButton(self, control, buttonName, buttonBGC):
        selection = cmds.ls(sl = True)
        
        if control not in selection:
            cmds.iconTextButton(buttonName, edit = True, bgc = buttonBGC)
        else:
            self.createSelectionScriptJob(control, buttonName, buttonBGC)    
#CharacterPicker()              
