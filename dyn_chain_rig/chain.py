##jointChain - Victor Mahnic

import maya.cmds as cmds
import maya.mel as mel

incX = 0
jointNum = 0
count = 0
jointDist = 0

if cmds.dockControl('chainUI', exists=True):
    cmds.deleteUI('chainUI')
    
window = cmds.window(title='jointChain', s=True, wh=(215, 100), tlb=True)
cmds.rowColumnLayout()
cmds.iconTextButton(fla=False,style='iconAndTextHorizontal', image1='curveEP.png', l='Create EP Curve', w=210, h=35, c='curvecreateEP()')
cmds.iconTextButton(fla=False,style='iconAndTextHorizontal', image1='pencil.png',l='Create Pen Curve', w=210, h=35, c='curvecreatePE()')
cmds.separator( height=20, style='in' )
cmds.text(l='Number of Joints:')
cmds.intField( ['jointsNo'], minValue=1, step=1)
cmds.separator( height=10, style='none' )
cmds.text(l='Joint Name:')
cmds.textField('JNT_name')
cmds.separator( height=20, style='in' )
cmds.iconTextButton(fla=False,style='iconAndTextHorizontal', image1='kinSplineHandle.png',l='Create Chain', w=210, h=35, c='crv()')
cmds.dockControl('chainUI', area='left', content=window, allowedArea='left', l='Dyn Chain Rigger' )


def curvecreatePE():
    cmds.PencilCurveTool()

def curvecreateEP():
    cmds.EPCurveTool()
    
# rebuilds & smooths curve #
def crv():
    global jointNum
    global CV
    jointNum=cmds.intField('jointsNo', q=True, value=True)
    CV = jointNum - 3
    cmds.rebuildCurve ('curve1', rt=0, ch=1, rpo=1, end=0, kr=0, kcp=0 ,kep=1, kt=1, s=CV, d=3, tol=0.01 )
    cmds.smoothCurve('curve1.cv[*]', s=20)
    spans = cmds.getAttr('curveShape1.spans')
    deg = cmds.getAttr('curveShape1.degree')
    CBS = spans + deg - 1
    vtxJnt()

## - creates joints along curve CV    
def vtxJnt():
    global jointNum
    cmds.select('curve1.cv[*]') 
    jointName=cmds.textField('JNT_name', q=True, tx=True) + '_%s'
    cnt = 1
    crv = cmds.ls(sl=True)[0]
    cvs = cmds.getAttr("%s" % crv)
    for cv in cvs:
        cmds.joint(p=cv)
        cmds.rename('joint1', jointName % cnt)
        cnt = cnt +1
    cmds.parent(jointName %1, w=True)
    cmds.joint(jointName %1, e=True, ch=True, oj='xyz', sao='yup', zso=True)
    cmds.joint(jointName %jointNum, e=True, oj='none', zso=True)
    cmds.delete('curve1')
    IK_spline()

## - Creates joint Chain
def JNT_chain_btn():
    global incX
    global jointNum
    global count
    global jointDist
    global jointName
    global IK
    global CRV
    jointNum=cmds.floatField('jointsNo', q=True, value=True)
    jointDist=cmds.floatField('chainLength', q=True, value=True)/ (jointNum -1)
    jointName=cmds.textField('JNT_name', q=True, tx=True) + '_%s'
    IK= 'IK_'+cmds.textField('JNT_name', q=True, tx=True)
    while count < jointNum :
        count = count +1
        cmds.joint(name=jointName %count, p=(incX,0,0))
        print 'joint_%s : dist_%s : ' % (count+1, incX) + jointName
        incX = incX + jointDist
    else:
        incX = 0
        IK_spline()
        
## - Adds IK spline to joint chain        
def IK_spline():
    global count
    global CRV_IK
    global CRV_MAN
    global CRV_DYNIN
    global CRV_DYNOUT
    global CRV
    global jointNum
    global jointNum
    global CV
    IK= 'IK_'+cmds.textField('JNT_name', q=True, tx=True)
    CRV= 'CRV_' +cmds.textField('JNT_name', q=True, tx=True)
    jointName=cmds.textField('JNT_name', q=True, tx=True) + '_%s'
    jointNum=cmds.intField('jointsNo', q=True, value=True)
    CV = jointNum - 3
    Ccount = 0
    CRV_IK=CRV+'_IK'
    CRV_MAN=CRV+'_MAN'
    CRV_DYNIN=CRV+'_DYNIN'
    CRV_DYNOUT=CRV+'_DYNOUT'
    CLUST = 'CLUST_'+jointName
    CTRL = 'CTRL_'+jointName
    cmds.ikHandle( n=IK, sj=jointName %1, ee=jointName %jointNum,sol='ikSplineSolver', scv=False)
    cmds.rebuildCurve ('curve1', rt=0, ch=1, rpo=1, end=0, kr=0, kcp=0 ,kep=1, kt=1, s=CV, d=3, tol=0.01 )
    cmds.smoothCurve('curve1.cv[*]', s=1)
    cmds.duplicate('curve1')
    cmds.duplicate('curve1')
    cmds.rename('curve1', CRV_IK)
    cmds.rename('curve2', CRV_MAN)
    cmds.rename('curve3', CRV_DYNIN)
    deg=cmds.getAttr( CRV_MAN+'.degree' )
    spans=cmds.getAttr( CRV_MAN+'.spans' )
    cv= deg + spans
    count=1
    while Ccount < jointNum:
        CLUST = 'CLUST_'+jointName % count
        CTRL = 'CTRL_'+jointName % count
        GRP = 'GRP_'+jointName % count
        cmds.select(CRV_MAN + '.cv[%s]' % Ccount)
        cmds.cluster(n=CLUST)
        cmds.circle(n=CTRL, r=7)
        cmds.group(CTRL, n=GRP)
        cmds.parentConstraint( CLUST+'Handle', CTRL)
        cmds.parentConstraint( CLUST+'Handle', CTRL, rm = True)
        cmds.setAttr(CLUST+'Handle.visibility', 0)
        cmds.parent(GRP, jointName % count, r=True)
        cmds.setAttr(CTRL + '.tx', 0)
        cmds.setAttr(CTRL + '.ty', 0)
        cmds.setAttr(CTRL + '.tz', 0)
        cmds.setAttr(CTRL + '.ry', 90)
        cmds.makeIdentity( apply=True, t=1, r=1, s=1, n=2 )
        cmds.parent(GRP, w=True)
        cmds.parent(CLUST+'Handle', CTRL)
        count = count + 1
        Ccount = Ccount + 1
    else:
        Ccount = 1
        count = count -1
        countrev = count -1
        while count > Ccount:
            CTRLREV = 'CTRL_'+jointName % countrev
            GRP = 'GRP_'+jointName % count
            print 'count: %s' %count
            print 'CCount: %s' %Ccount
            print 'countrev: %s'% countrev
            cmds.parent(GRP, CTRLREV)
            count = count - 1
            countrev = countrev -1
        else:
            BS_DYN()

## - Adds Blend shapes and Dynamics
def BS_DYN():
    global JNT
    global CRV_DYNIN
    global CRV_IK
    global DYNOUT
    JNT=cmds.textField('JNT_name', q=True, tx=True)
    #cmds.select()
    #cmds.select(CRV_IK, add=True)
    cmds.blendShape(CRV_MAN, CRV_DYNIN, name='BS_onAlways_'+JNT) 
    cmds.blendShape('BS_onAlways_'+JNT, edit=True, w=[(0, 1), (1, 0)])
    #print CRV_DYNIN
    cmds.select(CRV_DYNIN)
    mel.eval('makeCurvesDynamic 2 { "0", "0", "1", "1", "1" }')
    cmds.setAttr(CRV_DYNIN+'.inheritsTransform', 0)
    cmds.rename('hairSystem1Follicles', 'GRP_'+JNT+'_Follicles')
    cmds.rename('follicle1',JNT+'_follicle')
    cmds.rename('curve1', CRV_DYNOUT)
    cmds.rename('hairSystem1OutputCurves', 'GRP_'+JNT+'_OutputCurves')
    cmds.blendShape(CRV_DYNOUT, CRV_MAN, CRV_IK, name='BS_DYNMAN_'+JNT)
    cmds.shadingNode('reverse', n='REV_dynman_'+JNT, asShader=True)
    cmds.circle(n='CTRL_ALL_'+ JNT, r=10)
    cmds.parent('CTRL_ALL_' +JNT, JNT + '_1', r=True)
    cmds.setAttr('CTRL_ALL_' +JNT + '.ry', 90)
    cmds.makeIdentity( apply=True, t=1, r=1, s=1, n=2 )
    cmds.parent('CTRL_ALL_' +JNT, w=True)
    cmds.makeIdentity( apply=True, t=1, r=1, s=1, n=2 )
    cmds.addAttr(ln='DYN_ALL2', at='double', min = 0, max=1, dv =1, k =True)
    cmds.addAttr(ln='Point_Lock', at='enum', enumName = 'None:Base:Tip:Both', k = True)
    cmds.setAttr('CTRL_ALL_' +JNT+'.Point_Lock', 3)
    cmds.connectAttr ('CTRL_ALL_' +JNT+'.Point_Lock', JNT+'_follicleShape.pointLock')
    cmds.connectAttr('CTRL_ALL_'+JNT+'.DYN_ALL2', 'REV_dynman_'+JNT+'.inputX')
    cmds.connectAttr('CTRL_ALL_'+JNT+'.DYN_ALL2', 'BS_DYNMAN_'+JNT+'.CRV_'+JNT+'_DYNOUT')
    cmds.connectAttr('REV_dynman_'+JNT+'.outputX', 'BS_DYNMAN_'+JNT+'.CRV_'+JNT+'_MAN')
    cmds.parent('GRP_'+JNT+'_1', 'GRP_'+JNT+'_Follicles')
    cmds.parent('GRP_'+JNT+'_Follicles', 'CTRL_ALL_' +JNT)
    bind()


#attempt to bind stuff
def bind():
    cmds.bindSkin( 'GEO_test', JNT+'_1')
