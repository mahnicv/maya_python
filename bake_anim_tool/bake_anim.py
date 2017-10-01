import maya.cmds as cmds
#FILE DIRECTORY AND FILENAME - for saving out FBX (change this as needed).
DIR = "C:\Workspace\\"
FN = "character@anim_loop.fbx"


BIND = []
trash = []
GRP = ['CTRL_GRP', 'MISC_GRP', 'L_hand_GRP', 'R_hand_GRP', 'GEO_GRP']
sFrame = cmds.playbackOptions(min=True, q=True)
eFrame = cmds.playbackOptions(max=True, q=True)
selected = cmds.ls(type='joint')
refs = cmds.ls(type='reference')
rFile = cmds.referenceQuery(refs[0], f=True)

#import referenced rigs.
cmds.file(rFile, importReference=True)

#splits all joints in scene into either the BIND list(for baking anim) or trash list (for deleting).
for jnt in selected:
    if jnt.split('_')[-1] == 'BIND':
        BIND.append(jnt)
    else:
        trash.append(jnt)
        
#selects all BIND joints and bakes frames according to timeline length.
cmds.select(BIND, r=True)
cmds.bakeResults(BIND, sm=True, pok=True, dic=True, bol=False, s=True, t=(sFrame,eFrame))

#selects trash list and other unwanted groups - deletes them.
cmds.select(trash, r=True)
cmds.select(GRP, add=True)
cmds.delete()

#saves out FBX file
cmds.file(rename=DIR+FN)
cmds.file(force=True, options="v=0;", de=False, type="FBX export", pr=True, ea=True)