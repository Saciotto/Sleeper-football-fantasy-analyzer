# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 6.3.0
# WARNING! All changes made in this file will be lost!

from PySide6 import QtCore

qt_resource_data = b"\
\x00\x00\x00\xa9\
m\
odule components\
\x0d\x0aNavigationButt\
on 1.0 Navigatio\
nButton.qml\x0d\x0aNav\
igationBar 1.0 N\
avigationBar.qml\
\x0d\x0aPlayerDelegate\
 1.0 PlayerDeleg\
ate.qml\x0d\x0aPlayerL\
ist 1.0 PlayerLi\
st.qml\x0d\x0a\
\x00\x00\x05|\
i\
mport QtQuick\x0d\x0ai\
mport QtQuick.Co\
ntrols\x0d\x0a\x0d\x0aimport\
 assets 1.0\x0d\x0a\x0d\x0aI\
tem {\x0d\x0a    prope\
rty var player\x0d\x0a\
\x0d\x0a    id: root\x0d\x0a\
    implicitHeig\
ht: playerPositi\
on.height + 4\x0d\x0a \
   Rectangle {\x0d\x0a\
        id: play\
erPosition\x0d\x0a    \
    anchors {\x0d\x0a \
           left:\
 parent.left\x0d\x0a  \
          vertic\
alCenter: parent\
.verticalCenter\x0d\
\x0a        }\x0d\x0a    \
    width: 30\x0d\x0a \
       height: 2\
0\x0d\x0a        color\
: {\x0d\x0a           \
 switch (player.\
fantasy_position\
s[0]) {\x0d\x0a       \
     case 'QB':\x0d\
\x0a               \
 return Style.qb\
BackgroundColor;\
\x0d\x0a            ca\
se 'RB':\x0d\x0a      \
          return\
 Style.rbBackgro\
undColor;\x0d\x0a     \
       case 'WR'\
:\x0d\x0a             \
   return Style.\
wrBackgroundColo\
r;\x0d\x0a            \
case 'TE':\x0d\x0a    \
            retu\
rn Style.teBackg\
roundColor;\x0d\x0a   \
         case 'D\
L':\x0d\x0a           \
     return Styl\
e.dlBackgroundCo\
lor;\x0d\x0a          \
  case 'LB':\x0d\x0a  \
              re\
turn Style.lbBac\
kgroundColor;\x0d\x0a \
           case \
'DB':\x0d\x0a         \
       return St\
yle.dbBackground\
Color;\x0d\x0a        \
    }\x0d\x0a         \
   return Style.\
genericBackgroun\
dColor;\x0d\x0a       \
 }\x0d\x0a        radi\
us: 5\x0d\x0a        L\
abel {\x0d\x0a        \
    anchors.fill\
: parent\x0d\x0a      \
      text: play\
er.fantasy_posit\
ions[0]\x0d\x0a       \
     horizontalA\
lignment: Label.\
AlignHCenter\x0d\x0a  \
      }\x0d\x0a    }\x0d\x0a\
    Label {\x0d\x0a   \
     anchors {\x0d\x0a\
            left\
: playerPosition\
.right\x0d\x0a        \
    leftMargin: \
4\x0d\x0a            v\
erticalCenter: p\
arent.verticalCe\
nter\x0d\x0a        }\x0d\
\x0a        text: p\
layer.full_name\x0d\
\x0a    }\x0d\x0a}\x0d\x0a\
\x00\x00\x02\x10\
\x00\
\x00\x08\xe7x\x9c\xd5T\xb1n\xdb0\x10\xdd\xf5\x15\x84\
&{Q\x1ad\x88\xa1 K\x5c\xb4\x08\x10\x14H\x1b\
\xa4K\x17Z:\xcbD)R>\x9e\x12\x18\x85\xff=\
\xa4%\xd9\xa2\xe8\xd4J\x0a\x04('\x9d\xf8\xde\xf1\xf1\
\x1d\xefDYi$vO\xf7\xb5\xc8~G\x91hb\
n\x0c\x90a\xe7\xc9\xa7(\xba%(\xd9\x9f\x88\xd9U\
\xa1\xae\x00i\xc3\x0c\xa1P\x053 !#\xc8\x1f\x05\
<\xa7,\x8e\xa3\x1d\x0a\x81\xe7Z\xc9M\x00\xcf\xb9Y\
-4\xc7\x0e\xff\xb9\x1f\xc7\x7f\xe7.\xc0\xd0\x9dPP\
W-\xf9\xc6\xfbq\x82M\xc0\xcb\x96w\xa7\x0b\xa1\x1a\
\xca\x8e3\xd7J\xd9K\x08\xadL{K\xb7\x88c\x01\
\x94\xb2\x92\x1b\x02\xb4\x18B-%`\xa2\xf8\x93(\xb8\
\x83\x1f~\xeeY\xcbZ\xed21\xad\xbej\xefv\x93\
i/\xb9[}\xeb\xd8\xb5o\xcd\x95\x87\x14K6\x09\
dHw\x0b?. \x1f\x1e\xd2xB5*\x96Y\
,(\xfa\x82\xbc\x84\x04\xa1\x92<\x83I\xbc\xc6,=\
{\xb2G\x9a3On\xb2.e<\xf5ul\x19H\
\x03\xffp\xc2\xde\xf9\xa3\xd9\xa3\xf0\xcb\xb3\xf3\xa1-\xe1\
)'\xbbR\xfb\xe9\xc7j\xecN\x19J|E\x94\xff\
\x08OI\xf3\xdf\xf0\xfb\x04\xfa'\x1e\x97\xb9m^\xf6\
\xb3\xc8i\x95\xb2\x1f\xb4\x91\xd0{\xb77\x1c\x7f\xba\x9d\
\x06\xf4\xdd\x0a\xe4\xaa\x90\xfd\xc2r\x95\xad4\x9ad)\
\xa4LY\xc5\xd1*\xdaofZj<\x9au\xeev\
\xf68\x1b\xd5\xa5\x1a\x18\xd2JjR&\xbb\xc8\xdb\xff\
v\xc8W\x13\xe9!\xdd-a-\x9a\xaf8rk\xac\
\xd5\x11\xff\xaaavy\x1e\x07\xb8\x1cL\x86\xa2r\xb9\
R\xb66\x0f89\xcc\x9bx\x1a\xc0\xbbR\xa5\x83\xa2\
]\x0fz3 j5\x14=\x97v\x94\xbaL\xa1x\
\xb7F\x8d\x94\xa4\x18\xce\x8f\xab \xd9\xf6\x95\x06z\xbf\
\x91\x97\xb0\x1ce\xa4\xeb\x92\xb7y\xd8ue\xc0\x01\xc5\
\x17\xd2QF\x8e\xb8\x8f\xf3\xff0p>\xc2\xfa\xd9\xc5\
l\x94\xf5\xae\xffY3\x00\xdeV\x01\x7f\xf8\xfcGu\
\x18\xce\xd8\xf1\xd5\xe8\xa6\xe16z\x01o\xa4\x9d\xe7\
\x00\x00\x01\x22\
i\
mport QtQuick\x0d\x0ai\
mport QtQuick.Co\
ntrols\x0d\x0a\x0d\x0aimport\
 assets 1.0\x0d\x0a\x0d\x0aI\
tem {\x0d\x0a    id: r\
oot\x0d\x0a    propert\
y string players\
\x0d\x0a\x0d\x0a    ListView\
 {\x0d\x0a        anch\
ors.fill: parent\
\x0d\x0a        model:\
 JSON.parse(root\
.players)\x0d\x0a     \
   delegate: Pla\
yerDelegate {\x0d\x0a \
           playe\
r: modelData\x0d\x0a  \
      }\x0d\x0a    }\x0d\x0a\
}\
\x00\x00\x08^\
i\
mport QtQuick\x0aim\
port QtQuick.Con\
trols\x0a\x0aimport as\
sets 1.0\x0a\x0aItem {\
\x0a    property al\
ias iconCharacte\
r: iconCharacter\
.text\x0a    proper\
ty alias descrip\
tion: descriptio\
n.text\x0a    prope\
rty bool selecte\
d: false\x0a\x0a    si\
gnal navigationB\
uttonClicked()\x0a\x0a\
    width: Style\
.navigationBarWi\
dth\x0a    height: \
Style.navigation\
ButtonHeight\x0a\x0a  \
  Rectangle {\x0a  \
      id: backgr\
ound\x0a        anc\
hors.fill: paren\
t\x0a        color:\
 selected ? Styl\
e.navigationButt\
onPressedColor :\
 Style.navigatio\
nButtonColor\x0a\x0a  \
      Rectangle \
{\x0a            id\
: selectionIndic\
ator\x0a           \
 width: 4\x0a      \
      anchors.le\
ft: parent.left\x0a\
            anch\
ors.top: parent.\
top\x0a            \
anchors.bottom: \
parent.bottom\x0a  \
          color:\
 Style.navigatio\
nButtonSelection\
IndicatorColor\x0a \
           visib\
le: selected\x0a   \
     }\x0a\x0a        \
Column {\x0a       \
     spacing: St\
yle.navigationBu\
ttonSpacing\x0a    \
        anchors.\
centerIn: parent\
\x0a            Lab\
el {\x0a           \
     id: iconCha\
racter\x0a         \
       width: ba\
ckground.width\x0a \
               t\
ext: \x22\x5cue000\x22\x0a  \
              fo\
nt {\x0a           \
         family:\
 Style.fontMater\
ialIcons\x0a       \
             pix\
elSize: Style.na\
vigationButtonIc\
onPixSize\x0a      \
          }\x0a    \
            hori\
zontalAlignment:\
 Text.AlignHCent\
er\x0a            }\
\x0a            Lab\
el {\x0a           \
     id: descrip\
tion\x0a           \
     width: back\
ground.width\x0a   \
             fon\
t.pixelSize: Sty\
le.navigationBut\
tonTextPixSize\x0a \
               t\
ext: \x22SET ME!!\x22\x0a\
                \
horizontalAlignm\
ent: Text.AlignH\
Center\x0a         \
   }\x0a        }\x0a\x0a\
        MouseAre\
a {\x0a            \
id: mouseArea\x0a  \
          anchor\
s.fill: parent\x0a \
           curso\
rShape: Qt.Point\
ingHandCursor\x0a  \
          enable\
d: parent.enable\
d && !selected\x0a \
           hover\
Enabled: parent.\
enabled && !sele\
cted\x0a           \
 onEntered: back\
ground.state = \x22\
hover\x22;\x0a        \
    onExited: ba\
ckground.state =\
 \x22\x22\x0a            \
onClicked: navig\
ationButtonClick\
ed()\x0a        }\x0a\x0a\
        states: \
[\x0a            St\
ate {\x0a          \
      name: \x22hov\
er\x22\x0a            \
    PropertyChan\
ges {\x0a          \
          target\
: background\x0a   \
                \
 color: Style.na\
vigationButtonHo\
veredColor\x0a     \
           }\x0a   \
         }\x0a     \
   ]\x0a    }\x0a}\x0a\
"

qt_resource_name = b"\
\x00\x0a\
\x07j\x093\
\x00c\
\x00o\x00m\x00p\x00o\x00n\x00e\x00n\x00t\x00s\
\x00\x06\
\x07\x84+\x02\
\x00q\
\x00m\x00l\x00d\x00i\x00r\
\x00\x12\
\x00\x06@\xbc\
\x00P\
\x00l\x00a\x00y\x00e\x00r\x00D\x00e\x00l\x00e\x00g\x00a\x00t\x00e\x00.\x00q\x00m\
\x00l\
\x00\x11\
\x02\xcdk\x9c\
\x00N\
\x00a\x00v\x00i\x00g\x00a\x00t\x00i\x00o\x00n\x00B\x00a\x00r\x00.\x00q\x00m\x00l\
\
\x00\x0e\
\x05\xb8\xcf\x9c\
\x00P\
\x00l\x00a\x00y\x00e\x00r\x00L\x00i\x00s\x00t\x00.\x00q\x00m\x00l\
\x00\x14\
\x08\xdb(\x5c\
\x00N\
\x00a\x00v\x00i\x00g\x00a\x00t\x00i\x00o\x00n\x00B\x00u\x00t\x00t\x00o\x00n\x00.\
\x00q\x00m\x00l\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x05\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00,\x00\x00\x00\x00\x00\x01\x00\x00\x00\xad\
\x00\x00\x01\x80\xab\x1f\x1d\xf8\
\x00\x00\x00V\x00\x01\x00\x00\x00\x01\x00\x00\x06-\
\x00\x00\x01\x80\x9fi8\x83\
\x00\x00\x00~\x00\x00\x00\x00\x00\x01\x00\x00\x08A\
\x00\x00\x01\x80\xab\x11L\xe3\
\x00\x00\x00\x1a\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x80\xaa\xecj\xac\
\x00\x00\x00\xa0\x00\x00\x00\x00\x00\x01\x00\x00\x09g\
\x00\x00\x01\x80\x8c\x8f4\x8f\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
